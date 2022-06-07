from django.urls import path
from graphs import views

urlpatterns = [
    path('graphs/', views.graphs, name="graphs"),
    path('getExaExtGraphData/', views.getExaExtGraphData, name="getExaExtGraphData"),
    path('getICNEGraphData/', views.getICNEGraphData, name="getICNEGraphData"),
    path('getProcedenceGraphData/', views.getProcedenceGraphData, name="getProcedenceGraphData"),
    path('getSchoolProcedenceGraphData/', views.getSchoolProcedenceGraphData, name="getSchoolProcedenceGraphData"),
    path('getSchoolRegimeGraphData/', views.getSchoolRegimeGraphData, name="getSchoolRegimeGraphData"),
    path('getFailedSubjectsGraphData/', views.getFailedSubjectsGraphData, name="getFailedSubjectsGraphData"),
    path('getSchoolModalityGraphData/', views.getSchoolModalityGraphData, name="getSchoolModalityGraphData"),

]