
from django.urls import path
from comic import views
urlpatterns = [
    path('', views.comic_index, name='comic_index'),
    path('<int:chapter>/<int:number>/', views.display_detail, name='chapter_detail')
]
