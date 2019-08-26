from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('home-viewset', views.HomeApiViewset, base_name='home-viewset')

urlpatterns = [
    path('test/', views.HomeApiView.as_view()),
    path('', include(router.urls))
]