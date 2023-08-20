from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.urls import reverse


def index(request):
    return render(request, 'bookClub/index.html')

def user_login(request):
    """
    Handle user login.

    If the request method is POST, this function attempts to authenticate the user
    using the provided username and password. If successful, the user is logged in
    and redirected to the 'currently_reading' view. If authentication fails, an error
    message is displayed on the login page.

    If the request method is not POST, the login page is displayed

    Parameters:
    request (HttpRequest): The request object

    Returns:
    HttpResponse: The response after handling the login attempt
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the desired account view or main page, index?
            return redirect('bookClub:index')
        else:
            error_message = 'Incorrect username or password'
            return render(request, 'bookClub/login.html', {'error_message': error_message})
    return render(request, 'bookClub/login.html')

def user_register(request):
    if request.method == 'POST':
        # Extract data from POST request
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')  # Add first name extraction

        # Validate the data
        if not username or not password or not email or not first_name:
            return render(request, 'bookClub/register.html', {'error_message': 'Please fill in all the required fields.'})

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return render(request, 'bookClub/register.html', {'error_message': 'Username already exists. Please choose a different one.'})
        
        # Check if the email is already taken
        if User.objects.filter(email=email).exists():
            return render(request, 'bookClub/register.html', {'error_message': 'Email already exists. Please choose a different one.'})

        # Create the new user object
        new_user = User(username=username, email=email, first_name=first_name)
        new_user.set_password(password)

        # Save the new user to the database
        new_user.save()

        # Authenticate the new user
        authenticated_user = authenticate(username=username, password=password)
        if authenticated_user:
            # Login the user after successful registration
            #login(request, authenticated_user)
            return redirect(reverse('bookClub:successful_reg'))

    return render(request, 'bookClub/register.html')

def successful_reg(request):
    return render(request, 'bookClub/successful_reg.html')

@login_required
def currently_reading(request):
    """
    Display the currently reading book for the logged-in user

    Retrieves information about the currently reading book and renders the
    'currently_reading.html' template

    Parameters:
    request (HttpRequest): The request object

    Returns:
    HttpResponse: The response containing the currently reading book information
    """
    currently_reading_book = {
        'title': 'Harry Potter and the Prisoner of Azkaban',
        'author': 'J. K. Rowling',
        'status': 'Currently Reading',
    }
    return render(request, 'bookClub/currently_reading.html', {'book': currently_reading_book})

@login_required
def next_read(request):
    """
    Display the next read book for the logged-in user

    Retrieves information about the next read book(s) and renders the
    'next_read.html' template

    Parameters:
    request (HttpRequest): The request object

    Returns:
    HttpResponse: The response containing the next read book information
    """
    # Logic to fetch and display the next read book(s) for the logged-in user
    next_read_book = {
        'title': 'Harry Potter and the Goblet of Fire',
        'author': 'J. K. Rowling',
        'status': 'Next Read',
    }
    return render(request, 'bookClub/next_read.html', {'book': next_read_book})

@login_required
def past_weeks(request):
    """
    Display the books read in previous months for the logged-in user

    Retrieves information about books read in previous months and renders the
    'past_weeks.html' template

    Parameters:
    request (HttpRequest): The request object

    Returns:
    HttpResponse: The response containing the past books information
    """
    # Logic to fetch and display the books read in previous months for the logged-in user
    past_books = [
        {
            'title': 'Harry Potter and the Sorcerers Stone',
            'author': 'J. K. Rowling',
            'status': 'read in June',
        },
        {
            'title': 'Harry Potter and the Chamber of Secrets',
            'author': 'J. K. Rowling',
            'status': 'read in July',
        },
    ]
    return render(request, 'bookClub/past_weeks.html', {'books': past_books})