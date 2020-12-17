from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

app_name='scanner'

router=DefaultRouter()
router.register(r'scans',views.ScanViewSet, base_name='my-scans')
router.register(r'users',views.UserViewSet, base_name='users')



urlpatterns = [
    url(r'^api/',include(router.urls)),  
]