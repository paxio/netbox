from __future__ import unicode_literals

from django.urls import reverse
from rest_framework import status

from tenancy.models import Tenant, TenantGroup, Package
from utilities.testing import APITestCase


class TenantGroupTest(APITestCase):

    def setUp(self):

        super(TenantGroupTest, self).setUp()

        self.tenantgroup1 = TenantGroup.objects.create(name='Test Tenant Group 1', slug='test-tenant-group-1')
        self.tenantgroup2 = TenantGroup.objects.create(name='Test Tenant Group 2', slug='test-tenant-group-2')
        self.tenantgroup3 = TenantGroup.objects.create(name='Test Tenant Group 3', slug='test-tenant-group-3')

    def test_get_tenantgroup(self):

        url = reverse('tenancy-api:tenantgroup-detail', kwargs={'pk': self.tenantgroup1.pk})
        response = self.client.get(url, **self.header)

        self.assertEqual(response.data['name'], self.tenantgroup1.name)

    def test_list_tenantgroups(self):

        url = reverse('tenancy-api:tenantgroup-list')
        response = self.client.get(url, **self.header)

        self.assertEqual(response.data['count'], 3)

    def test_list_tenantgroups_brief(self):

        url = reverse('tenancy-api:tenantgroup-list')
        response = self.client.get('{}?brief=1'.format(url), **self.header)

        self.assertEqual(
            sorted(response.data['results'][0]),
            ['id', 'name', 'slug', 'url']
        )

    def test_create_tenantgroup(self):

        data = {
            'name': 'Test Tenant Group 4',
            'slug': 'test-tenant-group-4',
        }

        url = reverse('tenancy-api:tenantgroup-list')
        response = self.client.post(url, data, format='json', **self.header)

        self.assertHttpStatus(response, status.HTTP_201_CREATED)
        self.assertEqual(TenantGroup.objects.count(), 4)
        tenantgroup4 = TenantGroup.objects.get(pk=response.data['id'])
        self.assertEqual(tenantgroup4.name, data['name'])
        self.assertEqual(tenantgroup4.slug, data['slug'])

    def test_create_tenantgroup_bulk(self):

        data = [
            {
                'name': 'Test Tenant Group 4',
                'slug': 'test-tenant-group-4',
            },
            {
                'name': 'Test Tenant Group 5',
                'slug': 'test-tenant-group-5',
            },
            {
                'name': 'Test Tenant Group 6',
                'slug': 'test-tenant-group-6',
            },
        ]

        url = reverse('tenancy-api:tenantgroup-list')
        response = self.client.post(url, data, format='json', **self.header)

        self.assertHttpStatus(response, status.HTTP_201_CREATED)
        self.assertEqual(TenantGroup.objects.count(), 6)
        self.assertEqual(response.data[0]['name'], data[0]['name'])
        self.assertEqual(response.data[1]['name'], data[1]['name'])
        self.assertEqual(response.data[2]['name'], data[2]['name'])

    def test_update_tenantgroup(self):

        data = {
            'name': 'Test Tenant Group X',
            'slug': 'test-tenant-group-x',
        }

        url = reverse('tenancy-api:tenantgroup-detail', kwargs={'pk': self.tenantgroup1.pk})
        response = self.client.put(url, data, format='json', **self.header)

        self.assertHttpStatus(response, status.HTTP_200_OK)
        self.assertEqual(TenantGroup.objects.count(), 3)
        tenantgroup1 = TenantGroup.objects.get(pk=response.data['id'])
        self.assertEqual(tenantgroup1.name, data['name'])
        self.assertEqual(tenantgroup1.slug, data['slug'])

    def test_delete_tenantgroup(self):

        url = reverse('tenancy-api:tenantgroup-detail', kwargs={'pk': self.tenantgroup1.pk})
        response = self.client.delete(url, **self.header)

        self.assertHttpStatus(response, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TenantGroup.objects.count(), 2)


