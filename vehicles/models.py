from django.db import models

# Create your models here.

class Vehicle(models.Model):
    brand = models.CharField(max_length=100) 
    arrival_location = models.CharField(max_length=100)
    applicant = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.brand} - {self.arrival_location} - {self.applicant}' 
