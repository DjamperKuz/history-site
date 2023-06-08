from django.urls import path
from . import views
from .views import RegisterUser

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('text_1/', views.text_1, name='text_1'),
    path('text_2/', views.text_2, name='text_2'),
    path('text_3/', views.text_3, name='text_3'),
    path('subject_<int:topic_id>/', views.subject, name='subject'),
    path('result/<int:topic_id>/', views.result_page, name='result_page'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('results/', views.all_results, name='all_results'),
    path('about_us/', views.about_us, name='about_us'),
]