from rest_framework import serializers
from .models import Bucketlist

class BucketlistSerializer(serializers.ModelSerializer):
	"""Serializer to map model instance to JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with model fields."""
		model = Bucketlist
		fields = ('id', 'name', 'date_created', 'date_modified')
		read_only_fields = ('date_created', 'date_modified')
			