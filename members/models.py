from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

class User(AbstractUser):
    pass

class Measurements(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="athletemeasurements")
    head = models.IntegerField(default=0)
    neck = models.IntegerField(default=0)
    inside_leg = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    shoe = models.IntegerField(default=0)
    chest = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user}'s measurements"
    
class Media(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="athletepictures")
    photo1 = models.ImageField(upload_to='images')
    photo2 = models.ImageField(upload_to='images')
    photo3 = models.ImageField(upload_to='images')
    video = models.FileField(upload_to='videos_uploaded',null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])

    def __str__(self):
        return f"{self.user}'s media"