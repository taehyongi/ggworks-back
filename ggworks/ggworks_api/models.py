from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class UserProfile(models.Model):
  user = models.OneToOneField(User, unique=True, related_name='users', on_delete=models.CASCADE)
  full_name = models.CharField(max_length=100, blank=True)
  nick_name = models.CharField(max_length=50, blank=True)
  email = models.CharField(max_length=50, blank=True)
  photo = models.ImageField(blank=True, upload_to="profile_photo")
  photo_small = models.ImageField(blank=True, upload_to="profile_photo")
  created_date = models.DateTimeField(auto_now_add=True)
  modified_date = models.DateTimeField(auto_now=True)

  # admin 페이지에서 Display 되는 값을 __str__ 로 오버라이드 해줌
  def __str__(self):
    return str(self.user)

# post_save 시그널을 받아 토큰을 생성한다.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
  if created:
    Token.objects.create(user=instance)