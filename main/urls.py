from django.urls import path
from main import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index.html', views.home_view, name='home'),
    path('products/', views.products_view, name='products'),
    path('product/<int:pk>/', views.product_detail_view, name='product_detail'),
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('apply-discount/', views.apply_discount, name='apply_discount'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
