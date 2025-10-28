from django.views import View
from django.http import HttpResponse
from rest_framework import generics
from .models import Roombooking
from .serializers import RoombookingSerializer

class HomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to the Home Page")

class RoombookingListCreateView(generics.ListCreateAPIView):
    queryset = Roombooking.objects.all()
    serializer_class = RoombookingSerializer

class RoombookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roombooking.objects.all()
    serializer_class = RoombookingSerializer
