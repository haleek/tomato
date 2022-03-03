from django.urls import path
from tomatoAPI import views
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse('its working!'), name='hello_world'),
    path('predict/', views.predict.as_view())
]
