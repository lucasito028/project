from django.shortcuts import render #type: ignore
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    #contacts = Contact.objects.all().order_by('-id')
    contacts = Contact.objects.filter(show=True).order_by('-id')

    
    paginator= Paginator(contacts, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'contacts': contacts,
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }
    
    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):
    #single_contact  = Contact.objects.get(pk=contact_id).first()
    
    single_contact = get_object_or_404(
        Contact.objects, pk=contact_id, show=True
    )
    
    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': site_title
    }

    return render(
        request,
        'contact/contact.html',
        context
    )
    
def search(request):
    #strip retira espaços do início e fim da string
    search_value = request.GET.get('q', '').strip()
    #print('search_value', search_value)
    #se não digitou nada, redireciona para a home
    #Q possibilita o uso do OU nas consultas SQL
    if search_value == '':
        return redirect('contact:index')
    contacts = Contact.objects.filter(show=True).filter(Q(first_name__icontains=search_value) | 
                                                        Q(last_name__icontains=search_value) | 
                                                        Q(email__icontains=search_value)).order_by('-id')


    paginator= Paginator(contacts, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    
    context = {
        'contacts': contacts,
        'page_obj': page_obj,
        'site_title': 'Search -'
    }
    
    return render(
        request,
        'contact/index.html',
        context
    )