from django.urls import path
from . import views

app_name = 'polls' # This line is app-specific. It names the app so that Django can distinguish it from other apps that might have the same view or template names.

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

#Change the index view in polls/views.py to use Django’s generic views system.


