from extras.api.views import CustomFieldModelViewSet
from tenancy import filters
from tenancy.models import Tenant, TenantGroup, Package
from utilities.api import FieldChoicesViewSet, ModelViewSet
from . import serializers


#
# Field choices
#

class TenancyFieldChoicesViewSet(FieldChoicesViewSet):
    fields = ()


#
# Tenant Groups
#

class TenantGroupViewSet(ModelViewSet):
    queryset = TenantGroup.objects.all()
    serializer_class = serializers.TenantGroupSerializer
    filterset_class = filters.TenantGroupFilter


#
# Tenants
#

class TenantViewSet(CustomFieldModelViewSet):
    queryset = Tenant.objects.select_related('group').prefetch_related('tags')
    serializer_class = serializers.TenantSerializer
    filter_class = filters.TenantFilter


#
#  Packages
#

class PackageViewSet(CustomFieldModelViewSet):
    queryset = Package.objects.all()
    serializer_class = serializers.PackageSerializer
    write_serializer_class = serializers.WritablePackageSerializer
    filter_class = filters.PackageFilter
