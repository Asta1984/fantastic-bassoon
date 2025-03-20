from rest_framework import serializers
from .models import ProductUnavailability

class UnavailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductUnavailability
        fields = ['unavailable_date', 'reason']
        read_only_fields = ['product_id']

class BulkUnavailabilitySerializer(serializers.Serializer):
    dates = serializers.ListField(
        child=serializers.DateField(),
        min_length=1
    )
    reason = serializers.CharField(required=False, allow_blank=True)