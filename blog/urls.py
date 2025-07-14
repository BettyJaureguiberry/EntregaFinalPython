from django.urls import path, include
from django.contrib import admin
from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView


from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('pages/', PageListView.as_view(), name='pages_list'),
    path('crear/', PageCreateView.as_view(), name='page_create'),
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('<int:pk>/editar/', PageUpdateView.as_view(), name='page_update'),
    path('<int:pk>/borrar/', PageDeleteView.as_view(), name='page_delete'),
    path('accounts/', include('accounts.urls')),
]