from django.urls import path

from result.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home page'),
    # path('/home/', SubjectView.as_view()),
]
