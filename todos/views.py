from .models import Todo
from rest_framework import viewsets
# from rest_framework import permissions
from .serializers import TodoSerializer
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication 


# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Todo.objects.all()
    # The serializer class for serializing output
    serializer_class = TodoSerializer
    # optional permission class set permission level
    permission_classes = [permissions.IsAuthenticated] #Coule be [permissions.IsAuthenticated]
    authentication_classes = (JWTAuthentication,)

