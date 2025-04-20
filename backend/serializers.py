# from django.contrib.auth import get_user_model
# from rest_framework import serializers
# from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
# from .models import *
# User = get_user_model()
#
# class UserCreateSerializer(BaseUserCreateSerializer):
#     email = serializers.EmailField(required=True)
#
#     class Meta(BaseUserCreateSerializer.Meta):
#         model = User
#         fields = "__all__"
#         # fields = ('id', 'username', 'email', 'password')
#
#     def validate_email(self, value):
#         if User.objects.filter(email=value).exists():
#             raise serializers.ValidationError("A user with this email already exists.")
#         return value
#
#     def create(self, validated_data):
#         user = super().create(validated_data)
#         user.is_staff = True  # Assign staff access by default
#         user.save()
#         return user
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"
#         # fields = ('id', 'username', 'email')
#
# class BuildingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Building
#         fields = ['id', 'name', 'location', 'address']
#
#
#
# class SensorSerializer(serializers.ModelSerializer):
#     building = BuildingSerializer(read_only=True)
#     building_id = serializers.PrimaryKeyRelatedField(queryset=Building.objects.all(), source='building', write_only=True)
#
#     class Meta:
#         model = Sensor
#         fields = ['id', 'sensor_id', 'sensor_type', 'location_description', 'building', 'building_id']
#
#
# class SensorReadingSerializer(serializers.ModelSerializer):
#     sensor = SensorSerializer(read_only=True)
#     sensor_id = serializers.PrimaryKeyRelatedField(queryset=Sensor.objects.all(), source='sensor', write_only=True)
#
#     class Meta:
#         model = SensorReading
#         fields = ['id', 'timestamp', 'gas_level_ppm', 'temperature_c', 'humidity_percent', 'is_dangerous', 'sensor', 'sensor_id']
#
#
# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'email', 'phone_number']
#
#
# class DilutionActionSerializer(serializers.ModelSerializer):
#     sensor_reading = SensorReadingSerializer(read_only=True)
#     sensor_reading_id = serializers.PrimaryKeyRelatedField(queryset=SensorReading.objects.all(), source='sensor_reading', write_only=True)
#     triggered_by = CustomUserSerializer(read_only=True)
#     triggered_by_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), source='triggered_by', write_only=True, required=False)
#
#     class Meta:
#         model = DilutionAction
#         fields = ['id', 'sensor_reading', 'sensor_reading_id', 'action_taken', 'action_type', 'timestamp', 'triggered_by', 'triggered_by_id']