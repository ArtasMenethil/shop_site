from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('tarrifs/', views.tarrifsPage, name='tarrifs'),
    path('course/<slug>', views.CourseDetailPage.as_view(), name='course_detail'),
    path('course/<slug>/<lesson_slug>', views.LessonDetailPage.as_view(), name='lesson_detail'),
    path('add/add_course', views.CourseAdd.as_view(), name='add_course'),
]