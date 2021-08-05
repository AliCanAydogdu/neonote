from django.db import models
from datetime import datetime
from django.contrib.auth.models import Permission, User


class Group(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=200)

    def __str__(self):
         return str(self.group_name)

class Places(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    place_name = models.CharField(max_length=200)

    address = models.CharField(max_length=200)

    rate_choices = (('5','5'),('4','4'),('3','3'),('2','2'),('1','1'))
    rate = models.CharField(max_length=2,choices=rate_choices, default='5')

    date_added = models.DateTimeField('date published')

    img = models.ImageField(upload_to='place_images', blank=True)

    note = models.CharField(max_length=1000, blank=True)

    def __str__(self):
         return str(self.place_name)+ ', ' + str(self.user)
