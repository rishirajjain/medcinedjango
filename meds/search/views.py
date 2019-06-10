from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from search.documents import PostDocument
from elasticsearch_dsl import Q
def search(request):

    q = request.GET.get('q')
    s=q.replace(" ","&")
    if q:
        posts = PostDocument.search().query('bool', must=[Q('match', details=s)])
        posts = posts.highlight_options(pre_tags=["<b>"],post_tags=["</b>"],order='score')
        posts = posts.highlight('details')
        response = posts.execute()               
    else:
        posts = ''
        
    f=response.hits.total 
   
    return render(request, 'search.html', {'posts': posts,'f':f})