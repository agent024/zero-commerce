from django.urls.conf import path
from .views import HomeView, add_one_to_cart, add_to_cart, checkout, ItemDetailView, remove_from_cart, OrderSummaryView, remove_single_item_from_cart

app_name = 'core'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('checkout', checkout, name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('add-one-to-cart/<slug>/', add_one_to_cart, name='add-one-to-cart'),
]
