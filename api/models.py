from django.db import models
from django.contrib.auth.models import User


# ------------------Patient Models Starts------------------
class Patient(models.Model): # This model represents a patient in the healthcare system.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients') # Establishes a one-to-many relationship with the User model.
    name = models.CharField(max_length=100) # Stores the name of the patient.
    age = models.IntegerField() # Stores the age of the patient.
    medical_history = models.TextField() # Stores the medical history of the patient.
    
    def __str__(self): # This method returns a string representation of the Patient object, which is the patient's name.
        return self.name # This is useful for displaying the patient's name in the admin interface or other parts of the application.
# ------------------Patient Models Ends------------------

# ------------------Doctor Models Starts------------------
class Doctor(models.Model): # This model represents a doctor in the healthcare system.
    name = models.CharField(max_length=100) # Stores the name of the doctor.
    specialization = models.CharField(max_length=100) # Stores the specialization of the doctor.
    contact_info = models.CharField(max_length=100) # Stores the contact information of the doctor.
    
    def __str__(self): # This method returns a string representation of the Doctor object, which is the doctor's name.
        return self.name # This is useful for displaying the doctor's name in the admin interface or other parts of the application.
# ------------------Doctor Models Ends------------------

# ------------------Appointment Models Starts------------------
class Appointment(models.Model): # This model represents an appointment in the healthcare system.
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE) # Establishes a one-to-many relationship with the Patient model.
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE) # Establishes a one-to-many relationship with the Doctor model.
    
    def __str__(self): # This method returns a string representation of the Appointment object, which includes the patient's name and doctor's name.
        return f"{self.patient.name} - {self.doctor.name}" # This is useful for displaying appointment details in the admin interface or other parts of the application.
# ------------------Appointment Models Ends------------------