from django.urls import path

from extras.views import ObjectChangeLogView
from . import views
from .models import Tenant, TenantGroup, Package

app_name = 'tenancy'
urlpatterns = [

    # Tenant groups
    path(r'service-providers/', views.TenantGroupListView.as_view(), name='tenantgroup_list'),
    path(r'service-providers/add/', views.TenantGroupCreateView.as_view(), name='tenantgroup_add'),
    path(r'service-providers/import/', views.TenantGroupBulkImportView.as_view(), name='tenantgroup_import'),
    path(r'service-providers/delete/', views.TenantGroupBulkDeleteView.as_view(), name='tenantgroup_bulk_delete'),
    path(r'service-providers/<slug:slug>/edit/', views.TenantGroupEditView.as_view(), name='tenantgroup_edit'),
    path(r'service-providers/<slug:slug>/changelog/', ObjectChangeLogView.as_view(), name='tenantgroup_changelog', kwargs={'model': TenantGroup}),

    # Tenants
    path(r'customers/', views.TenantListView.as_view(), name='tenant_list'),
    path(r'customers/add/', views.TenantCreateView.as_view(), name='tenant_add'),
    path(r'customers/import/', views.TenantBulkImportView.as_view(), name='tenant_import'),
    path(r'customers/edit/', views.TenantBulkEditView.as_view(), name='tenant_bulk_edit'),
    path(r'customers/delete/', views.TenantBulkDeleteView.as_view(), name='tenant_bulk_delete'),
    path(r'customers/<slug:slug>/', views.TenantView.as_view(), name='tenant'),
    path(r'customers/<slug:slug>/edit/', views.TenantEditView.as_view(), name='tenant_edit'),
    path(r'customers/<slug:slug>/delete/', views.TenantDeleteView.as_view(), name='tenant_delete'),
    path(r'customers/<slug:slug>/changelog/', ObjectChangeLogView.as_view(), name='tenant_changelog', kwargs={'model': Tenant}),

    # Packages
    url(r'packages/', views.PackageListView.as_view(), name='package_list'),
    url(r'packages/add/', views.PackageCreateView.as_view(), name='package_add'),
    url(r'packages/import/', views.PackageBulkImportView.as_view(), name='package_import'),
    url(r'packages/edit/', views.PackageBulkEditView.as_view(), name='package_bulk_edit'),
    url(r'packages/delete/', views.PackageBulkDeleteView.as_view(), name='package_bulk_delete'),
    url(r'packages/<slug:slug>/', views.PackageView.as_view(), name='package'),
    url(r'packages/<slug:slug>/edit/', views.PackageEditView.as_view(), name='package_edit'),
    url(r'packages/<slug:slug>/delete/', views.PackageDeleteView.as_view(), name='package_delete'),
    url(r'packages/<slug:slug>/changelog/', ObjectChangeLogView.as_view(), name='package_changelog', kwargs={'model': Package}),

]
