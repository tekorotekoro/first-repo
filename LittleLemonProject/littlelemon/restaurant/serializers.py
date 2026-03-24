from rest_framework import serializers
from restaurant.models import Menu, Booking
from django.contrib.auth.models import User
from django.utils import timezone

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    booking_date = serializers.DateTimeField(required=False)
    class Meta:
        model = Booking
        fields = ["name", "no_of_guests", "booking_date"]

    def validate_booking_date(self, value):
        if not value:
            return timezone.now()   
        if value < timezone.now():
            raise serializers.ValidationError("Booking date cannot be in the past.")    
        return value

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']