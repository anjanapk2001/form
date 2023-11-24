from django.urls import path
from.import views
urlpatterns = [
    path('',views.demo,name="demo"),
    path('login/',views.login,name="login"),
    path('success/',views.success,name='success'),
    path('register/',views.register,name='register'),
    path('student-form/',views.student_form,name='student_form'),
    path('get-courses/',views.get_courses,name='get_courses'),
    path('logout/',views.logout,name='logout'),





]