from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django.utils.translation import ugettext_lazy as _



@python_2_unicode_compatible
class GroupFeed(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    post = models.TextField(max_length=255)
    # parent = models.ForeignKey('Feed', null=True, blank=True)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    class Meta:
        verbose_name = _('Group Feed')
        verbose_name_plural = _('Group Feeds')
        ordering = ('-date',)

    def __str__(self):
        return self.post
