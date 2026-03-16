from django.db import models

# Create your models here.

class Job(models.Model):
    api_id = models.IntegerField(unique=True)

    title = models.CharField(max_length=200)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    client_name = models.CharField(max_length=100)
    client_avatar = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
