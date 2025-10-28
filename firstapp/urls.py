from django.urls import path
from .views import RoombookingListCreateView, HomeView ,RoombookingDetail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/bookings/', RoombookingListCreateView.as_view(), name='bookings'),
    path("api/bookings/<int:pk>/", RoombookingDetail.as_view(), name="booking-detail"),  # ✅ fixed path

]
