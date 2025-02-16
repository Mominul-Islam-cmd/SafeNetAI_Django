from django.contrib import admin
from django.urls import path
from Researchers import views

app_name = 'Researchers'

urlpatterns = [
    path("info_form/", views.info_form, name='info_form'),
    path("reseachers_show/", views.researcher_view, name='researcher_view'),
    path("edit_info/<int:researcher_id>/", views.edit_info, name='edit_info'),
    path("recommend_form/", views.recommend_form, name='recommend_form'),
    path("research_student_recommendation_show/<int:researcher_id>/", views.research_student_recommendation_show, name='research_student_recommendation_show'),
    path("delete_info/<int:researcher_id>", views.delete_info, name='delete_info'),
]
