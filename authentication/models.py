from django.db import models
from django.contrib.auth.models import AbstractUser
from authentication.choices import ROLES # type: ignore

# Create your models here.
class Role(models.Model):
     name = models.CharField(max_length=100, unique=True)
     short_name = models.CharField(max_length=100, choices=ROLES,default="client")
     description = models.CharField(max_length=255)
     is_active = models.BooleanField(default=True)
     
     def __str__(self):
          return self.short_name
     
     class Meta:
          db_table = 'roles'

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    mobile_number = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    created_on = models.DateField(auto_created=True, null=True)
    status = models.IntegerField(default=0)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
         db_table = 'user'

class Services(models.Model):
      name  = models.CharField(max_length=255)
      category = models.CharField(max_length=255)

      def __str__(self):
           return self.name

      class Meta:
           db_table = 'services'

class ServiceProvider(models.Model):
      name = models.CharField(max_length=255)
      image = models.ImageField(upload_to="service_provider")
      contact = models.CharField(max_length=255)
      rating = models.IntegerField()
      total_reviews = models.IntegerField()
      service = models.ForeignKey(Services, on_delete=models.CASCADE)
      
      class Meta:
           db_table = 'service_provider'
class Reviews(models.Model):
      provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
      message = models.TextField()

      class Meta:
          db_table = 'reviews'
