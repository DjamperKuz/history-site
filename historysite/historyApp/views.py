import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView

from .forms import RegisterUserForm
from .models import Question, Topic, TestResult


def main_page(request):
    return render(request, 'historyApp/main_page.html')


def text_1(request):
    return render(request, 'historyApp/text_1.html')


def text_2(request):
    return render(request, 'historyApp/text_2.html')


def text_3(request):
    return render(request, 'historyApp/text_3.html')


def about_us(request):
    return render(request, 'historyApp/about_us.html')


def subject(request, topic_id):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST':
            topic = Topic.objects.get(id=topic_id)
            questions = Question.objects.filter(topic=topic)
            total_questions = 5
            correct_answers = 0

            for question in questions:
                selected_answer_id = request.POST.get(f'question_{question.id}')
                correct_answer_id = question.answer_set.filter(is_correct=True).first().id

                if selected_answer_id == str(correct_answer_id):
                    correct_answers += 1

            request.session['message'] = f'Вы ответили правильно на {correct_answers} из {total_questions} вопросов.'

            return redirect('result_page', topic_id=topic_id)

        else:
            topic = Topic.objects.get(id=topic_id)
            all_questions = Question.objects.filter(topic=topic)
            random_questions = random.sample(list(all_questions), 5)
            context = {'topic': topic, 'questions': random_questions}
            return render(request, f'historyApp/subject_{topic_id}.html', context)


def result_page(request, topic_id):
    message = request.session.pop('message', '')  # Получаем сообщение из сессии и удаляем его
    context = {'message': message}
    test = Topic.objects.get(id=topic_id)
    test_result = TestResult(user=request.user, test=test, score=message)
    test_result.save()
    return render(request, f'historyApp/result_page.html', context)


def all_results(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        user = request.user
        test_results = TestResult.objects.filter(user=user)
        context = {'test_results': test_results}
        return render(request, 'historyApp/all_results.html', context)


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')  # Перенаправление на главную страницу после успешного входа
        else:
            # Обработка неверных учетных данных
            return render(request, 'historyApp/login.html', {'error_message': 'Неверные учетные данные'})

    return render(request, 'historyApp/login.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'historyApp/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main_page')


def logout_view(request):
    logout(request)
    return redirect('login')
