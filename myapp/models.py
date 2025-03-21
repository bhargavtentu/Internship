from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import RegexValidator


def validate_indian_phone(value):
    if not re.match(r'^[6-9]\d{9}$', value):  # Indian numbers start with 6,7,8,9 and have 10 digits
        raise ValidationError("Enter a valid 10-digit Indian mobile number.")

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='media/profile-pics/', blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True, validators=[validate_indian_phone])


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    postname = models.CharField(max_length=600)
    category = models.CharField(max_length=600)
    image = models.ImageField(upload_to='images/posts/', blank=True, null=True)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.postname)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}. {self.content[:20]}..."


class Contact(models.Model):
    name = models.CharField(max_length=600)
    email = models.EmailField(max_length=600)
    subject = models.CharField(max_length=1000)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
