from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Ensure email is unique
    is_staff = models.BooleanField(default=True)  # Provide staff access by default

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Username is required but email is primary

    def __str__(self):
        return self.email


class Product(models.Model):
    SELL_TO_CUSTOMER = 'customer'
    SELL_TO_APP = 'app'
    SALE_TYPE_CHOICES = [
        (SELL_TO_CUSTOMER, 'Sell to Customer'),
        (SELL_TO_APP, 'Sell to App')
    ]

    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    sale_type = models.CharField(max_length=20, choices=SALE_TYPE_CHOICES)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="cart")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


class Order(models.Model):
    PENDING = 'Pending'
    PAID = 'Paid'
    SHIPPED = 'Shipped'
    DELIVERED = 'Delivered'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (PAID, 'Paid'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered')
    ]

    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    source_address = models.TextField(blank=True, null=True)
    destination_address = models.TextField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=PENDING)
    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product.name}"


class Transaction(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    commission_fee = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction for Order #{self.order.id}"


class Transport(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    driver_name = models.CharField(max_length=255)
    vehicle_number = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default="In Transit")  # In Transit, Delivered
    delivery_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Transport for Order #{self.order.id}"