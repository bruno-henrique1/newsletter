from django.shortcuts import render

# Create your views here.

def pess (request):
    contexte_pess = {
        'text': 'Página do pess',
        'title':"pagina do pess",
        'post_pess':'agr é pesss',
}
    return render(request,'pess/pess.html',contexte_pess)