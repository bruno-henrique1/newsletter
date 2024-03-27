from blog.data import posts
from django.shortcuts import render
from typing import Any
from django.http import HttpResponse, Http404
# Create your views here.

def blog (request):
    print('blog')
    
    contexte_blog = {
        'text': 'Página do blog',
        'title':'blog',
        'posts': posts
}
    return render(request,'blog/blog.html', contexte_blog)

def post (request:HttpResponse,post_id:int):
    found_post: dict[str,Any] | None = None 
    
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise HttpResponse ('Essa página não existe vc digitou letras')
    

    contexte_blog = {
        'title': found_post['title'] + '-',
        'post': found_post
}
    return render(request,'blog/post.html', contexte_blog)

def carrinho(request):
    print('exemplo')
    contexte_carrinho = {
        'text': 'Página do carrinho',
        'title':'shosp'
}
    return render(request,'blog/shop.html',contexte_carrinho)