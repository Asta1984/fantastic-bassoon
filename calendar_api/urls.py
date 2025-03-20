from django.urls import path
from .views import ProductUnavailabilityView

urlpatterns = [
    path(
        'products/<int:product_id>/unavailable-dates/',
        ProductUnavailabilityView.as_view(),
        name='product-unavailability'
    ),
]