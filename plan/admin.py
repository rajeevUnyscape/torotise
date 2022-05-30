from django.contrib import admin

# Register your models here.
from .models import *
# from django.contrib.auth.admin import UserAdmin


admin.site.register(Partner)
admin.site.register(Plans)
admin.site.register(Promotion)
admin.site.register(CustomerGoals)