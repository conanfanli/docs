from dynamic_rest.serializers import DynamicModelSerializer
from rest_framework import serializers

from things.core.models import Resource


class ResourceSerializer(DynamicModelSerializer):

    class Meta:
        model = Resource
        name = 'resource'
        fields = ('id', 'data')
