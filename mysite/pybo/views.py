from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer, KospiPredict, Metric
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponseNotAllowed
from django.core.paginator import Paginator  
from django.views.generic.base import TemplateView
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from time import mktime, strptime

def index(request):
    page = request.GET.get('page', '1')  # 페이지
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


class Home(TemplateView):
    template_name = 'pybo/gridtest.html'


class KospiPredictAPIView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request):
        stocks = KospiPredict.objects.all().order_by('date')

        close_list = [1,2,3,4]
        open_list = [5,6,7,8,9]
        for stock in stocks:
            time_tuple = strptime(str(stock.date), '%Y-%m-%d')  
            utc_now = mktime(time_tuple) * 1000           
            close_list.append([utc_now, stock.close])
            open_list.append([utc_now, stock.open])

        data = {
            'close': close_list,
            'open': open_list
        }

        return Response(data)

class ChartView(View):
    def get(self, request, *args, **kwargs):
        metric = Metric.objects.all()
        context ={'metric': metric}
        return render(request, 'pybo/dashboard.html',context)


class base(View):
    def get(self, request, *args, **kwargs):
        context ={}
        return render(request, 'pybo/base.html',context)


class SQLView(View):
    def get(self, request, *args, **kwargs):
        context ={}
        return render(request, 'pybo/sql.html',context)
