from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.
from contacts.models import Contacts
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contacts.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have Inquired already')
                return redirect('/listings/' + listing_id)


    contact = Contacts(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message,
                           user_id=user_id)
    contact.save()
    messages.success(request, 'Your request has been submited')
    return redirect('/listings/' +  listing_id)
