from django.shortcuts import render #type: ignore
from contact.models import Contact

# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    
    context = {
        'contacts': contacts
    }
    
    return render(
        request,
        'contact/index.html',
        context
    )