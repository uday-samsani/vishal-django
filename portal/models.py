from django.db import models


class AlumniInfo(models.Model):
    name = models.CharField(max_length = 32)
    reg_no = models.CharField(max_length = 8)
    mail_id = models.CharField(max_length = 16)
    degree = models.CharField(max_length = 16)
    department = models.CharField(max_length=32)
    company= models.CharField(max_length=64)
    experience = models.IntegerField(max_length=2)
    location = models.CharField(max_length=16)
    linkedin = models.CharField(max_length=16)
    github = models.CharField(max_length=16)
    working_as = models.CharField(max_length=16)
    description = models.TextField(null=True, blank=True)

