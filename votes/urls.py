from django.urls import path
from . import views
app_name = 'votes'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('candidate_create/', views.candidate_create, name='ccreate'),
    path('position_create/', views.position_create, name='pcreate'),
    path('<int:candidate_id>/', views.candidate_detail, name='detail'),
    path('<int:candidate_id>/candidate_update', views.candidate_update, name='candidate_update'),
    path('<int:candidate_id>/vote', views.vote, name='vote')
]