import django_filters
from .models import Professor

class ProfessorFilter(django_filters.FilterSet):
    # Range 
    min_id = django_filters.NumberFilter(field_name='prof_id', lookup_expr='gte')
    max_id = django_filters.NumberFilter(field_name='prof_id', lookup_expr='lte')

    # Case insensitive 
    name = django_filters.CharFilter(field_name='id', lookup_expr='icontains')

    # Case sensative
    degree=django_filters.CharFilter(field_name='prof_id', lookup_expr='exact')

    class Meta:
        model=Professor
        fields=['degree']