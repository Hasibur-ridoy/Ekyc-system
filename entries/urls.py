from django.urls import path
from . import views

urlpatterns = [

    path('create_entry/', views.createEntry, name='create_entry'),
    path('update_entry/', views.updateEntry, name='update_entry'),
    path('delete_entry/', views.deleteEntry, name='delete_entry'),
    path('student_entry/update_personal_info/', views.updatePersonalInfo, name='update_personal_info'),
    path('student_entry/update_aca_hsc_equiv_info/', views.updateHSCEquivInfo, name='update_aca_hsc_equiv_info'),
    path('student_entry/update_aca_ssc_equiv_info/', views.updateSSCEquivInfo, name='update_aca_ssc_equiv_info'),
    path('student_entry/update_financial_info/', views.updateFinancialInfo, name='update_financial_info'),
    path('student_entry/edit_grade/', views.editGrade, name='edit_grade'),
    path('student_entry/delete_grade/', views.deleteGrade, name='delete_grade'),
    path('', views.StudentList, name='StudentList'),
    path('student_entry/', views.studentEntry, name='student_entry'),
    path('assign_grade/', views.assignGrade, name='assign_grade'),
]