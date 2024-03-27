from django.shortcuts import render

# Create your views here.

def index (request):
    contexte_contact = {
        'text': 'Página do contact',
        'title':"pagina do contact",
        'post_contact':'agr é contact',
}
    return render(request,'contact/index.html',contexte_contact)