from django.db import models
from django.conf import settings
# Create your models here.

class Group(models.Model):
    # # #

    # # #

    facebook_id = models.CharField(max_length=200, default ='')

    test_field = models.CharField(max_length=200, default ='')


    name = models.CharField(max_length=255, default ='')

    name_test = models.CharField(max_length=255, default='')

    slug = models.CharField(max_length=255, default ='')

    description = models.TextField(max_length=5000, default='')

    cover = models.CharField(max_length=150, default='')

    administrator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Posts (models.Model):

    group = models.ForeignKey(Group, on_delete = models.CASCADE)

    facebook_id = models.CharField(max_length=100, default='')

    body = models.TextField(max_length=5000,default='')



    def __str__(self):
        return self.facebook_id + self.group.name

class Comments (models.Model):

    post_id = models.ForeignKey(Posts, on_delete = models.CASCADE)

    facebook_id = models.TextField(max_length=100, default='')

    comment = models.TextField(max_length=5000,default='')