from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, UserDetail, get_my_teams, add_member

router = DefaultRouter()
router.register('', TeamViewSet, basename='teams')

# urlpatterns = router.urls # if it didn't work do it with path and include
urlpatterns = [
    path('teams/member/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('teams/get-my-team/', get_my_teams, name='get-my-team'),
    path('teams/add-member/', add_member, name='add-member'),
    path('teams/', include(router.urls)),
]
