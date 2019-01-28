from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField

from extras.api.customfields import CustomFieldModelSerializer
<<<<<<< HEAD
from tenancy.models import Tenant, TenantGroup, Package
from utilities.api import ValidatedModelSerializer, WritableNestedSerializer
=======
from tenancy.models import Tenant, TenantGroup
from utilities.api import ValidatedModelSerializer
from .nested_serializers import *
>>>>>>> v2.5.3


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


class NestedTenantSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='tenancy-api:tenant-detail')

    class Meta:
        model = Tenant
        fields = ['id', 'url', 'name', 'slug', 'description']


class WritableTenantSerializer(CustomFieldModelSerializer):

    class Meta:
        model = Tenant
        fields = ['id', 'name', 'slug', 'group', 'description', 'comments', 'custom_fields', 'created', 'last_updated']


#
#  Packages
#

class NestedPackageSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='tenancy-api:package-detail')

    class Meta:
        model = Package
        fields = ['id', 'url', 'name', 'slug']


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

