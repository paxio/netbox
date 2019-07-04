from django import forms
from taggit.forms import TagField

from extras.forms import AddRemoveTagsForm, CustomFieldForm, CustomFieldBulkEditForm, CustomFieldFilterForm
from utilities.forms import (
    APISelect, APISelectMultiple, BootstrapMixin, ChainedFieldsMixin, ChainedModelChoiceField, CommentField,
    FilterChoiceField, SlugField,
)
from ipam.models import Prefix
from .models import Tenant, TenantGroup, Package
from .constants import SERVICE_TYPE_CHOICES


#
# Tenant groups
#

class TenantGroupForm(BootstrapMixin, forms.ModelForm):
    slug = SlugField()

    class Meta:
        model = TenantGroup
        fields = [
            'name', 'slug',
        ]


class TenantGroupCSVForm(forms.ModelForm):
    slug = SlugField()

    class Meta:
        model = TenantGroup
        fields = TenantGroup.csv_headers
        help_texts = {
            'name': 'Group name',
        }


#
# Tenants
#

class TenantForm(BootstrapMixin, CustomFieldForm):
    slug = SlugField()
    comments = CommentField()
    tags = TagField(
        required=False
    )

    class Meta:
        model = Tenant
        fields = [
            'name', 'slug', 'group', 'description', 'comments', 'tags',
        ]
        widgets = {
            'group': APISelect(
                api_url="/api/tenancy/tenant-groups/"
            )
        }


class TenantCSVForm(forms.ModelForm):
    slug = SlugField()
    group = forms.ModelChoiceField(
        queryset=TenantGroup.objects.all(),
        required=False,
        to_field_name='name',
        help_text='Name of parent group',
        error_messages={
            'invalid_choice': 'Group not found.'
        }
    )

    class Meta:
        model = Tenant
        fields = Tenant.csv_headers
        help_texts = {
            'name': 'Tenant name',
            'comments': 'Free-form comments'
        }


class TenantBulkEditForm(BootstrapMixin, AddRemoveTagsForm, CustomFieldBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=Tenant.objects.all(),
        widget=forms.MultipleHiddenInput()
    )
    group = forms.ModelChoiceField(
        queryset=TenantGroup.objects.all(),
        required=False,
        widget=APISelect(
            api_url="/api/tenancy/tenant-groups/"
        )
    )

    class Meta:
        nullable_fields = [
            'group',
        ]


class TenantFilterForm(BootstrapMixin, CustomFieldFilterForm):
    model = Tenant
    q = forms.CharField(
        required=False,
        label='Search'
    )
    group = FilterChoiceField(
        queryset=TenantGroup.objects.all(),
        to_field_name='slug',
        null_label='-- None --',
        widget=APISelectMultiple(
            api_url="/api/tenancy/tenant-groups/",
            value_field="slug",
            null_option=True,
        )
    )


#
# Form extensions
#

class TenancyForm(ChainedFieldsMixin, forms.Form):
    tenant_group = forms.ModelChoiceField(
        queryset=TenantGroup.objects.all(),
        required=False,
        widget=APISelect(
            api_url="/api/tenancy/tenant-groups/",
            filter_for={
                'tenant': 'group_id',
            },
            attrs={
                'nullable': 'true',
            }
        ),
        label="Service Provider"
    )
    tenant = ChainedModelChoiceField(
        queryset=Tenant.objects.all(),
        chains=(
            ('group', 'tenant_group'),
        ),
        required=False,
        widget=APISelect(
            api_url='/api/tenancy/tenants/?group_id={{tenant_group}}'
        ),
        label="Customer"
    )

    def __init__(self, *args, **kwargs):

        # Initialize helper selector
        instance = kwargs.get('instance')
        if instance and instance.tenant is not None:
            initial = kwargs.get('initial', {}).copy()
            initial['tenant_group'] = instance.tenant.group
            kwargs['initial'] = initial

        super().__init__(*args, **kwargs)


class TenancyFilterForm(forms.Form):
    tenant_group = FilterChoiceField(
        queryset=TenantGroup.objects.all(),
        to_field_name='slug',
        null_label='-- None --',
        widget=APISelectMultiple(
            api_url="/api/tenancy/tenant-groups/",
            value_field="slug",
            null_option=True,
            filter_for={
                'tenant': 'group'
            }
        )
    )
    tenant = FilterChoiceField(
        queryset=Tenant.objects.all(),
        to_field_name='slug',
        null_label='-- None --',
        widget=APISelectMultiple(
            api_url="/api/tenancy/tenants/",
            value_field="slug",
            null_option=True,
        )
    )


#
#  Packages
#

class PackageForm(BootstrapMixin, CustomFieldForm):
    slug = SlugField()

    class Meta:
        model = Package
        fields = ['name', 'slug', 'ipv4_enabled', 'ipv6_enabled', 'multicast_enabled', 'speed_upload', 'speed_download', 'qos_profile', 'comments', 'tags']


class PackageFilterForm(BootstrapMixin, CustomFieldFilterForm):
    model = Package
    q = forms.CharField(required=False, label='Search')


class PackageCSVForm(forms.ModelForm):
    slug = SlugField()

    class Meta:
        model = Package
        fields = Package.csv_headers
        help_texts = {
            'name': 'Package name'
        }


class PackageBulkEditForm(BootstrapMixin, AddRemoveTagsForm, CustomFieldBulkEditForm):
    pk = forms.ModelMultipleChoiceField(queryset=Tenant.objects.all(), widget=forms.MultipleHiddenInput)
    qos_profile = forms.CharField(max_length=100, required=False)

    class Meta:
        nullable_fields = []