class TenantTest(APITestCase):

    def setUp(self):

        super(TenantTest, self).setUp()

        self.tenantgroup1 = TenantGroup.objects.create(name='Test Tenant Group 1', slug='test-tenant-group-1')
        self.tenantgroup2 = TenantGroup.objects.create(name='Test Tenant Group 2', slug='test-tenant-group-2')
        self.tenant1 = Tenant.objects.create(name='Test Tenant 1', slug='test-tenant-1', group=self.tenantgroup1)
        self.tenant2 = Tenant.objects.create(name='Test Tenant 2', slug='test-tenant-2', group=self.tenantgroup1)
        self.tenant3 = Tenant.objects.create(name='Test Tenant 3', slug='test-tenant-3', group=self.tenantgroup1)

    def test_get_tenant(self):

        url = reverse('tenancy-api:tenant-detail', kwargs={'pk': self.tenant1.pk})
        response = self.client.get(url, **self.header)

        self.assertEqual(response.data['name'], self.tenant1.name)

    def test_list_tenants(self):

        url = reverse('tenancy-api:tenant-list')
        response = self.client.get(url, **self.header)

        self.assertEqual(response.data['count'], 3)

    def test_list_tenants_brief(self):

        url = reverse('tenancy-api:tenant-list')
        response = self.client.get('{}?brief=1'.format(url), **self.header)

        self.assertEqual(
            sorted(response.data['results'][0]),
            ['description', 'id', 'name', 'slug', 'url']
        )

    def test_create_tenant(self):

        data = {
            'name': 'Test Tenant 4',
            'slug': 'test-tenant-4',
            'group': self.tenantgroup1.pk,
        }

        url = reverse('tenancy-api:tenant-list')
        response = self.client.post(url, data, format='json', **self.header)

        self.assertHttpStatus(response, status.HTTP_201_CREATED)
        self.assertEqual(Tenant.objects.count(), 4)
        tenant4 = Tenant.objects.get(pk=response.data['id'])
        self.assertEqual(tenant4.name, data['name'])
        self.assertEqual(tenant4.slug, data['slug'])
        self.assertEqual(tenant4.group_id, data['group'])

    def test_create_tenant_bulk(self):

        data = [
            {
                'name': 'Test Tenant 4',
                'slug': 'test-tenant-4',
            },
            {
                'name': 'Test Tenant 5',
                'slug': 'test-tenant-5',
            },
            {
                'name': 'Test Tenant 6',
                'slug': 'test-tenant-6',
            },
        ]

        url = reverse('tenancy-api:tenant-list')
        response = self.client.post(url, data, format='json', **self.header)

        self.assertHttpStatus(response, status.HTTP_201_CREATED)
        self.assertEqual(Tenant.objects.count(), 6)
        self.assertEqual(response.data[0]['name'], data[0]['name'])
        self.assertEqual(response.data[1]['name'], data[1]['name'])
        self.assertEqual(response.data[2]['name'], data[2]['name'])

    def test_update_tenant(self):

        data = {
            'name': 'Test Tenant X',
            'slug': 'test-tenant-x',
            'group': self.tenantgroup2.pk,
        }

        url = reverse('tenancy-api:tenant-detail', kwargs={'pk': self.tenant1.pk})
        response = self.client.put(url, data, format='json', **self.header)

        self.assertHttpStatus(response, status.HTTP_200_OK)
        self.assertEqual(Tenant.objects.count(), 3)
        tenant1 = Tenant.objects.get(pk=response.data['id'])
        self.assertEqual(tenant1.name, data['name'])
        self.assertEqual(tenant1.slug, data['slug'])
        self.assertEqual(tenant1.group_id, data['group'])

    def test_delete_tenant(self):

        url = reverse('tenancy-api:tenant-detail', kwargs={'pk': self.tenant1.pk})
        response = self.client.delete(url, **self.header)

        self.assertHttpStatus(response, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tenant.objects.count(), 2)


