from django.contrib import admin
from .models import Vehicle

# Register your models here.
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id','brand','arrival_location','applicant','create_at')
    search_fields = ('brand','arrival_location','applicant')
    list_filter= ('arrival_location','brand')