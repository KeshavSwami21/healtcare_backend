from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import (
    RegisterSerializer,
    PatientSerializer,
    DoctorSerializer,
    AppointmentSerializer
)
from .models import Patient, Doctor, Appointment




#--------------------Register View Starts--------------------


class RegisterView(generics.CreateAPIView): # This view handles user registration
    queryset = User.objects.all() # It retrieves all User objects from the database
    serializer_class = RegisterSerializer # It uses the RegisterSerializer to validate and save the user data


#--------------------Register View Ends-----------------------

#--------------------Patient Starts--------------------


class PatientListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer # This view handles listing and creating patients
    permission_classes = [permissions.IsAuthenticated] # Only authenticated users can access this view
    
    def get_queryset(self): # This method filters the patients to only those associated with the authenticated user
        return Patient.objects.filter(user=self.request.user) # It retrieves all Patient objects where the user matches the authenticated user
    
    def perform_create(self, serializer): # This method is called when a new patient is created
        serializer.save(user=self.request.user) # It saves the patient with the authenticated user as the owner



class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer # This view handles retrieving, updating, and deleting a specific patient
    permission_classes = [permissions.IsAuthenticated] # Only authenticated users can access this view
    
    def get_queryset(self): # This method filters the patients to only those associated with the authenticated user
        return Patient.objects.filter(user=self.request.user) # It retrieves all Patient objects where the user matches the authenticated user


#--------------------Patient Ends-----------------------

#--------------------Doctor Starts--------------------


class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all() # This view handles listing and creating doctors
    serializer_class = DoctorSerializer # It uses the DoctorSerializer to validate and save the doctor data
    permission_classes = [permissions.IsAuthenticated] # Only authenticated users can access this view

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all() # This view handles retrieving, updating, and deleting a specific doctor
    serializer_class = DoctorSerializer # It uses the DoctorSerializer to validate and save the doctor data
    permission_classes = [permissions.IsAuthenticated] # Only authenticated users can access this view


#--------------------Doctor Ends-----------------------

#--------------------Appointment Starts--------------------

class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all() # This view handles listing and creating appointments
    serializer_class = AppointmentSerializer # It uses the AppointmentSerializer to validate and save the appointment data
    permission_classes = [permissions.IsAuthenticated] # Only authenticated users can access this view

class AppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all() # This view handles retrieving, updating, and deleting a specific appointment
    serializer_class = AppointmentSerializer # It uses the AppointmentSerializer to validate and save the appointment data
    permission_classes = [permissions.IsAuthenticated] # Only authenticated users can access this view


#--------------------Appointment Ends-----------------------