from django.shortcuts import render

# Create your views here.
from Book.models import Books


def view_all_books(request):
    print("User details: "+request.user)
    objs = Books.objects.all()

    print(objs)
    context = {
        'books': objs
    }
    return render(request,'view_all_books.html', context=context)


def view_single_book(request, book_id):
    obj = Books.object.filter(id=book_id)

    context = {
        'book': obj
    }
    return render(request,'view_single_book.html', context=context)
