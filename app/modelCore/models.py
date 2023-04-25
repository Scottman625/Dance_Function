from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.urls import reverse
from django.utils import timezone
import pathlib
import uuid


def image_upload_handler(instance,filename):
    fpath = pathlib.Path(filename)
    new_fname = str(uuid.uuid1()) #uuid1 -> uuid + timestamp
    return f'images/{new_fname}{fpath.suffix}'

@property
def get_photo_url(self):
    if self.photo and hasattr(self.photo, 'url'):
        return self.photo.url
    else:
        return "/static/web/assets/img/generic/2.jpg"

class UserManager(BaseUserManager):
    
    def create_user(self, phone, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not phone:
            raise ValueError('Users must have an phone')
        # user = self.model(email=self.normalize_email(email), **extra_fields)
        user = self.model(
            phone = phone, 
            name=extra_fields.get('name'),
            line_id=extra_fields.get('line_id'),
            apple_id =extra_fields.get('apple_id'),
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone, password, **extra_fields):
        """Creates and saves a new super user"""
        user = self.create_user(phone, password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=10, unique=True)
    objects = UserManager()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    name = models.CharField(max_length=255,null=True,blank=True)

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default=MALE)

    email = models.CharField(max_length= 100, blank = True, null=True)
    address = models.CharField(max_length= 100, blank = True, null=True)
    image = models.ImageField(upload_to=image_upload_handler, blank=True, null=True)

    line_id = models.CharField(max_length= 100, blank = True, null=True, unique=True)
    apple_id = models.CharField(max_length= 100, blank = True, null=True, unique=True)


    background_image = models.ImageField(upload_to=image_upload_handler, blank=True, null=True)

    ATMInfoBankCode = models.CharField(max_length=20, default='', blank = True, null=True)
    ATMInfoBranchBankCode = models.CharField(max_length=20, default='', blank = True, null=True)
    ATMInfoAccount = models.CharField(max_length=20, default='', blank = True, null=True)

    USERNAME_FIELD = 'phone'




class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='')
    upload_date = models.DateTimeField(default=timezone.now)
    video_file = models.FileField(upload_to='videos/')
    data = models.JSONField(null=True,blank=True)
    total_score = models.IntegerField(null=True,blank=True)

class GameScore(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        null=True
    )
    video = models.ForeignKey(
        Video,
        on_delete = models.SET_NULL,
        null=True
    )
    score = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    @property
    def rating(self):
        score_perc = float(self.score/self.video.total_score)
        if score_perc > 1:
            return 'AAA'
        elif score_perc > 0.85:
            return 'AA'
        elif score_perc > 0.65:
            return 'A'
        elif score_perc > 0.4:
            return 'B'
        elif score_perc > 0.3:
            return 'C'
        elif score_perc > 0.2:
            return 'D'
        else:
            return 'E'