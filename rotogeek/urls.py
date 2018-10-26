from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from applications.views import EmployeeViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
]
