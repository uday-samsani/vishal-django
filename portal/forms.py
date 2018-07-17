from django import forms
from .models import AlumniInfo


class AlumniInfoForm(forms.ModelForm):
    class Meta:
        model=AlumniInfo
        fields=('name','reg_no',
                'mail_id',
                'degree',
                'department',
                'company',
                'experience',
                'location','linkedin','github','working_as',
                'phn_no',
                'description','passed_out',
        )