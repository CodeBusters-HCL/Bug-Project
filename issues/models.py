from django.db import models
from datetime import datetime
import uuid
# from django.contrib.auth.models import User         #uncomment this and commentout below line if inbuilt user is needed
from accounts.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Issue(models.Model):


    class Level(models.TextChoices):
        HIGH = 'HIGH', _('High')
        MEDIUM = 'MEDIUM', _('MEDIUM')
        LOW = 'LOW', _('LOW')

    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', _('Active')
        INACTIVE = 'INACTIVE', _('Inactive')
        INVALID = 'INVALID', _('Invalid')

    issue_title = models.CharField(max_length=200)
    issue_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #issue_id = models.IntegerField(primary_key=True)
    issued_on =models.DateTimeField(default=datetime.now)
    issuer_username = models.CharField(max_length=200,  blank=True)
    issuer_email = models.EmailField(max_length=200, blank=True)
    project_type = models.CharField(max_length=200, blank=True)
    priority = models.CharField(max_length=20,choices=Level.choices,default=Level.LOW ,blank=True)
    deadline = models.DateField(blank=True)
    severity = models.CharField(max_length=20,choices=Level.choices,default=Level.LOW ,blank=True)
    description = models.TextField(blank=True)
    issue_file = models.FileField(upload_to='issues_file/%Y/%m/%d/', blank=True)
    issue_status = models.CharField(max_length=20,default=Status.ACTIVE, choices=Status.choices)
    assigned_to_email = models.EmailField( blank=True)
    assigned_to_username = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    assigned_on = models.DateTimeField(blank =True, null=True)
    admin_comment = models.TextField(blank=True)

    def __str__(self):
        self.issue_title


class Comment(models.Model):
    issue = models.ForeignKey(Issue,on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    content = models.TextField(max_length=200, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.issue.issue_id,str(self.user.username))


# def Profile(models.Model):
#     name = models.CharField(max_length=50)
#     picture = models.ImageField(upload_to = 'pictures')

#     class Meta:
#         db_table = "profile"



