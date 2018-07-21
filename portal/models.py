from django.db import models

from django.core.validators import RegexValidator

from django.core.validators import RegexValidator
experience_choice=(
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('>5','>5'),
)
degree_choice = (
    ('B.TECH','B.TECH'),
    ('M.TECH','M.TECH'),
    ('MBA','MBA'),
)
dept_choice = (
    ('IT','IT'),
    ('ECE','ECE'),
    ('CIVIL','CIVIL'),
    ('EEE','EEE'),
    ('MECH','MECH'),
    ('CSE','CSE'),
)



class AlumniInfo(models.Model):
    email_regex = RegexValidator(regex=r'^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6}')
    name = models.CharField(max_length=12)
    reg_no = models.CharField(max_length=12)
    mail_id = models.CharField(max_length=36,validators=[email_regex])
    degree = models.CharField(max_length=12,choices=degree_choice)
    department = models.CharField(max_length=12,choices=dept_choice)
    company= models.CharField(max_length=12)
    experience = models.CharField(max_length=2,choices=experience_choice)
    location = models.CharField(max_length=12)
    linkedin = models.CharField(max_length=12)
    github = models.CharField(max_length=12)
    working_as = models.CharField(max_length=12)
    phn_no = models.CharField(max_length=10, default=0)
    description = models.TextField(null=True, blank=True)
    passed_out = models.PositiveIntegerField(default=2012)
    def __str__(self):
        return "name- {},company- {}".format(self.name,self.company)