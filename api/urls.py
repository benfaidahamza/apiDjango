from django.urls import path
from . import views


urlpatterns=[
   path('',views.ListStudents, name='List-students'),
   path('add/',views.addStudent,name='add-students'),
   path('students/<int:student_id>/', views.GetStudent, name='get-student'),
   path('students/first/', views.GetStudentsByFirstName, name='get-students-by-firstname'),
   path('students/last/', views.GetStudentsByLastName, name='get-students-by-lastname'),
   path('students/roll_number/<int:roll_number>/', views.GetStudentByRollNumber, name='get-student-by-roll-number'),
   path('students/delete/<int:student_id>/', views.DeleteStudent, name='delete_student'),
   path('students/update/<int:student_id>/', views.UpdateStudent, name='update_student'),
]