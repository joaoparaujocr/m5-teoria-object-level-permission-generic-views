from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from users.serializers import ComputerSerializer

from .models import Computer
from .permissions import isComputerOwner


# Create your views here.
class RetrieveComputerView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, isComputerOwner]

    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
