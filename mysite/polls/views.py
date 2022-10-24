from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic import View
from django import forms
from django.views.generic.edit import FormView
from django.utils.functional import cached_property


from rest_framework.views import APIView
from .serializers import ProductSerializer, DataSerializer
from rest_framework.response import Response

from .models import Choice, Question, Product, Data, KospiPredict, Post, Side_Var
from .forms import SelectQueryForm

from time import mktime, strptime

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# Create your views here.


class sidebarMixin(object): 
    @cached_property
    def getList(self):
        return Side_Var.objects.all()


class ContactFormView(FormView):
    template_name = 'polls/contact.html'
    form_class = SelectQueryForm
    success_url = '/thanks/'
    def get_query(request):
        if request.method == 'POST':
            print(request.method)
            pass
        else:
            print(request.method)
            pass
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

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

class ChartView(sidebarMixin,View):
    def get(self, request, *args, **kwargs):
        context ={'sidebarList': Side_Var.objects.all()}
        return render(request, 'polls/home.html',context)



class ResultAPIView(APIView):
    
    authentication_classes = []
    permission_classes = []

    def get(self, request): 
        data = request.session.get('result')
        return Response(data)

def result_detail(request):

    context = {}
    return render(request, 'polls/chart.html', context )



class DataListAPI(APIView):
    def get(self, request):
        queryset = Data.objects.all()
        print(queryset)
        serializer = DataSerializer(queryset, many=True)
        return Response(serializer.data)

class ProductListAPI(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        print(queryset)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# ...

def post_new(request):
    boards = Post.objects.all()
    context = {'object_list': boards}    
    return render(request, 'polls/head.html', context)

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'polls/data_list.html', {'posts': posts})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))




def indextest(request):
    return render(request, 'polls/indextest.html', {'title':'data'})

def home(request):
    return render(request, 'polls/home.html', {'title':'home'})    

def board(request):
    return render(request, 'polls/board.html', {'title':'board'})    




class CategoryView(View):
    template_name = 'polls/category.html'

    def get(self, request):
        context = {
            'categories': Category.objects.all(),
        }
        return render(request, self.template_name, context)