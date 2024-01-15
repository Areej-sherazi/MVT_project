

# urls.py
from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
   path('add/', views.student, name='myapp-views-student'),
   path('list/', views.list, name='myapp-views-list'),
   path('student/<int:id>/', views.detail, name='myapp-views-detail'),
   path('student-delete/<int:id>/', views.delete, name='myapp-views-delete'),
   path('student-update/<int:id>/', views.update, name='myapp-views-update')




]
