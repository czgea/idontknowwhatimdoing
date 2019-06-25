from rest_framework import serializers
from app.models import Area, Feedback, Location, Show

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('name')


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('customer_first_name', 'customer_last_name', 'email', 'area', 'details', 'followup', 'date')


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = ('showName', 'showLocation', 'showTime', 'showMessage', 'showLong', 'showLat')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'icon', 'long', 'lat')





