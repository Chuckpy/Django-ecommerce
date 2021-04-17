from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models
from PIL import Image

class User(AbstractUser):
    bio = models.TextField(blank=True)

    
    def get_absolute_url(self):
        return reverse("/")


def upload_perfil_user(instance, filename):
    return f"profile_photos/user_{instance.id}/{filename}"

class Profile(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="no_image.jpg", upload_to=upload_perfil_user)

    def __str__(self):
        return f'Perfil de { self.user.username }'

    # redimensionando imagem para um maximo de 300x300 px
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width >300 :
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


