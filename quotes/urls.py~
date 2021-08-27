from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from user import views as user_views
from .views import HomeView, QuoteView, AddQuoteView, MyQuote, UpdateQuoteView, DeleteQuoteView, LikeView, HomeLikeView, ProfileView

urlpatterns = [
        path('', HomeView.as_view(), name='home'),
        path('quote/<int:pk>/', QuoteView.as_view(), name='quote'),
        path('add/', AddQuoteView.as_view(), name='add_quote'),
        path('quote/update/<int:pk>/', UpdateQuoteView.as_view(), name='update_quote'),
        path('quote/delete/<int:pk>/' ,DeleteQuoteView.as_view(), name='delete_quote'),
        path('my_quote/', MyQuote.as_view(), name='my_quote'),
        path('like/<int:pk>/', LikeView, name='like_quote'),
        path('home/like/<int:pk>/', HomeLikeView, name='home_like'),
        path('author/<int:pk>/', ProfileView.as_view(), name='profile'),
        path('about/', TemplateView.as_view(template_name="quote/about.html")),
]
