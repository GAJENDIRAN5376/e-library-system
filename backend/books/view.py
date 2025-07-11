from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book, BorrowRecord
from .serializers import BookSerializer, BorrowSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['POST'])
def borrow_book(request):
    user = request.user
    book_id = request.data.get('book_id')
    book = Book.objects.get(id=book_id)
    if not book.is_available:
        return Response({"error": "Book not available"}, status=400)
    book.is_available = False
    book.save()
    BorrowRecord.objects.create(user=user, book=book)
    return Response({"status": "borrowed"})

@api_view(['POST'])
def return_book(request):
    user = request.user
    book_id = request.data.get('book_id')
    record = BorrowRecord.objects.filter(user=user, book_id=book_id, returned_at__isnull=True).first()
if not record:
        return Response({"error": "Record not found"}, status=400)
    record.returned_at = timezone.now()
    record.save()
    book = record.book
    book.is_available = True
    book.save()
    return Response({"status": "returned"})
