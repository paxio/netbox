from __future__ import unicode_literals

from rest_framework import serializers

from extras.api.customfields import CustomFieldModelSerializer
from tenancy.models import Tenant, TenantGroup, Package
from utilities.api import ValidatedModelSerializer


#
# Tenant groups
#

class TenantGroupSerializer(ValidatedModelSerializer):

    class Meta:
        model = TenantGroup
        fields = ['id', 'name', 'slug']


class NestedTenantGroupSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='tenancy-api:tenantgroup-detail')

    class Meta:
        model = TenantGroup
        fields = ['id', 'url', 'name', 'slug']


#
# Tenants
#

class TenantSerializer(CustomFieldModelSerializer):
    group = NestedTenantGroupSerializer()

    class Meta:
        model = Tenant
        fields = ['id', 'name', 'slug', 'group', 'description', 'comments', 'custom_fields', 'created', 'last_updated']


class NestedTenantSerializer(CustomFieldModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='tenancy-api:tenant-detail')

    class Meta:
        model = Tenant
        fields = ['id', 'url', 'name', 'slug', 'custom_fields']


class WritableTenantSerializer(CustomFieldModelSerializer):

    class Meta:
        model = Tenant
        fields = ['id', 'name', 'slug', 'group', 'description', 'comments', 'custom_fields', 'created', 'last_updated']

#
#  Packages
#

class NestedPackageSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='tenancy-api:package-detail')

    class Meta:
        model = Package
        fields = ['id', 'url', 'name', 'slug', 'tag_type']

class PackageSerializer(CustomFieldModelSerializer):
    group = NestedPackageSerializer()

    class Meta:
        model = Package
        fields = ['id', 'name', 'slug', 'group', 'ipv4_enabled', 'ipv6_enabled', 'multicast_enabled', 'service_type', 'speed_upload', 'speed_download', 'qos_profile', 'dhcp_pool', 'tag_type']


class WritablePackageSerializer(CustomFieldModelSerializer):

    class Meta:
        model = Package
        fields = ['id', 'name', 'slug', 'group', 'ipv4_enabled', 'ipv6_enabled', 'multicast_enabled', 'service_type', 'speed_upload', 'speed_download', 'qos_profile', 'dhcp_pool', 'tag_type']

