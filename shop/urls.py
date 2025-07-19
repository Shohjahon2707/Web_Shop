# shop/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # ⬅️ Подключаем urls.py из приложения main
]

# Для отображения медиа-файлов (например, картинок товаров)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
