from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import serializers  # Add missing import
from .models import ProductUnavailability
from .serializers import UnavailabilitySerializer, BulkUnavailabilitySerializer
from django.utils import timezone

class ProductUnavailabilityView(generics.ListCreateAPIView):
    serializer_class = UnavailabilitySerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return ProductUnavailability.objects.filter(
            product_id=product_id,
            unavailable_date__gte=timezone.now().date()
        ).order_by('unavailable_date')

    def create(self, request, *args, **kwargs):
        product_id = self.kwargs['product_id']
        serializer = BulkUnavailabilitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Validate dates before processing
        dates = serializer.validated_data['dates']
        self.validate_dates(dates)  # Call validation method

        # Delete existing entries
        ProductUnavailability.objects.filter(product_id=product_id).delete()

        # Create new entries
        reason = serializer.validated_data.get('reason', '')
        objs = [
            ProductUnavailability(
                product_id=product_id,
                unavailable_date=date,
                reason=reason
            ) for date in dates
        ]
        ProductUnavailability.objects.bulk_create(objs)

        return Response(
            {'status': 'success', 'updated_entries': len(objs)},
            status=status.HTTP_201_CREATED
        )

    # Properly indented class method
    def validate_dates(self, dates):
        today = timezone.now().date()
        for date in dates:
            if date < today:
                raise serializers.ValidationError(
                    "Cannot set unavailability for past dates"
                )