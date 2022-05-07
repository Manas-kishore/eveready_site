from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        messege = request.POST.get('messege')


        data = {
                'name': name,
                'email': email,
                'phone': phone,
                'messege': messege
        }
        messege = '''
        New Messege: {}

        From: {}
        '''.format(data['messege'], data['email'])
        send_mail('msenterprises(eveready)', messege, '', ['msenterprises7143@gmail.com'])

        messages.success(request, 'Your Message Has Been Sent!')


    return render(request, 'contact.html')

def product(request):
    return render(request, 'product.html')



