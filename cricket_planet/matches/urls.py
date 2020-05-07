from django.urls import path
from . import views

urlpatterns = [
    # path('all_matches/', pass),
    path('fixtures/',views.fixturesView.as_view())
]