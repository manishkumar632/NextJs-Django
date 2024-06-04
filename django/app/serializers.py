from rest_framework import serializers
from .models import App, Subscriber
class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'