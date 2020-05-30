import django_filters
from django_filters import CharFilter

from .models import POST


class POSTFilter(django_filters.FilterSet):

    name = CharFilter(field_name='name', lookup_expr='icontains', label='')

    class Meta:
        model = POST
        fields = "__all__"
        exclude = ['picture', 'rating', 'notes', 'user']
