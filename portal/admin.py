from django.contrib import admin

# Register your models here.
from . models import AlumniInfo


@admin.register(AlumniInfo)
class AlumniInfoAdmin(admin.ModelAdmin):
    list_display = ['name','mail_id','phn_no'
                   ]
    list_filter = ['name','company','reg_no'
                  ]
    search_fields = ['reg_no','name','company','experience','location','passed_out','location'
                    ]

