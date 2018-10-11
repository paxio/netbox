from __future__ import unicode_literals

import django_tables2 as tables

from utilities.tables import BaseTable, ToggleColumn
from .models import Tenant, TenantGroup, Package

TENANTGROUP_ACTIONS = """
<a href="{% url 'tenancy:tenantgroup_changelog' slug=record.slug %}" class="btn btn-default btn-xs" title="Changelog">
    <i class="fa fa-history"></i>
</a>
{% if perms.tenancy.change_tenantgroup %}
    <a href="{% url 'tenancy:tenantgroup_edit' slug=record.slug %}" class="btn btn-xs btn-warning"><i class="glyphicon glyphicon-pencil" aria-hidden="true"></i></a>
{% endif %}
"""

COL_TENANT = """
{% if record.tenant %}
    <a href="{% url 'tenancy:tenant' slug=record.tenant.slug %}" title="{{ record.tenant.description }}">{{ record.tenant }}</a>
{% else %}
    &mdash;
{% endif %}
"""

PACKAGE_ACTIONS = """
{% if perms.tenancy.change_package %}
    <a href="{% url 'tenancy:package_edit' slug=record.slug %}" class="btn btn-xs btn-warning"><i class="glyphicon glyphicon-pencil" aria-hidden="true"></i></a>
{% endif %}
"""


#
# Tenant groups
#

class TenantGroupTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn(verbose_name='Name')
    tenant_count = tables.Column(verbose_name='Tenants')
    slug = tables.Column(verbose_name='Slug')
    actions = tables.TemplateColumn(
        template_code=TENANTGROUP_ACTIONS, attrs={'td': {'class': 'text-right'}}, verbose_name=''
    )

    class Meta(BaseTable.Meta):
        model = TenantGroup
        fields = ('pk', 'name', 'tenant_count', 'slug', 'actions')


#
# Tenants
#

class TenantTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = Tenant
        fields = ('pk', 'name', 'group', 'description')

#
#  Packages
#

class PackageTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn()
    actions = tables.TemplateColumn(
        template_code=PACKAGE_ACTIONS, attrs={'td': {'class': 'text-right'}}, verbose_name=''
    )

    class Meta(BaseTable.Meta):
        model = Package
        fields = ('pk', 'name', 'group', 'ipv4_enabled', 'ipv6_enabled', 'multicast_enabled', 'service_type', 'speed_upload', 'speed_download', 'dhcp_pool')
