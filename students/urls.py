from django.urls import path
from .views import (
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView
)

urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('<uuid:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('new/', StudentCreateView.as_view(), name='student-create'),
    path('<uuid:pk>/edit/', StudentUpdateView.as_view(), name='student-update'),
    path('<uuid:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
]


