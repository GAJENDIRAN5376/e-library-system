from django.urls import path
from .views import BookList, borrow_book, return_book
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('books/', BookList.as_view(), name='book-list'),
    path('borrow/', borrow_book, name='borrow'),
    path('return/', return_book, name='return'),
]
