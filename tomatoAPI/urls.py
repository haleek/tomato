from django.urls import path
from tomatoAPI import views

urlpatterns = [
    
    path('predict/', views.predict.as_view())
]