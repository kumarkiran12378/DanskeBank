from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from user.models import User

class UserSerializer(serializers.Serializer):
    uid = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(User.objects.all())])
    mobile_no = serializers.CharField(required=True, validators=[UniqueValidator(User.objects.all())])
    password = serializers.CharField(required=True, write_only=True)
    status = serializers.IntegerField(required=True)
    islibrarian = serializers.BooleanField(required=True)
    
    class Meta:
        model = User
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)