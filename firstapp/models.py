from django.db import models

class Roombooking(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    selected_rooms = models.TextField()  # Comma-separated room numbers
    check_in_time = models.TimeField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.selected_rooms}"
