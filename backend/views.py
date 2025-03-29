from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Product, Order, Transaction, Transport, Cart, CustomUser
from .serializers import ProductSerializer, OrderSerializer, TransactionSerializer, TransportSerializer, CartSerializer
import razorpay
from django.conf import settings

razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        product = request.data.get('product')
        quantity = request.data.get('quantity', 1)
        user = request.user

        product_object = get_object_or_404(Product, id=product)

        cart_item, created = Cart.objects.get_or_create(user=user, product=product_object)
        if not created:
            cart_item.quantity += int(quantity)
            cart_item.save()

        return Response({'message': 'Product added to cart successfully'}, status=status.HTTP_201_CREATED)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        cart_items = Cart.objects.filter(user=user)
        if not cart_items:
            return Response({"message": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

        orders = []
        total_amount = 0
        for cart_item in cart_items:
            order = Order.objects.create(
                buyer=user,
                product=cart_item.product,
                quantity=cart_item.quantity,
                total_price=cart_item.product.price * cart_item.quantity
            )
            orders.append(order)
            total_amount += order.total_price

        Cart.objects.filter(user=user).delete()  # Clear cart after order is placed

        # Razorpay Payment
        razorpay_order = razorpay_client.order.create({
            "amount": int(total_amount * 100),  # Razorpay works with paise
            "currency": "INR",
            "payment_capture": "1"
        })

        for order in orders:
            order.razorpay_order_id = razorpay_order['id']
            order.save()

        return Response({
            "message": "Order placed successfully",
            "razorpay_order_id": razorpay_order['id'],
            "total_amount": total_amount
        }, status=status.HTTP_201_CREATED)


class PaymentVerifyViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        razorpay_order_id = request.data.get("razorpay_order_id")
        razorpay_payment_id = request.data.get("razorpay_payment_id")
        razorpay_signature = request.data.get("razorpay_signature")

        try:
            razorpay_client.utility.verify_payment_signature({
                "razorpay_order_id": razorpay_order_id,
                "razorpay_payment_id": razorpay_payment_id,
                "razorpay_signature": razorpay_signature
            })

            order = Order.objects.get(razorpay_order_id=razorpay_order_id)
            order.status = "Paid"
            order.save()

            return Response({"message": "Payment verified and order confirmed"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TransportViewSet(viewsets.ModelViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    permission_classes = [IsAuthenticated]


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

class UpdateUsernameView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        new_username = request.data.get("username")

        if not new_username:
            return Response({"error": "Username cannot be empty"}, status=status.HTTP_400_BAD_REQUEST)

        user.username = new_username
        user.save()

        return Response({"message": "Username updated successfully"}, status=status.HTTP_200_OK)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not user.check_password(old_password):
            return Response({"error": "Old password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

class ForgotPasswordView(APIView):
    def post(self, request):
        email = request.data.get("email")

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({"error": "User with this email does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        token = default_token_generator.make_token(user)

        # Send email with token and user ID
        send_mail(
            subject="Password Reset Request",
            message=f"Use this token to reset your password in the app:\n\nUser Name: {user.username}\nToken: {token}",
            from_email=settings.EMAIL_HOST_USER,  # Correct setting
            recipient_list=[email],
            fail_silently=False,  # Ensure errors are raised
        )
        return Response({"message": "Password reset token sent to your email"}, status=status.HTTP_200_OK)

class ResetPasswordView(APIView):
    def post(self, request):
        username = request.data.get("username")
        token = request.data.get("token")
        new_password = request.data.get("new_password")


        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return Response({"error": "Invalid user"}, status=status.HTTP_400_BAD_REQUEST)

        if not default_token_generator.check_token(user, token):
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)
        if  not new_password:
            return  Response({"error": "New Password Missing!!"})
        user.set_password(new_password)
        user.save()

        return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)
