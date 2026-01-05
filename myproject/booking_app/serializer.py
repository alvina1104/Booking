from .models import (UserProfile,Country,City,Service,Hotel,HotelImage,
                     Room,RoomImage,Booking,Review)
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
        class Meta:
            model = Country
            fields = '__all__'

class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id','city_name','city_image']

class HotelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id','hotel_name','country','hotel_stars']

class CityDetailSerializer(serializers.ModelSerializer):
    city_hotels = HotelListSerializer(many=True,read_only=True)
    class Meta:
        model = City
        fields = ['id','city_name','city_hotels']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class HotelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name','country','city','hotel_stars','street','postal_code','description','service']


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'