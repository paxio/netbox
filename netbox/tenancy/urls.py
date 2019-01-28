from django.conf.urls import url

from extras.views import ObjectChangeLogView
from . import views
from .models import Tenant, TenantGroup, Package

app_name = 'tenancy'
urlpatterns = [

    # Tenant groups
    url(r'^service-providers/$', views.TenantGroupListView.as_view(), name='tenantgroup_list'),
    url(r'^service-providers/add/$', views.TenantGroupCreateView.as_view(), name='tenantgroup_add'),
    url(r'^service-providers/import/$', views.TenantGroupBulkImportView.as_view(), name='tenantgroup_import'),
    url(r'^service-providers/delete/$', views.TenantGroupBulkDeleteView.as_view(), name='tenantgroup_bulk_delete'),
    url(r'^service-providers/(?P<slug>[\w-]+)/edit/$', views.TenantGroupEditView.as_view(), name='tenantgroup_edit'),
    url(r'^service-providers/(?P<slug>[\w-]+)/changelog/$', ObjectChangeLogView.as_view(), name='tenantgroup_changelog', kwargs={'model': TenantGroup}),

    # Tenants
    url(r'^customers/$', views.TenantListView.as_view(), name='tenant_list'),
    url(r'^customers/add/$', views.TenantCreateView.as_view(), name='tenant_add'),
    url(r'^customers/import/$', views.TenantBulkImportView.as_view(), name='tenant_import'),
    url(r'^customers/edit/$', views.TenantBulkEditView.as_view(), name='tenant_bulk_edit'),
    url(r'^customers/delete/$', views.TenantBulkDeleteView.as_view(), name='tenant_bulk_delete'),
    url(r'^customers/(?P<slug>[\w-]+)/$', views.TenantView.as_view(), name='tenant'),
    url(r'^customers/(?P<slug>[\w-]+)/edit/$', views.TenantEditView.as_view(), name='tenant_edit'),
    url(r'^customers/(?P<slug>[\w-]+)/delete/$', views.TenantDeleteView.as_view(), name='tenant_delete'),
    url(r'^customers/(?P<slug>[\w-]+)/changelog/$', ObjectChangeLogView.as_view(), name='tenant_changelog', kwargs={'model': Tenant}),

    # Packages
    url(r'^packages/$', views.PackageListView.as_view(), name='package_list'),
    url(r'^packages/add/$', views.PackageCreateView.as_view(), name='package_add'),
    url(r'^packages/import/$', views.PackageBulkImportView.as_view(), name='package_import'),
    url(r'^packages/edit/$', views.PackageBulkEditView.as_view(), name='package_bulk_edit'),
    url(r'^packages/delete/$', views.PackageBulkDeleteView.as_view(), name='package_bulk_delete'),
    url(r'^packages/(?P<slug>[\w-]+)/$', views.PackageView.as_view(), name='package'),
    url(r'^packages/(?P<slug>[\w-]+)/edit/$', views.PackageEditView.as_view(), name='package_edit'),
    url(r'^packages/(?P<slug>[\w-]+)/delete/$', views.PackageDeleteView.as_view(), name='package_delete'),
    url(r'^packages/(?P<slug>[\w-]+)/changelog/$', ObjectChangeLogView.as_view(), name='package_changelog', kwargs={'model': Package}),

]
