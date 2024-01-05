from django.urls import path

from . import views

app_name = 'polls' # This line is app-specific. It names the app so that Django can distinguish it from other apps that might have the same view or template names.

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('specifics/<int:question_id>/',views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/',views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/',views.vote, name='vote'),
]

# The next step is to point the root URLconf at the polls.urls module.


