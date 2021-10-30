from django.urls import path
from core import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('list/', views.VacancyListView.as_view(), name='vacancy_list'),
    path('create/', views.VacancyCreateView.as_view(), name='vacancy_create'),
    path('detail/<int:pk>', views.VacancyDetailView.as_view(), name='vacancy_detail'),
    path('update/<int:pk>/', views.VacancyUpdateView.as_view(), name='vacancy_update'),
    path('delete/<int:pk>/', views.VacancyDeleteView.as_view(), name='vacancy_delete'),
]
