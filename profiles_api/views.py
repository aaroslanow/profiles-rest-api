from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIVIEW features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, delete)',
            'is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello','an_apiview': an_apiview})

    def post(self, request):
        """Create Hello message with name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message= f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None):
        """update an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update """
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """delete object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """ test viewset"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """ return a hello message"""
        a_viewset =[
            'uses acttions (list,create,retrieve,update, partial_update)',
            "Automatically maps to URLS using Routers",
            "Preovides more functionality with less code,"
        ]
        return Response({'message': 'Hello','a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello{name}!'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})

    def update(self, request, pk = None):
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk = None):
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk = None):
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
