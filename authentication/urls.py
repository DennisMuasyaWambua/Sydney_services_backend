from django.urls import path
from .views import *

urlpatterns = [
    path("login/", LoginView.as_view(), name='login'),
    path("register/", RegisterView.as_view(), name='register'),
    path("services/", CreateServiceView.as_view(), name='create-service'),
    path("service-provider/", CreateServiceProvider.as_view(), name='service-provider')
]   