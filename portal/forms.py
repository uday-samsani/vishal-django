from django import forms
from .models import AlumniInfo


class AlumniInfoForm(forms.ModelForm):
    class Meta:
        model=AlumniInfo
        fields=('name','reg_no',
                'department','degree',
                'passed_out','phn_no',
                'mail_id','company',
                'working_as','experience',
                'location','linkedin',
                'github','description',
        )