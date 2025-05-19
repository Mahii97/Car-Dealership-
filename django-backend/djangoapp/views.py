from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.conf import settings
import requests
from .models import CarMake, CarModel
from django.urls import reverse
import random
import string

def index(request):
    # Example: Fetch dealers from Express backend
    try:
        resp = requests.get('http://localhost:3000/dealers')
        dealers = resp.json()
    except Exception:
        dealers = []
    return render(request, 'index.html', {'dealers': dealers})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login_view(request):
    next_url = request.GET.get('next', reverse('index'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        from django.contrib.auth.models import User
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'No account found with this username. Please sign up first.')
            return render(request, 'login.html', {'next': next_url})
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html', {'next': next_url})

def logout_view(request):
    logout(request)
    return render(request, 'logout_alert.html')

def signup(request):
    from django.contrib.auth.models import User
    import random
    import string
    suggested_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # Password validation
        if len(password) < 8 or password.isalpha() or password.isdigit():
            messages.error(request, 'Password must be at least 8 characters and contain both letters and numbers.')
            return render(request, 'signup.html', {'suggested_password': suggested_password})
        # Check for unique password (no other user has this password)
        for user in User.objects.all():
            if user.check_password(password):
                messages.error(request, 'This password is already in use. Please choose a unique password.')
                return render(request, 'signup.html', {'suggested_password': suggested_password})
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            messages.success(request, 'Signed up successfully!')
            return redirect('index')
    return render(request, 'signup.html', {'suggested_password': suggested_password})

@login_required
def dealer_details(request, dealer_id):
    # Fetch dealer details and reviews from Express backend
    try:
        dealer_resp = requests.get(f'http://localhost:3000/dealers/{dealer_id}')
        dealer = dealer_resp.json()
    except Exception:
        dealer = None
    try:
        reviews_resp = requests.get(f'http://localhost:3000/reviews/{dealer_id}')
        reviews = reviews_resp.json()
    except Exception:
        reviews = []
    return render(request, 'dealer_details.html', {'dealer': dealer, 'reviews': reviews})

@login_required
def add_review(request, dealer_id):
    if request.method == 'POST':
        review = request.POST.get('review')
        reviewer = request.user.username
        # Here you would POST to Express backend (not implemented for dummy)
        # requests.post(f'http://localhost:3000/reviews/{dealer_id}', json={...})
        return redirect('dealer_details', dealer_id=dealer_id)
    return render(request, 'add_review.html', {'dealer_id': dealer_id})

def sentiment_analyzer(request):
    # Dummy sentiment analyzer endpoint
    text = request.GET.get('text', '')
    sentiment = 'positive' if 'good' in text.lower() else 'negative'
    return JsonResponse({'text': text, 'sentiment': sentiment})

def car_makes(request):
    car_makes = CarMake.objects.all()
    return render(request, 'car_makes.html', {'car_makes': car_makes})

def car_models(request):
    search_query = request.GET.get('search', '').strip()
    car_models = CarModel.objects.select_related('make').all()
    if search_query:
        car_models = car_models.filter(name__icontains=search_query)
    return render(request, 'car_models.html', {'car_models': car_models})
