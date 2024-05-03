import django_filters
from .models import Education

class EducationFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    teacher_name = django_filters.CharFilter(field_name="teacher__name")
    teacher_family = django_filters.CharFilter(field_name="teacher__family")
    group_title = django_filters.CharFilter(field_name="group__group_title")
    # feature_name = django_filters.CharFilter(field_name="feature__feature_name")
    filter_value = django_filters.CharFilter(field_name="feature__educationfeature__filter_value__value_title")

    class Meta:
        model = Education
        fields = ['min_price', 'max_price', 'teacher_name', 'teacher_family', 'group_title', 'filter_value']
