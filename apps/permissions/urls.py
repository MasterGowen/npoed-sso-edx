 
from django.conf.urls import url, include
import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', views.UserAPIViewSet)
router.register(r'role', views.RoleAPIViewSet)

urlpatterns = url(r'^api/permissions/', include(router.urls, namespace='api-permissons')),