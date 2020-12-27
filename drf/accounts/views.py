from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status , viewsets ,views
from  rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly , IsAuthenticated


from . import models
from .serializers import HelloSerializer,UserProfileSerializer , ProfileFeedItemSerializer
from . import permissions


class HelloApiView(views.APIView):

    serializer_class = HelloSerializer

    def get(self, request, format=None):

        an_apiview = [
            'yedidya',
            'moyshi',
            'shelomo',
            'yosi'
        ]

        return Response({'message': 'Hello!', 'an_apiview':an_apiview})

    def post(self, request):

        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f'Hllo {name}'

            return Response({'message' : message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):

        return Response({'method' : 'put'})

    def patch(self, request, pk=None):

        return Response({'method' : 'patch'})

    def delete(self, request, pk=None):

        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):

    serializer_class = HelloSerializer

    def list(self, request, format=None):

        a_viewset = [
            'yedidya',
            'moyshi',
            'shelomo',
            'yosi'
        ]

        return Response({'message': 'Hello!', 'a_viewset':a_viewset})

    def create(self, request):

        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f'Hllo {name}'

            return Response({'message' : message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):

        return Response({'method' : 'get'})

    def update(self, request, pk=None):

        return Response({'method' : 'put'})

    def partial_update(self, request, pk=None):

        return Response({'method' : 'patch'})

    def destory(self, request, pk=None):

        return Response({'method': 'delete'})


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):

    get_serializer = AuthTokenSerializer

    def create(self, request):

        return ObtainAuthToken.post(self, request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):


    serializer_class = ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.PostOwnStatus,IsAuthenticated)

    def perform_create(self, serializer):

        serializer.save(user_profile=self.request.user)



