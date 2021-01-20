from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.gis.db.models.functions import GeometryDistance

from users.models import CustomUser, MatchedUser, MatchRequest



class CustomUserSerializer(serializers.ModelSerializer):


	class Meta:
		model = CustomUser
		fields = '__all__'


	def create(self, validated_data):
		return CustomUser.objects.create_user(**validated_data)



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

	# def create(self, validated_data):
	# 	request =  MatchRequest.objects.create(**validated_data)


	# 	return request





class MatchRequestSerializer(serializers.ModelSerializer):


	user1_id = serializers.IntegerField(required=True)
	user2_id = serializers.IntegerField(required=True)

	class Meta:
		model = CustomUser
		fields = ['user1_id', 'user2_id', 'first_name', 'last_name', 'email', 'genre', 'bio']












