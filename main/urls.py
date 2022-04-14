from django.urls import path
from rest_framework import routers
from main import views


urlpatterns = []

urlpatterns += [
    path('category-list/', views.BookCategoryListView.as_view()),
    path('category-create/', views.BookCategoryCreatView.as_view()),
    path('category-list-create/', views.BookCategoryListCreateView.as_view()),
    path('category-retrieve/<int:pk>/', views.BookCategoryRetrivewView.as_view()),
    path('category-update/<int:pk>/', views.BookCategoryUpdateView.as_view()),
    path('category-retrieve-update/<int:pk>/', views.BookCategoryRetrieveUpdateView.as_view()),
    path('category-delete/<int:pk>/', views.BookCategoryDeleteView.as_view()),
]