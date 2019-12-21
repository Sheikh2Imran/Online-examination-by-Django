from django.urls import path

from result.views import HomeView, ExamListView, ExamView, ResultView, AnswerView

urlpatterns = [
    path('', HomeView.as_view(), name='home page'),
    path('exams/', ExamListView.as_view(), name='exam list'),
    path('exams/exam/', ExamView.as_view(), name='exam'),
    path('exams/exam/answer/', AnswerView.as_view(), name='answer'),
    path('exams/exam/answer/result/', ResultView.as_view(), name='result'),
]
