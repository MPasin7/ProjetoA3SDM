from django.urls import include, path
from . import views
from rest_framework import routers

app_name = 'endereco'

router = routers.DefaultRouter()
router.register('', views.EnderecoMViewSet, basename='endereco')

urlpatterns = [
    path('', include(router.urls) )
]
