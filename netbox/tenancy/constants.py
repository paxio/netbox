from __future__ import unicode_literals

SERVICE_TYPE_STATIC = 0
SERVICE_TYPE_DYNAMIC = 1
SERVICE_TYPE_CHOICES = (
    (SERVICE_TYPE_STATIC, 'Static configuration'),
    (SERVICE_TYPE_DYNAMIC, 'Dynamic configuration')
)

TAG_TYPE_UNTAGGED = 0
TAG_TYPE_SINGLETAGGED = 1
TAG_TYPE_DOUBLETAGGED = 2
TAG_TYPE_CHOICES = (
  (TAG_TYPE_UNTAGGED, 'Untagged port'),
  (TAG_TYPE_SINGLETAGGED, 'Single tagged port'),
  (TAG_TYPE_DOUBLETAGGED, 'Double tagged port')
)
