from django.shortcuts import render #type: ignore
from contact.models import Contact
from django.http import Http404
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    #contacts = Contact.objects.all().order_by('-id')
    contacts = Contact.objects\
    .filter(show=True)\
    .order_by('-id')[:10]
    print(contacts.query)
    
    context = {
        'contacts': contacts
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
    context = {
        'contact': single_contact,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )