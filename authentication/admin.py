from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Services)
admin.site.register(ServiceProvider)
admin.site.register(Reviews)
