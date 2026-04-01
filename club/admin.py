from django.contrib import admin

# Register your models here.
from django.shortcuts import*

from .models import *

admin.site.register(Club)
admin.site.register(arsenal)
admin.site.register(ClubMember)