from rest_framework import serializers

from tenancy.models import Tenant, TenantGroup, Package
from utilities.api import WritableNestedSerializer

__all__ = [
    'NestedTenantGroupSerializer',
    'NestedTenantSerializer',
    'NestedPackageSerializer',
]


#
# Tenants
#

class NestedTenantGroupSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='tenancy-api:tenantgroup-detail')

    class Meta:
        model = TenantGroup
        fields = ['id', 'url', 'name', 'slug']


class NestedTenantSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='tenancy-api:tenant-detail')

    class Meta:
        model = Tenant
        fields = ['id', 'url', 'name', 'slug', 'description']


#
#  Packages
#

class NestedPackageSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='tenancy-api:package-detail')

    class Meta:
        model = Package
        fields = ['id', 'url', 'name', 'slug']
