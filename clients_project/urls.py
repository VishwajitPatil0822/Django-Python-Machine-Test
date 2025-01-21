from django.urls import path,include
from .views import ClientList_APIView,ClientDetail_APIView,ProjectList_APIView,ProjectDetail_APIView

urlpatterns = [
    path('client/', ClientList_APIView.as_view(), name='ClientList_APIView_urls'),
    path('client/<int:pk>/', ClientDetail_APIView.as_view(), name='ClientDetail_APIView_urls'),
    path('project/', ProjectList_APIView.as_view(), name='ProjectList_APIView_urls'),
    path('project/<int:pk>/', ProjectDetail_APIView.as_view(), name='ProjectDetail_APIView_urls'),
]