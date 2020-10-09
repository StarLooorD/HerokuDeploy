from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # REST API urls
    path('admin/', admin.site.urls),
    path('api/v1/base-auth/', include('rest_framework.urls')),
    path('api/v1/author/', include('author.urls')),
    path('api/v1/book/', include('book.urls')),
    path('api/v1/order/', include('order.urls')),
]
