from django.db.models import DateTimeField

from .models import (UserProfile,Country,City,Service,Hotel,HotelImage,
                     Room,RoomImage,Booking,Review)
from rest_framework import serializers


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class CountryProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_image', 'country_name']

class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','first_name','last_name','user_image','role']


class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileReviewSerializer(serializers.ModelSerializer):
    country = CountryProfileSerializer()
    class Meta:
        model = UserProfile
        fields = ['first_name','user_image','country']


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id','city_name','city_image']

class CityHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name']

class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ["hotel_image"]

class HotelListSerializer(serializers.ModelSerializer):
    city = CityHotelSerializer()
    hotel_photos = HotelImageSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['id','hotel_name','hotel_photos','city','hotel_stars','description']

class HotelCreateSerializer(serializers.ModelSerializer):
     class Meta:
         model = Hotel
         fields = '__all__'


class CityDetailSerializer(serializers.ModelSerializer):
    city_hotels = HotelListSerializer(many=True,read_only=True)
    class Meta:
        model = City
        fields = ['id','city_name','city_hotels']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['service_image','service_name']

class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','room_number','room_type','room_status']

class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image']

class RoomDetailSerializer(serializers.ModelSerializer):
    room_photos = RoomImageSerializer(many=True,read_only=True)
    class Meta:
        model = Room
        fields = ['id','room_number','room_photos','price','room_type','room_status',
                  'description']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = UserProfileReviewSerializer()
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))

    class Meta:
        model = Review
        fields = ['user','text','created_date']

class HotelDetailSerializer(serializers.ModelSerializer):
    country =CountrySerializer()
    city = CityHotelSerializer()
    hotel_photos = HotelImageSerializer(many=True, read_only=True)
    service = ServiceSerializer(many=True)
    hotel_rooms = RoomListSerializer(many=True, read_only=True)
    hotel_reviews = ReviewSerializer(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_person = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['hotel_name','country','city','hotel_stars','street','postal_code',
                  'hotel_photos','description','service','hotel_rooms','get_avg_rating',
                  'get_count_person','hotel_reviews',]

    def get_avg_rating(self,obj):
        return obj.get_avg_rating()

    def get_count_person(self, obj):
        return obj.get_count_person()

