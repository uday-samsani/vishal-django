from .models import AlumniInfo
import django_filters
# do pip install "django-filters" then add "django_filters" to installed apps
class AlumniInfoFilter(django_filters.FilterSet):
    class Meta:
        model = AlumniInfo
        fields = ['name' ]