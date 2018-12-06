from django.urls import path ,include
from . import views
urlpatterns = [
	path('profile',views.Student_profile,name="Student_profile"),
	path('courses/<slug:slug>',views.Student_courses,name="student_courses"),
	path('profile/grade-sheet',views.Student_grade_sheet,name="student_grades"),
    path('<slug:slug>',views.Student_profile),
    path('courses/your_course/<slug:slug>',views.Student_course_page,name="student_course_page"),
    path('courses/your_course/to-do-assignments/<slug:slug>',views.Student_assignment_list,name="student_course_page_assignments"),
]
