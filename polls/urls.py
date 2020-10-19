from django.urls import path
from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)

app_name='polls'
urlpatterns = [
    # ex: /polls/
    #path('', views.index, name='index'),
    path('', include(router.urls)),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('add/', views.add, name='add'),
]