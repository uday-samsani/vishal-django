from django.db import models
from django.core.validators import RegexValidator


class AlumniInfo(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    name = models.CharField(max_length=32)
    reg_no = models.CharField(max_length=8)
    mail_id = models.CharField(max_length=16)
    degree = models.CharField(max_length=16)
    department = models.CharField(max_length=32)
    company= models.CharField(max_length=64)
    experience = models.IntegerField(default=0)
    location = models.CharField(max_length=16)
    linkedin = models.CharField(max_length=16)
    github = models.CharField(max_length=16)
    working_as = models.CharField(max_length=16)
    phn_no = models.CharField(validators=[phone_regex],max_length=16, default=0)
    description = models.TextField(null=True, blank=True)
    passed_out = models.IntegerField(default=2015)

    def __str__(self):
        return "name- {},company- {}".format(self.name,self.company)