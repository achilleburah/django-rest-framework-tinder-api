from django_filters import rest_framework as filters
from users.models import CustomUser


class UserProposalsFilter(filters.FilterSet):

    distance_max = filters.NumberFilter(field_name='distance', lookup_expr='lte')
    class Meta:
        model = CustomUser
        fields = ['distance_max',]
