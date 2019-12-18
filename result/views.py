from django.shortcuts import redirect, render
from django.views import View

from exam.models import Exam, ExamQuestion
from result.forms import UserForm, ExamForm
from result.models import User, UserAnswer, UserResult
from questions.models import Subject, Question
from pagination.models import Pagination


class HomeView(View):
    def get(self, request):
        return render(request, 'result/home.html')

    def post(self, request):
        form = UserForm(data=request.POST)
        if not form.is_valid():
            return render(request, 'result/home.html')
        user_object = User.objects.get_or_create_user(name=request.POST['name'], email=request.POST['email'])
        if not user_object:
            return render(request, 'result/home.html')
        request.session['user_id'] = user_object.id
        return redirect('exams/')


class ExamListView(View):
    def get(self, request):
        exams = Exam.objects.get_published_exams()
        return render(request, 'result/exams.html', {'exams': exams})

    def post(self, request):
        form = ExamForm(data=request.POST)
        if not form.is_valid():
            return render(request, 'result/home.html')
        request.session['exam_id'] = request.POST['id']
        return redirect('exam/')


class ExamView(View):
    def get(self, request):
        page = Pagination.objects.create_pagination(request.session)
        questions = ExamQuestion.objects.get_exam_questions(request.session['exam_id'])[page.start:page.end]
        return render(request, 'result/exam.html', {'questions': questions})

    def post(self, request):
        answered_obj = UserAnswer.objects.store_user_answer(request.session, request.POST)
        if not answered_obj:
            return render(request, 'result/exams.html')
        page = Pagination.objects.update_pagination(request.session)
        questions = ExamQuestion.objects.get_exam_questions(request.session['exam_id'])[page.start:page.end]
        if questions:
            return render(request, 'result/exam.html', {'questions': questions})
        else:
            return redirect('result/')


class ResultView(View):
    def get(self, request):
        results = UserResult.objects.get_user_result(request.session['exam_id'])
        return render(request, 'result/results.html', {'results': results})