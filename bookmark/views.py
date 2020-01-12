from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookmark
from .forms import BookmarkForm
# Create your views here.

def list(req):
    lists = Bookmark.objects.all()
    return render(req,'bookmark/list.html',{
        'list': lists,
    })

def new(req):
    if req.method == 'POST':
        form = BookmarkForm(req.POST)
        if form.is_valid():
            bookmark = Bookmark()
            bookmark.site_name = form.cleaned_data['site_name']
            bookmark.url = form.cleaned_data['url']
            bookmark.save()
            return redirect('bookmark:list')
    else:
        form = BookmarkForm()
    return render(req, 'bookmark/new.html',{
        'form': form,
    })

def edit(req, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    if req.method =='POST':
        form  = BookmarkForm(req.POST, instance=bookmark)
        if( form.is_valid()):
            bookmark.site_name = form.cleaned_data['site_name']
            bookmark.url = form.cleaned_data['url']
            bookmark.save()
            return redirect('bookmark:list')

    else:
        form = BookmarkForm(instance = bookmark)
    return render(req,'bookmark/edit.html',{
        'bookmark': bookmark,
        'form' : form,
    })

def delete(req,pk):
    bookmark = get_object_or_404(Bookmark,pk=pk)
    if req.method == 'POST':
        bookmark.delete()
        return redirect('bookmark:list')