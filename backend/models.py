from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User Model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']

    def __str__(self):
        return self.email


# Represents a physical building under monitoring
class Building(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.location}"

    class Meta:
        db_table = "buildings"


# Represents a sensor installed in a specific location of a building
class Sensor(models.Model):

    id = models.BigAutoField(primary_key=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='sensors')
    sensor_id = models.CharField(max_length=50, unique=True)
    location_description = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.sensor_id}  at {self.location_description}"

    class Meta:
        db_table = "sensors"


# Represents real-time or historical data captured from a sensor
class SensorReading(models.Model):
    id = models.BigAutoField(primary_key=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='readings')
    timestamp = models.DateTimeField(auto_now_add=True)
    gas_level_ppm = models.FloatField(help_text="Gas concentration in PPM")
    temperature_c = models.FloatField(null=True, blank=True)
    humidity_percent = models.FloatField(null=True, blank=True)
    is_dangerous = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sensor.sensor_id} - {self.timestamp} - {self.gas_level_ppm} ppm"

    class Meta:
        db_table = "sensor_readings"
        ordering = ['-timestamp']


# Represents automated or manual dilution action taken
class DilutionAction(models.Model):
    ACTION_TYPE_CHOICES = [
        ('AUTO', 'Automated'),
        ('MANUAL', 'Manual'),
    ]

    id = models.BigAutoField(primary_key=True)
    sensor_reading = models.OneToOneField(SensorReading, on_delete=models.CASCADE)
    action_taken = models.TextField()
    action_type = models.CharField(max_length=10, choices=ACTION_TYPE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    triggered_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Dilution @ {self.timestamp} ({self.action_type})"

    class Meta:
        db_table = "dilution_actions"
