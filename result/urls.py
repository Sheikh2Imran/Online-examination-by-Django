from django.urls import path

from result.views import HomeView, ExamListView, ExamView, ResultView

urlpatterns = [
    path('', HomeView.as_view(), name='home page'),
    path('exams/', ExamListView.as_view(), name='exam list'),
    path('exams/exam/', ExamView.as_view(), name='exam'),
    path('exams/exam/result/', ResultView.as_view(), name='result'),
]
