from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
#from django.shortcuts import get_object_or_404



class User_Bio(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOISE = (
        (MALE, 'Male'),
        (FEMALE, 'Female')    
    )


    register = models.ForeignKey(User)
    name = models.CharField(max_length=50, unique=True)
    age = models.PositiveIntegerField(default = 0)
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOISE,
                              default=FEMALE)
    date_join = models.DateTimeField('date joined')
    facebook_id = models.CharField(blank=True, null=True, default=None, max_length=255)

    def __str__(self):
        return self.name

class Wall(models.Model):
    user = models.ForeignKey(User_Bio)
    #status = models.CharField(max_length=500)
    #pub_date = models.DateTimeField('date published')

class Post(models.Model):
    wall = models.ForeignKey(Wall)
    poster = models.ForeignKey(User_Bio)
    status = models.CharField(max_length=500)
    pub_date = models.DateTimeField('datepublished')

    def __str__(self):
        return self.status

class Sub_Post(models.Model):
    wall = models.ForeignKey(Wall)
    parent_post = models.ForeignKey(Post)
    poster = models.ForeignKey(User_Bio)
    status = models.CharField(max_length=500)
    pub_date = models.DateTimeField('datepublished', blank=True)

    def __str__(self):
        return self.status

class Pics(models.Model):
    user = models.ForeignKey(User_Bio)
    #photo = models.ImageField()
    photo = models.ImageField(default='welcome.jpg')
    is_profile_pic = models.BooleanField(default=True)