from django.shortcuts import redirect, render
from django.views import View

from result.forms import UserForm, SubjectForm
from result.models import User, UserAnswer
from questions.models import Subject, Question
from pagination.models import Pagination


class HomeView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'result/home.html', {'form': form})

    def post(self, request):
        form = UserForm(data=request.POST)
        if not form.is_valid():
            return render(request, 'result/home.html', {'form': form})
        user_object = User.objects.get_or_create_user(name=request.POST['name'], email=request.POST['email'])
        if not user_object:
            return render(request, 'result/home.html', {'form': form})
        request.session['user_id'] = user_object.id
        return redirect('subject/')


class SubjectView(View):
    def get(self, request):
        subjects = Subject.objects.all()
        return render(request, 'result/subjects.html', {'subjects': subjects})

    def post(self, request):
        form = SubjectForm(data=request.POST)
        if not form.is_valid():
            return render(request, 'result/subjects.html', {'form': form})
        request.session['subject_id'] = request.POST['id']
        return redirect('exam/')


class ExamView(View):
    def get(self, request):
        page = Pagination.objects.create_pagination(request.session)
        questions = Question.objects.get_question(request.session['subject_id'])[page.start:page.end]
        return render(request, 'result/exam.html', {'questions': questions})

    def post(self, request):
        answer_obj = UserAnswer.objects.store_user_answer(request.session, request.POST)
        if not answer_obj:
            return render(request, 'result/subject.html')
        pagination = Pagination.objects.update_pagination(request.session)
        questions = Question.objects.get_question(request.session['subject_id'])[pagination.start:pagination.end]
        if not questions:
            return redirect('result/')
        return render(request, 'result/exam.html', {'questions': questions})


class ResultView(View):
    def get(self, request):
        return render(request, 'result/results.html')