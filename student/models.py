from django.db import models

from django.core.validators import RegexValidator



courses_choice = (
    ('Bachelor Of Technology','Bachelor Of Technology'),
    ('Master Of Technology','Master Of Technology'),
    ('Master Of Buisiness Administration','Master Of Buisiness Administration'),
)

stream_choice = (
    ('IT','IT'),
    ('ECE','ECE'),
    ('CIVIL','CIVIL'),
    ('EEE','EEE'),
    ('MECH','MECH'),
    ('CSE','CSE'),
)
# Create your models here.
class StudentInfo(models.Model):
    email_regex = RegexValidator(regex=r'^[a-z0-9\.\_]+@[a-z_]+?\.[a-zA-Z]{2,6}')
    phn_regex = RegexValidator(regex=r'^[0-9]{10}')
    regno_regex = RegexValidator(regex=r'^[0-9A-Z]')
    linkedIn_regex = RegexValidator(regex=r'^\w+://+www.linkedin.com+')
    git_regex = RegexValidator(regex=r'\w+://github.com+')
    pw_regex = RegexValidator(regex=r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%]).{6,20}')
    name=models.CharField(max_length=32)
    reg_no=models.CharField(max_length=10,validators=[regno_regex])
    course=models.CharField(max_length=32,choices=courses_choice,null=True)
    stream=models.CharField(max_length=16,choices=stream_choice,null=True)
    year=models.PositiveIntegerField(default=1)
    phn_no=models.PositiveIntegerField(validators=[phn_regex])
    git_hub=models.CharField(max_length=64,validators=[git_regex])
    linkedIn=models.CharField(max_length=64,validators=[linkedIn_regex])
    email=models.CharField(max_length=32,validators=[email_regex],default="abc@gmail.com")
    description=models.TextField(max_length=1024)
    usrname=models.CharField(max_length=16)
    pswd=models.CharField(max_length=16,validators=[pw_regex])