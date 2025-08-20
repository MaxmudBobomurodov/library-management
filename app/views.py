from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect

from app.forms import BookForm
from app.models import BookModel


@login_required
@permission_required('library.view_book', raise_exception=True)
def book_list(request):
    book = BookModel.objects.all()
    return render(request, 'book_list.html', {'book': book})

@login_required
@permission_required('library.add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')

    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


@login_required
@permission_required('library.change_book', raise_exception=True)
def change_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')