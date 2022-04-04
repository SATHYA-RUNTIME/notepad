from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from logapp import models as  md

# Register your models here.
class adminreg(admin.ModelAdmin):
    list=['username','mobileno','age','gender','mail','nikename','pwd']
    
    
admin.site.register(md.register,adminreg)

admin.site.register(md.data)