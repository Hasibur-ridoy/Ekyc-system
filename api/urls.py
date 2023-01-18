from django.urls import path


from . import views

urlpatterns = [
    path('',views.apiOverview,name='apiOverview'),
    path('api-student-info/',views.apiStudentview,name='apiStudentview'),
]