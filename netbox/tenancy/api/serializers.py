from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField

from extras.api.customfields import CustomFieldModelSerializer
from tenancy.models import Tenant, TenantGroup, Package
from utilities.api import ValidatedModelSerializer
from .nested_serializers import *


#
# Tenants
#

class TenantGroupSerializer(ValidatedModelSerializer):

    class Meta:
        model = TenantGroup
        fields = ['id', 'name', 'slug']


class TenantSerializer(TaggitSerializer, CustomFieldModelSerializer):
    group = NestedTenantGroupSerializer(required=False)
    tags = TagListSerializerField(required=False)

    class Meta:
        model = Tenant
        fields = [
            'id', 'name', 'slug', 'group', 'description', 'comments', 'tags', 'custom_fields', 'created',
            'last_updated',
        ]


class WritableTenantSerializer(CustomFieldModelSerializer):

    class Meta:
        model = Tenant
        fields = ['id', 'name', 'slug', 'group', 'description', 'comments', 'custom_fields', 'created', 'last_updated']


#
#  Packages
#

class PackageSerializer(TaggitSerializer, CustomFieldModelSerializer):
    tags = TagListSerializerField(required=False)

    class Meta:
        model = Package
        fields = [
            'id', 'name', 'slug', 'ipv4_enabled', 'ipv6_enabled', 'multicast_enabled', 'speed_upload', 'speed_download',
            'qos_profile', 'comments', 'tags', 'custom_fields', 'created', 'last_updated',
        ]


class WritablePackageSerializer(CustomFieldModelSerializer):

    class Meta:
        model = Package
        fields = [
            'id', 'name', 'slug', 'ipv4_enabled', 'ipv6_enabled', 'multicast_enabled', 'speed_upload', 'speed_download',
            'qos_profile', 'comments', 'custom_fields', 'created', 'last_updated'
        ]

