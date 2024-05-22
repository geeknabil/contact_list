from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, PhoneNumber
from .forms import ContactForm, PhoneNumberFormSet

def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        formset = PhoneNumberFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            contact = form.save()
            phone_numbers = formset.save(commit=False)
            for phone_number in phone_numbers:
                phone_number.contact = contact
                phone_number.save()
            return redirect('list_contacts')
    else:
        form = ContactForm()
        formset = PhoneNumberFormSet()
    return render(request, 'contacts/add_contact.html', {'form': form, 'formset': formset})

def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/list_contacts.html', {'contacts': contacts})

def contact_details(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    phone_numbers = contact.phone_numbers.all()
    return render(request, 'contacts/contact_details.html', {'contact': contact, 'phone_numbers': phone_numbers})
