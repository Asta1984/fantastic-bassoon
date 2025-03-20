from django.db import models

from django.db import models
from django.core.validators import MinValueValidator
from datetime import date

class ProductUnavailability(models.Model):
    product_id = models.PositiveIntegerField()  # Assuming you're using integer product IDs
    unavailable_date = models.DateField(
        validators=[MinValueValidator(limit_value=date.today)]
    )
    reason = models.TextField(blank=True, null=True)  # Optional field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['product_id', 'unavailable_date']),
        ]
        unique_together = ('product_id', 'unavailable_date')