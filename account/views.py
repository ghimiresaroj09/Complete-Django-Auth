# views.py
import random
import string
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')

def generate_random_password(length=8):
    """Generate a random password of specified length with letters and numbers only."""
    characters = string.ascii_letters + string.digits  # Letters and numbers only
    return ''.join(random.choice(characters) for _ in range(length))

def registerview(request):
    if request.method == 'POST':
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        address = request.POST['address']
        phone = request.POST['phone']
        birth = request.POST['birth']

        # Generate a random password
        password = generate_random_password()
        
        # Check if the user already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register')
        
        user = CustomUser(email=email, firstname=firstname, lastname=lastname, address=address, phone=phone, birth=birth)
        user.set_password(password)  # Set the random password
        user.password_changed = False  # Set to False as this is a temporary password
        user.save()

        # Send the generated password to the user's email
        send_mail(
            'Welcome to Our Site!',
            f'Your account has been created. Your temporary password is: {password}',
            'from@example.com',  # Change to your from email
            [email],
            fail_silently=False,
        )

        messages.success(request, "Registration successful! A temporary password has been sent to your email.")
        return redirect('login')
    
    return render(request, 'register.html')  # Use your actual registration template

def loginview(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Check if the user is logging in with the temporary password
            if not user.password_changed:  # If password hasn't been changed yet
                return redirect('change_password')  # Redirect to change password view
            return redirect('home')  # Redirect to home for normal login
        else:
            messages.error(request, "Invalid email or password")
            return redirect('login')
    
    return render(request, 'login.html')

def logoutview(request):
    logout(request)
    return redirect('login')

def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '')
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if request.user.password_changed == True:
            if not request.user.check_password(old_password):
                messages.error(request, "Old password is incorrect")
                return redirect('change_password')

        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('change_password')

        request.user.set_password(new_password)
        request.user.password_changed = True  # Set the flag to True
        request.user.save()

        # Log the user out after changing the password
        logout(request)

        messages.success(request, 'Your password has been changed successfully.')
        return redirect('login')

    return render(request, 'change_password.html',{'password_changed': request.user.password_changed})  # Use your actual change password template
