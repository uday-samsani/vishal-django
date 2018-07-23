from django.db import models

from django.core.validators import RegexValidator

from django.core.validators import RegexValidator
experience_choice=(
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('+6','+6'),
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
    email_regex = RegexValidator(regex=r'^\w+@[a-zA-Z_.]+?\.[a-zA-Z]{2,6}')
    phn_regex=RegexValidator(regex=r'^[0-9]{10}')
    regno_regex=RegexValidator(regex=r'^[0-9A-Z-]+')
    linkin_regex=RegexValidator(regex=r'^\w+://+www.linkedin.com+')
    git_regex=RegexValidator(regex=r'\w+://github.com+')
    name = models.CharField(max_length=20)
    reg_no = models.CharField(max_length=11,validators=[regno_regex])
    mail_id = models.CharField(max_length=35,validators=[email_regex])
    degree = models.CharField(max_length=12,choices=degree_choice)
    department = models.CharField(max_length=12,choices=dept_choice)
    company= models.CharField(max_length=12)
    experience = models.CharField(max_length=2,choices=experience_choice)
    location = models.CharField(max_length=15)
    linkedin = models.CharField(max_length=50,validators=[linkin_regex])
    github = models.CharField(max_length=50,validators=[git_regex])
    working_as = models.CharField(max_length=20)
    phn_no = models.CharField(validators=[phn_regex],max_length=10, default=0)
    description = models.TextField(max_length=120,null=True, blank=True)
    passed_out = models.PositiveIntegerField(default=2012)
    def __str__(self):
        return "name : {},registration number : {}".format(self.name,self.reg_no)