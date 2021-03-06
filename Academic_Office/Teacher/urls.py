from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>',views.Teacher_Profile,name="T_profile"),
    path('students/<slug:slug>',views.Show_students,name="Show_students"),
    path('C_name/<slug:slug>',views.Course_contents,name="Course_contents"),
    path('C_name/books/upload/', views.upload_book, name='upload_book'),
    path('C_name/books-assignments/list/<slug:slug>', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),
    path('students/attendance/<slug:slug>',views.takeattendance,name='attendance'),
    path('grades/<slug:slug>',views.assignments,name='grades'),
    path('add-assignment/',views.add_assignment,name='add_assignment'),
    path('add-weightage/<slug:slug>',views.set_grading_policy,name='add_weightage'),
    path('Show_assignments/<slug:slug>',views.Show_assignments,name='Show_assignments'),
    path('add_marks/<slug:slug>',views.add_marks,name='add_mark'),
    path('add_final_grade/<slug:slug>',views.final_grade_policy,name='add_final_grade'),
    path('announcement/<slug:slug>',views.add_announcements,name='add_announcements'),
]
