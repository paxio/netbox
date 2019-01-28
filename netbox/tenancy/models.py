from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

from extras.models import CustomFieldModel
from utilities.models import ChangeLoggedModel
from .constants import *


class TenantGroup(ChangeLoggedModel):
    """
    An arbitrary collection of Tenants.
    """
    name = models.CharField(
        max_length=50,
        unique=True
    )
    slug = models.SlugField(
        unique=True
    )

    csv_headers = ['name', 'slug']

    class Meta:
        ordering = ['name']
        verbose_name = 'Service Provider'
        verbose_name_plural = 'Service Providers'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "{}?group={}".format(reverse('tenancy:tenant_list'), self.slug)

    def to_csv(self):
        return (
            self.name,
            self.slug,
        )


class Tenant(ChangeLoggedModel, CustomFieldModel):
    """
    A Tenant represents an organization served by the NetBox owner. This is typically a customer or an internal
    department.
    """
    name = models.CharField(
        max_length=30,
        unique=True
    )
    slug = models.SlugField(
        unique=True
    )
    group = models.ForeignKey(
        to='tenancy.TenantGroup',
        on_delete=models.SET_NULL,
        related_name='tenants',
        blank=True,
        null=True
    )
    description = models.CharField(
        max_length=100,
        blank=True,
        help_text='Long-form name (optional)'
    )
    comments = models.TextField(
        blank=True
    )
    custom_field_values = GenericRelation(
        to='extras.CustomFieldValue',
        content_type_field='obj_type',
        object_id_field='obj_id'
    )

    tags = TaggableManager()

    csv_headers = ['name', 'slug', 'group', 'description', 'comments']

    class Meta:
        ordering = ['group', 'name']
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tenancy:tenant', args=[self.slug])

    def to_csv(self):
        return (
            self.name,
            self.slug,
            self.group.name if self.group else None,
            self.description,
            self.comments,
        )


class Package(ChangeLoggedModel, CustomFieldModel):
    """
    A Package represents a service delivered to our customers.
    """
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(unique=True)

    ipv4_enabled = models.BooleanField(blank=False, default=True, verbose_name='IPv4 is enabled', help_text='Customers recieve an IPv4 address')
    ipv6_enabled = models.BooleanField(blank=False, default=True, verbose_name='IPv6 is enabled', help_text='Customers recieve an IPv6 address')
    multicast_enabled = models.BooleanField(blank=False, default=True, verbose_name='Multicast is enabled', help_text='Customers can use multicast')
    speed_upload = models.PositiveIntegerField(blank=False, null=False, verbose_name='Upload speed rate (Kbps)')
    speed_download = models.PositiveIntegerField(blank=False, null=False, verbose_name='Download speed rate (Kbps)')
    qos_profile = models.CharField(max_length=30, unique=False)

    comments = models.TextField(
        blank=True
    )
    custom_field_values = GenericRelation(
        to='extras.CustomFieldValue',
        content_type_field='obj_type',
        object_id_field='obj_id'
    )

    tags = TaggableManager()

    csv_headers = ['name', 'slug', 'ipv4_enabled', 'ipv6_enabled', 'multicast_enabled', 'speed_upload', 'speed_download', 'qos_profile']

    class Meta:
        ordering = ['name']
        verbose_name = 'Package'
        verbose_name_plural = 'Packages'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tenancy:package', args=[self.slug])

    def to_csv(self):
        return (
            self.name,
            self.slug,
            self.ipv4_enabled,
            self.ipv6_enabled,
            self.multicast_enabled,
            self.speed_upload,
            self.speed_download,
            self.qos_profile,
        )
