from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ClientViewSet, NoteViewSet, convert_lead_to_client

router = DefaultRouter()
router.register('clients', ClientViewSet, basename='clients')
router.register('notes', NoteViewSet, basename='notes')

# urlpatterns = router.urls # if it didn't work do it with path and include
urlpatterns = [
    path('convert_lead_to_client/', convert_lead_to_client, name='convert_lead_to_client'),
    path('', include(router.urls)),
]
