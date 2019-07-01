from django.shortcuts import render
from django.shortcuts import render
from search.documents import PostDocument
from elasticsearch_dsl import Q
def search(request):

    q = request.GET.get('q')
    s=q.split(",")
    a= "Q('match', med_details='{}')".format(s[0])
    i=1
    while i<len(s):
        a+='&Q(\'match\', med_details=\'{}\')'.format(s[i])
        i+=1
        
    if q:
        posts = PostDocument.search().query('bool', must=[eval(a)])        
        posts = posts.highlight_options(pre_tags=["<span class=\"result\">"],post_tags=["</span>"],order='score',fragment_size=1000)
        posts = posts.highlight('med_details')
        response = posts.execute()               
    else:
        posts = ''
    posts=posts[0:10000]    
    f=response.hits.total 
   
    return render(request, 'search.html', {'posts': posts,'f':f})

