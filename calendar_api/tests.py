from django.urls import reverse
from rest_framework.test import APITestCase
from django.utils import timezone
from .models import ProductUnavailability
from datetime import timedelta

class UnavailabilityTests(APITestCase):
    def test_create_unavailability(self):
        # Create future dates relative to current date
        today = timezone.now().date()
        future_date_1 = today + timedelta(days=1)
        future_date_2 = today + timedelta(days=2)
        
        url = reverse('product-unavailability', kwargs={'product_id': 1})
        data = {
            'dates': [
                future_date_1.isoformat(),
                future_date_2.isoformat()
            ],
            'reason': 'Maintenance'
        }
        
        response = self.client.post(url, data, format='json')
        print(response.data)  # For debugging
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ProductUnavailability.objects.count(), 2)