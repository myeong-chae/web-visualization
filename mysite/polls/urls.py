from django.urls import path
from .views import ProductListAPI, DataListAPI, ContactFormView
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('api/product/', ProductListAPI.as_view()),
    path('api/', DataListAPI.as_view()),
    path('api/result/', views.ResultAPIView.as_view(), name="result_api"),
    path('result/', views.result_detail, name='result_detail'),
    path('api/predict/', views.KospiPredictAPIView.as_view(), name="predict_kospi_api"),
    path('chart', views.ChartView.as_view(), name="chart"),
    path('post', views.post_list, name="post"),
    path('post/new', views.post_new, name="post_new"),
    path('form', ContactFormView.as_view(), name="contact"),
    path('test', views.indextest, name='indextest'),
    path('board/', views.board, name='board'),
    path('home/', views.home, name='home'),
]