class PackageTest(APITestCase):

    def setUp(self):

        super(PackageTest, self).setUp()

        self.package1 = Package.objects.create(name='Test Package 1', slug='test-package-1', ipv4_enabled=True, ipv6_enabled=True, multicast_enabled=True, speed_upload=100000, speed_download=100000, qos_profile='normal_qos')
        self.package2 = Package.objects.create(name='Test Package 2', slug='test-package-2', ipv4_enabled=False, ipv6_enabled=True, multicast_enabled=False, speed_upload=10000, speed_download=10000, qos_profile='special_qos')
        self.package3 = Package.objects.create(name='Test Package 3', slug='test-package-3', ipv4_enabled=True, ipv6_enabled=False, multicast_enabled=False, speed_upload=1000, speed_download=1000, qos_profile='normal_qos')

    def test_create_package(self):

        data = {
            'name': 'Test Package 4',
            'slug': 'test-package-4',
            'ipv4_enabled': True,
            'ipv6_enabled': True,
            'multicast_enabled': True,
            'speed_upload': 1000000,
            'speed_download': 1000000,
            'qos_profile': 'normal_qos',
        }

        url = reverse('tenancy-api:package-list')
        response = self.client.post(url, data, format='json', **self.header)

        self.assertHttpStatus(response, status.HTTP_201_CREATED)
        self.assertEqual(Package.objects.count(), 4)
        package4 = Package.objects.get(pk=response.data['id'])
        self.assertEqual(package4.name, data['name'])
        self.assertEqual(package4.slug, data['slug'])
        self.assertEqual(package4.ipv4_enabled, data['ipv4_enabled'])
        self.assertEqual(package4.ipv6_enabled, data['ipv6_enabled'])
        self.assertEqual(package4.multicast_enabled, data['multicast_enabled'])
        self.assertEqual(package4.speed_upload, data['speed_upload'])
        self.assertEqual(package4.speed_download, data['speed_download'])
        self.assertEqual(package4.qos_profile, data['qos_profile'])

    def test_create_package_bulk(self):

        data = [
            {
                'name': 'Test Package 4',
                'slug': 'test-package-4',
                'ipv4_enabled': True,
                'ipv6_enabled': True,
                'multicast_enabled': True,
                'speed_upload': 1000000,
                'speed_download': 1000000,
                'qos_profile': 'normal_qos',
            },
            {
                'name': 'Test Package 5',
                'slug': 'test-package-5',
                'ipv4_enabled': False,
                'ipv6_enabled': False,
                'multicast_enabled': False,
                'speed_upload': 1000000,
                'speed_download': 1000000,
                'qos_profile': 'normal_qos',
            },
            {
                'name': 'Test Package 6',
                'slug': 'test-package-6',
                'ipv4_enabled': True,
                'ipv6_enabled': True,
                'multicast_enabled': True,
                'speed_upload': 100,
                'speed_download': 100,
                'qos_profile': 'special_qos',
            },
        ]

        url = reverse('tenancy-api:package-list')
        response = self.client.post(url, data, format='json', **self.header)

        self.assertHttpStatus(response, status.HTTP_201_CREATED)
        self.assertEqual(Package.objects.count(), 6)
        self.assertEqual(response.data[0]['name'], data[0]['name'])
        self.assertEqual(response.data[1]['name'], data[1]['name'])
        self.assertEqual(response.data[2]['name'], data[2]['name'])

    def test_update_package(self):

        data = {
            'name': 'Test Package X',
            'slug': 'test-package-x',
            'ipv4_enabled': False,
            'ipv6_enabled': False,
            'multicast_enabled': False,
            'speed_upload': 10,
            'speed_download': 10,
            'qos_profile': 'special_qos',
        }

        url = reverse('tenancy-api:package-detail', kwargs={'pk': self.package1.pk})
        response = self.client.put(url, data, format='json', **self.header)

        self.assertHttpStatus(response, status.HTTP_200_OK)
        self.assertEqual(Package.objects.count(), 3)
        package1 = Package.objects.get(pk=response.data['id'])
        self.assertEqual(package1.name, data['name'])
        self.assertEqual(package1.slug, data['slug'])
        self.assertEqual(package1.ipv4_enabled, data['ipv4_enabled'])
        self.assertEqual(package1.ipv6_enabled, data['ipv6_enabled'])
        self.assertEqual(package1.multicast_enabled, data['multicast_enabled'])
        self.assertEqual(package1.speed_upload, data['speed_upload'])
        self.assertEqual(package1.speed_download, data['speed_download'])
        self.assertEqual(package1.qos_profile, data['qos_profile'])

    def test_delete_package(self):

        url = reverse('tenancy-api:package-detail', kwargs={'pk': self.package1.pk})
        response = self.client.delete(url, **self.header)

        self.assertHttpStatus(response, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Package.objects.count(), 2)
