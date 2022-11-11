from authentication.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.modelSerializer):

    password = serializers.CharField(
        max_length = 128, min_length = 6, write_only = True)

    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)