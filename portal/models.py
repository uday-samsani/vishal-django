from django.db import models
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
    name = models.CharField(max_length=32)
    reg_no = models.CharField(max_length=16)
    mail_id = models.CharField(max_length=32)
    degree = models.CharField(max_length=16,choices=degree_choice)
    department = models.CharField(max_length=32,choices=dept_choice)
    company= models.CharField(max_length=64)
    experience = models.CharField(max_length=2,choices=experience_choice)
    location = models.CharField(max_length=16)
    linkedin = models.CharField(max_length=16)
    github = models.CharField(max_length=16)
    working_as = models.CharField(max_length=16)
    phn_no = models.CharField(max_length=16, default=0)
    description = models.TextField(null=True, blank=True)
    passed_out = models.PositiveIntegerField(default=2012)

    def __str__(self):
        return "name- {},company- {}".format(self.name,self.company)