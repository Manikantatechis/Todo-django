from django.urls import URLPattern, path
from . import views
urlpatterns = [
    path('', views.todo, name='todo'),
    path('create/', views.create),
    path('update/<id>/', views.Update),
    path('delete/<id>/', views.delete),
    path('detail/<id>/', views.detail)

]