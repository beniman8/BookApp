from django.shortcuts import render,get_object_or_404
from .models import Book,Chapter
from django.http import Http404


def book_list(request):
    queryset=Book.objects.all()

    context ={
        'queryset':queryset
    }

    return render(request,"book_list.html",context)


def book_detail(request,slug):
    book = get_object_or_404(Book,slug=slug)
    context ={
        'book':book
    }
    return render(request,"book_detail.html",context)

def chapter_detail(request,book_slug,chapter_number):
    chapter = Chapter.objects.filter(book__slug=book_slug).filter(chapter_number=chapter_number)
    if chapter.exists():
        context ={
            'chapter':chapter[0]
        }
        return render(request,"chapter_detail.html",context)
    return Http404


