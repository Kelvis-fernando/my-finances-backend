from django.db import models

class Wage(models.Model):
    wage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.wage
    
class Spending(models.Model):
    title = models.TextField(max_length=60)
    description = models.TextField(max_length=160)
    amount = models.BooleanField()
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
