from rest_framework import serializers
from .models import Movie,Gener
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')
        extra_kwargs = {'password':{'write_only':True}}

    def crate(self,validated_data):
        user = User(
            email=validated_data['email'],
            username = validated_data['username']

        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class GenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gener
        fields = '__all__'


class MovieGenSerializer(serializers.ModelSerializer):
    gener = serializers.StringRelatedField(many=True)
    class Meta:
        model = Movie
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    #gener = serializers.StringRelatedField(many=True)
    class Meta:
        model = Movie
        fields = '__all__'
