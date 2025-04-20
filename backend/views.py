# import json
#
# from django.conf import Settings, settings
# from django.core.mail import send_mail
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from rest_framework import status
#
# from .models import CustomUser, Building, Sensor, SensorReading, DilutionAction
# from .serializers import (
#     CustomUserSerializer,
#     BuildingSerializer,
#     SensorSerializer,
#     SensorReadingSerializer,
#     DilutionActionSerializer
# )
#
# class CustomUserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     permission_classes = [IsAuthenticated]
#
# class BuildingViewSet(viewsets.ModelViewSet):
#     queryset = Building.objects.all()
#     serializer_class = BuildingSerializer
#     permission_classes = [IsAuthenticated]
#
# class SensorViewSet(viewsets.ModelViewSet):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer
#     permission_classes = [IsAuthenticated]
#
# class SensorReadingViewSet(viewsets.ModelViewSet):
#     queryset = SensorReading.objects.all()
#     serializer_class = SensorReadingSerializer
#     permission_classes = [IsAuthenticated]
#
#     # For ESP32 to push gas alert readings
#     @action(detail=False, methods=['post'], permission_classes=[])
#     def alert(self, request):
#         """
#         ESP32 sends POST data to /api/readings/alert/
#         Example Payload:
#         {
#             "gas_value": 567,
#             "device_id": "ESP32_WROVER_001"
#         }
#         """
#         gas_value = request.data.get("gas_value")
#         device_id = request.data.get("device_id")
#
#         if gas_value is None or device_id is None:
#             return Response({"error": "Missing data"}, status=status.HTTP_400_BAD_REQUEST)
#
#         try:
#             sensor = Sensor.objects.get(sensor_location=device_id)
#         except Sensor.DoesNotExist:
#             return Response({"error": "Sensor not found"}, status=status.HTTP_404_NOT_FOUND)
#
#         reading = SensorReading.objects.create(
#             sensor=sensor,
#             gas_value=gas_value
#         )
#         return Response({
#             "message": "Gas reading stored",
#             "id": reading.id,
#             "value": reading.gas_value
#         }, status=status.HTTP_201_CREATED)
#
# class DilutionActionViewSet(viewsets.ModelViewSet):
#     queryset = DilutionAction.objects.all()
#     serializer_class = DilutionActionSerializer
#     permission_classes = [IsAuthenticated]
import json

from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from config import settings


@csrf_exempt
def gas_alert(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            gas_value = data.get('gas_value')
            status = data.get('status')

            # Print to console
            print(f"🚨 GAS ALERT 🚨 | Value: {gas_value} | Status: {status}")

            # Send email alert
            send_mail(
                subject='🚨 GAS LEAK DETECTED!',
                message=f'Alert from Gas Detection System\n\nGas Value: {gas_value}\nStatus: {status}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['prasanths1807@gmail.com'],  # Replace with your email
                fail_silently=True,
            )

            return JsonResponse({"message": "Data received and email sent."}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Only POST method allowed"}, status=405)
