from django.urls import path
from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)


app_name='blog'
urlpatterns = [
    # ex: /blog/
   # path('', views.IndexView.as_view(), name='index'),
    path('', include(router.urls)),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

]