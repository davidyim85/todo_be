from .models import Todo
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TodoSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication 


# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Todo.objects.all()
    # The serializer class for serializing output
    serializer_class = TodoSerializer
    # optional permission class set permission level
    permission_classes = [AllowAny]
    # authentication_classes = (JWTAuthentication,)



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
