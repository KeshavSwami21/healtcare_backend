from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import (
    RegisterView,
    PatientListCreateView,
    PatientDetailView,
    DoctorListCreateView,
    DoctorDetailView,
    AppointmentListCreateView,
    AppointmentDetailView
)


urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'), # This endpoint handles user registration
    path('auth/login/', TokenObtainPairView.as_view(), name='login'), # This endpoint handles user login and returns JWT tokens for authentication
    
    path('patients/', PatientListCreateView.as_view(), name='patient'), # This endpoint handles listing and creating patients
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'), # This endpoint handles retrieving, updating, and deleting a specific patient
    
    path('doctors/', DoctorListCreateView.as_view(), name='doctor'), # This endpoint handles listing and creating doctors
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'), # This endpoint handles retrieving, updating, and deleting a specific doctor
    
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment'), # This endpoint handles listing and creating appointments
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'), # This endpoint handles retrieving, updating, and deleting a specific appointment
]
