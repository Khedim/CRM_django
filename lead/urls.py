from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeadViewSet

router = DefaultRouter()
router.register('', LeadViewSet, basename='leads')

# urlpatterns = router.urls # if it didn't work do it with path and include
urlpatterns = [
    path('leads/', include(router.urls)),
]
