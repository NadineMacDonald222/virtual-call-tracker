from django.db import models

class CallLog(models.Model):
    caller_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    status_choices = [
        ('missed', 'Missed'),
        ('completed', 'Completed'),
        ('ongoing', 'Ongoing'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='ongoing')
    
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when record is created
    updated_at = models.DateTimeField(auto_now=True)      # Timestamp when record is updated

    def __str__(self):
        return f"{self.caller_name} ({self.phone_number}) - {self.status}"
