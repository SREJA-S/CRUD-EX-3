from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Book


# READ: Display all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


# CREATE: Add a new book
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        Book.objects.create(
            title=title,
            author=author,
            price=int(price)
        )
        return redirect('book_list')

    return render(request, 'books/add_book.html')


# UPDATE: Modify a book's price
def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.price = int(request.POST.get('price'))
        book.save()
        return redirect('book_list')

    return render(request, 'books/update_book.html', {'book': book})


# DELETE: Remove a book
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'books/delete_book.html', {'book': book})
