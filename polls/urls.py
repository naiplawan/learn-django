from django.urls import path
from . import views

app_name = 'polls' # This line is app-specific. It names the app so that Django can distinguish it from other apps that might have the same view or template names.

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# The next step is to point the root URLconf at the polls.urls module.


