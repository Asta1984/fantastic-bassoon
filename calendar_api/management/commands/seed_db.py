from django.core.management.base import BaseCommand
from calendar_api.models import ProductUnavailability
from django.utils import timezone
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed database with test data'

    def handle(self, *args, **options):
        fake = Faker()
        
        # Clear existing data
        ProductUnavailability.objects.all().delete()
        
        # Create 10 products with random unavailability dates
        for product_id in range(1, 11):
            for _ in range(random.randint(1, 5)):  # 1-5 dates per product
                ProductUnavailability.objects.create(
                    product_id=product_id,
                    unavailable_date=fake.date_between(
                        start_date='today',
                        end_date='+30d'
                    ),
                    reason=fake.sentence()
                )
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))