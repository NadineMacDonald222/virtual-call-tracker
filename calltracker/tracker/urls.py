from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CallLogViewSet, dashboard

router = DefaultRouter()
router.register(r'calls', CallLogViewSet)

urlpatterns = [
    path('', include(router.urls)),         # API: /calls/
    path('dashboard/', dashboard, name='dashboard'),  # Dashboard: /dashboard/
]

