from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from django.contrib.gis.db.models.functions import GeometryDistance

from users.models import CustomUser, MatchedUser, MatchRequest
from users.serializers import CustomUserSerializer, UserInfoSerializer, MatchRequestSerializer, MatchedUsersSerializer, CustomRegisterUserSerializer
from users.filters import UserProposalsFilter



class CustomUserView(generics.CreateAPIView):
    """
    This viewset automatically only provides the Create action.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomRegisterUserSerializer
    permission_classes = (AllowAny,)




class MatchProposalsView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserInfoSerializer
    filter_class = UserProposalsFilter

    def get_queryset(self):
        current_user = self.request.user
        genre = self.request.query_params.get('genre', None)
        radius = self.request.query_params.get('radius', 5)
        queryset = CustomUser.objects.exclude(id=current_user.id, is_staff=True)

        if current_user.location:
          queryset = queryset.annotate(distance = GeometryDistance('location', current_user.location)*100)
          #queryset = queryset.filter(distance<radius)

        if genre is not None:
          queryset = queryset.filter(genre=genre)

        return queryset




class MatchRequestViewSet(viewsets.ModelViewSet):
    queryset = MatchRequest.objects.all()
    serializer_class = MatchRequestSerializer



class MatchedUsersView(generics.ListAPIView):

  queryset = MatchedUser.objects.all()
  serializer_class = MatchedUsersSerializer

  def list(self, request):
    queryset = self.get_queryset()
    serializer = MatchRequestSerializer(list(queryset), many=True)
    return Response(serializer.data)


  def get_queryset(self):
    user_id = self.request.query_params.get('user_id', None)

    queryset = MatchRequest.objects.all()

    if user_id is not None:
      queryset.filter(sender_id=user_id)
      queryset = queryset.raw(
          'SELECT request.id, request.sender_id AS user1_id, request.receiver_id AS user2_id, match.first_name, match.last_name, match.email, match.genre, match.bio FROM users_matchrequest request LEFT JOIN users_matchrequest request2 ON request.receiver_id = request2.sender_id JOIN users_customuser match ON request.receiver_id = match.id WHERE request.sender_id = request2.receiver_id AND request.sender_id < request.receiver_id AND request.sender_id = %s', user_id)
    else:
      queryset = queryset.raw(
          'SELECT request.id, request.sender_id AS user1_id, request.receiver_id AS user2_id, match.first_name, match.last_name, match.email, match.genre, match.bio FROM users_matchrequest request LEFT JOIN users_matchrequest request2 ON request.receiver_id = request2.sender_id JOIN users_customuser match ON request.receiver_id = match.id WHERE request.sender_id = request2.receiver_id AND request.sender_id < request.receiver_id')




    return queryset







