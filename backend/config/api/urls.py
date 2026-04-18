from django.urls import path
from . import views

urlpatterns = [
    path('scrape/', views.scrape_books),
    path('books/', views.get_books),
    path('books/<int:id>/', views.get_book_detail),
    path('ask/', views.ask_question),
    path('recommend/', views.recommend_books),
]