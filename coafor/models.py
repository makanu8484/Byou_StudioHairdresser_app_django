from django.db import models



class Coafor(models.Model):

    full_name = models.CharField(max_length=40)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    notes = models.TextField(max_length=400)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
