from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient, Doctor, Appointment


#--------------------Register Serializer Starts--------------------
class RegisterSerializer(serializers.ModelSerializer):  # This serializer is used for registering a new user (patient).
    password = serializers.CharField(write_only=True)   # The password field is write-only, meaning it won't be included in the serialized output.
    
    class Meta:  # Meta class is used to define the model and fields that this serializer will handle.
        model = User  # The model associated with this serializer is the User model from Django's auth system.
        fields = ['username', 'email', 'password']  # The fields that will be included in the serialized output are username, email, and password.
    
    def create(self, validated_data):  # The create method is overridden to handle the creation of a new user.
        user = User.objects.create_user(  # This method creates a new user instance using the validated data.
            username=validated_data['username'],  # The username is taken from the validated data.
            email=validated_data['email'],  # The email is also taken from the validated data.
            password=validated_data['password']  # The password is taken from the validated data and is hashed automatically by Django's create_user method.
        )
        return user
#--------------------Register Serializer Ends--------------------


#--------------------Patient Serializer Starts--------------------
class PatientSerializer(serializers.ModelSerializer):  # This serializer is used for serializing Patient model instances.
    class Meta:  # Meta class is used to define the model and fields that this serializer will handle.
        model = Patient  # The model associated with this serializer is the Patient model.
        fields = '__all__'  # All fields of the Patient model will be included in the serialized output.
        read_only_fields = ['user']  # The 'user' field is read-only, meaning it won't be included in the serialized input but will be included in the output.
#--------------------Patient Serializer Ends--------------------


#--------------------Doctor Serializer Starts--------------------
class DoctorSerializer(serializers.ModelSerializer):  # This serializer is used for serializing Doctor model instances.
    class Meta:  # Meta class is used to define the model and fields that this serializer will handle.
        model = Doctor  # The model associated with this serializer is the Doctor model.
        fields = '__all__'  # All fields of the Doctor model will be included in the serialized output.
#--------------------Doctor Serializer Ends--------------------


#--------------------Appointment Serializer Starts--------------------
class AppointmentSerializer(serializers.ModelSerializer):  # This serializer is used for serializing Appointment model instances.
    class Meta:  # Meta class is used to define the model and fields that this serializer will handle.
        model = Appointment  # The model associated with this serializer is the Appointment model.
        fields = '__all__'  # All fields of the Appointment model will be included in the serialized output.
#--------------------Appointment Serializer Ends--------------------