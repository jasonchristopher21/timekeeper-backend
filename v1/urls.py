from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'decks', views.DeckViewSet)
router.register(r'slides', views.SlideViewSet)

# Wire up our API using autiomatic URL routing.
# Additionally, we include login URLs for the browsable API
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]