from django.shortcuts import render
# Create your views here.

def home (request):
    contexte = {
        'text': 'Página do home',
        'title':"home",
        'post_home':'tem que aparecer por ultimo no home'
}

    print('Home')
    return render(request,'home/home.html',contexte)

