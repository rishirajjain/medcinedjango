from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from search.documents import PostDocument

def search(request):

    q = request.GET.get('q')

    if q:
        posts = PostDocument.search().query("match", medDetails=q)
    else:
        posts = ''

    return render(request, 'search.html', {'posts': posts})