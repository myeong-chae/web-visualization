from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.ChartView.as_view(),name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('grid/', views.Home.as_view(), name='grid'),
    path('api/predict/', views.KospiPredictAPIView.as_view(), name="predict_kospi_api"),
    path('chart', views.index, name="chart"),
    path('SQL', views.SQLView.as_view(), name="SQL"),
]