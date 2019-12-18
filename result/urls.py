from django.urls import path

from result.views import HomeView, SubjectView, ExamView, ResultView

urlpatterns = [
    path('', HomeView.as_view(), name='home page'),
    path('subject/', SubjectView.as_view(), name='subjects'),
    path('subject/exam/', ExamView.as_view(), name='exam'),
    path('subject/exam/result/', ResultView.as_view(), name='result'),
]
