from .models import Client,Project
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='username')
    
    class Meta:
        model = User
        fields = ['id','name']


class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = Client
        fields = ['id','client_name','created_at','created_by']


class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = Project
        fields = ['id','project_name','created_at','created_by']
        

class ProjectSerializerUpdate(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    client = serializers.CharField(read_only=True)    
    user = UserSerializer(many = True, read_only = True)

    class Meta:
        model = Project
        fields = ['id','project_name','client','user','created_at','created_by']
        
        
class ClientSerializerUpdate(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    projects = ProjectSerializer(many = True, read_only = True)
    
    class Meta:
        model = Client
        fields = ['id','client_name','projects','created_at','created_by','updated_at']


class ClientSerializerUpdateFetchById(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    
    class Meta:
        model = Client
        fields = ['id','client_name','created_at','created_by','updated_at']        