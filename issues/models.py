from django.db import models
from datetime import datetime
import uuid
from django.contrib.auth.models import User
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
    issued_on =models.DateTimeField(default=datetime.now)
    issuer_username = models.CharField(max_length=200,  blank=True)
    issuer_email = models.EmailField(max_length=200,  blank=True)
    project_type = models.CharField(max_length=200, blank=True)
    priority = models.CharField(max_length=20,choices=Level.choices,default=Level.LOW ,blank=True)
    deadline = models.DateField(blank=True)
    severity = models.CharField(max_length=20,choices=Level.choices,default=Level.LOW ,blank=True)
    description = models.TextField(blank=True)
    issue_file = models.FileField(upload_to='issues_file/%Y/%m/%d/', blank=True)
    issue_status = models.CharField(max_length=20,default=Status.ACTIVE, choices=Status.choices)
    assigned_to_email = models.EmailField( blank=True)
    assigned_to_username = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    assigned_on = models.DateTimeField(blank =True)
    admin_comment = models.TextField(blank=True)

def __str__(self):
    self.issue_title





