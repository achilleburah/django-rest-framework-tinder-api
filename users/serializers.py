from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.gis.db.models.functions import GeometryDistance

from users.models import CustomUser, MatchedUser, MatchRequest



class CustomUserSerializer(serializers.ModelSerializer):

	class Meta:
		model = CustomUser
		fields = '__all__'
		ordering = ['email']

	def create(self, validated_data):
		return CustomUser.objects.create_user(**validated_data)


class CustomRegisterUserSerializer(serializers.ModelSerializer):

	#password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
	password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
	password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = CustomUser
		fields = ['email', 'first_name', 'last_name', 'genre', 'bio', 'password', 'password2']
		ordering = ['email']

		extra_kwargs = {
			'password': {'style': {'input_type': 'password'}, 'required': True, 'write_only': True},

		}

	def create(self, validated_data):
		if self.validated_data['password'] == self.validated_data['password2']:
			data = validated_data.pop('password2')
			return CustomUser.objects.create_user(**validated_data)
		else:
			raise serializers.ValidationError("Password not identical")





class UserInfoSerializer(serializers.ModelSerializer):

	# distance = serializers.SerializerMethodField(read_only=True)
	distance = serializers.FloatField(default=0)


	class Meta:
		model = CustomUser
		fields = ['first_name', 'last_name', 'genre', 'picture', 'location', 'distance']






class MatchRequestSerializer(serializers.ModelSerializer):

	class Meta:
		model = MatchRequest
		fields = ['sender', 'receiver']
		unique_together = (('sender','receiver'),)

		validators = [
			UniqueTogetherValidator(queryset=MatchRequest.objects.all(), fields=['sender', 'receiver'])
		]


	def validate(self, data):
		sender = data.get('sender')
		receiver = data.get('receiver')
		if sender == receiver:
			raise serializers.ValidationError('Fields are the same')
		else:
			return data


class MatchedUsersSerializer(serializers.ModelSerializer):


	user1_id = serializers.IntegerField(required=True)
	user2_id = serializers.IntegerField(required=True)

	class Meta:
		model = CustomUser
		fields = ['user1_id', 'user2_id', 'first_name', 'last_name', 'email', 'genre', 'bio']












