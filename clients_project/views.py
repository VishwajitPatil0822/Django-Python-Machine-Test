from .models import Client,Project
from .serializers import ClientSerializer,ProjectSerializer,ProjectSerializerUpdate,ClientSerializerUpdate,ClientSerializerUpdateFetchById
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ClientList_APIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class ClientDetail_APIView(APIView):
    permission_classes = [IsAuthenticated]
        
    def get(self,request,pk):
            
        try:
            clients = Client.objects.get(pk=pk)
                
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        serializer = ClientSerializerUpdate(clients)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def put(self, request,pk):
        try:
            clients = Client.objects.get(pk=pk)
                    
        except Client.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
                
        serializer = ClientSerializerUpdateFetchById(clients, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
                
    def delete(self, request,pk):
        try:
            clients = Client.objects.get(pk=pk)
                    
        except Client.DoesNotExist:
            return Response( status=status.HTTP_404_NOT_FOUND)
                
        clients.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
            
class ProjectList_APIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ProjectSerializerUpdate(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    
    
class ProjectDetail_APIView(APIView):
    permission_classes = [IsAuthenticated]
        
    def get(self,request,pk):
            
        try:
            project = Project.objects.get(pk=pk)
                
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        serializer = ProjectSerializerUpdate(project)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def put(self, request,pk):
        try:
            project = Project.objects.get(pk=pk)
                    
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
                
        serializer = ProjectSerializerUpdate(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
                
    def delete(self, request,pk):
        try:
            project = Project.objects.get(pk=pk)
                    
        except Project.DoesNotExist:
            return Response( status=status.HTTP_404_NOT_FOUND)
                
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            