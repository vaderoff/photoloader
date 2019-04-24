from django.urls import path
from .views import PhotoViewSet

urlpatterns = [
    path('photos/', PhotoViewSet.as_view({'get': 'list'}), name='photo-list'),
    path('photo/', PhotoViewSet.as_view({'post': 'load'}), name='photo-load')
]