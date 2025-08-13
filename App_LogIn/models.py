from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/')
    
    def __str__(self):
        return f"Avatar de {self.user.username} - {self.image.name}"
    

# Create your models here.
