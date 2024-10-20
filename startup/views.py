from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages

from .forms import ContactForm, QuoteForm
from .models import *
from blog.models import Blog

# Create your views here.

def get_context(*args):
  context = {}
  if 'about' in args:
    context['about'] = About.objects.first()
  if 'teams' in args:
    context['teams'] = Team.objects.all()
  if 'services' in args:
    context['services'] = Service.objects.all()
  if 'testimonials' in args:
    context['testimonials'] = Testimonial.objects.all()
  if 'features' in args:
    context['features'] = Feature.objects.all()
  if 'feature_img' in args:
    context['feature_img'] = FeaturePage.objects.first()
  if 'prices' in args:
    context['prices'] = Price.objects.all()
  if 'quote' in args:
    context['quote'] = Quote.objects.first()
  if 'sliders' in args:
    context['sliders'] = Slider.objects.order_by('uploaded_on')
  if 'blogs' in args:
    context['blogs'] = Blog.objects.order_by('-created_on')
  return context
  

def home(request):
  context = get_context(
    'about', 'teams', 'services', 'testimonials', 'features', 'feature_img', 
    'prices', 'quote', 'sliders', 'blogs')
  return render(request, "index.html", context)
  

def about(request):
  context = get_context('about', 'teams')
  return render(request, "about.html", context)
  

def service(request):
  context = get_context('services', 'testimonials')
  return render(request, "service.html", context)


def price_plan(request):
  context = get_context('prices')
  return render(request, "price.html", context)


def team(request):
  context = get_context('teams')
  return render(request, "team.html", context)


def feature(request):
  context = get_context('features', 'feature_img')
  return render(request, "feature.html", context)


def testimonial(request):
  context = get_context('testimonials')
  return render(request, "testimonial.html", context)


def contact(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data["name"]
      email = form.cleaned_data["email"]
      subject = form.cleaned_data["subject"]
      message = form.cleaned_data["message"]

      html_content = render_to_string(
                "emails/emaildisplay.html",
                {
                    "name": name,
                    "email": email,
                    "subject": subject,
                    "message": message,
                },
            )

      send_mail("You got a mail!", message, email, ['info@genfourtech.com'], html_message=html_content, fail_silently=False)
    
      return redirect("contact")
  else:
    form = ContactForm()
  return render(request, 'contact.html', {'form': form})



def quote(request):
  quote = Quote.objects.first()

  if request.method == "POST":
    form = QuoteForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data["name"]
      email = form.cleaned_data["email"]
      service = form.cleaned_data["service"]
      message = form.cleaned_data["message"]

      html_content = render_to_string(
                "emails/quote_email.html",
                {
                    "name": name,
                    "email": email,
                    "service": service,
                    "message": message,
                },
            )

      send_mail("You got a mail for a Quote!", message, email, ['info@genfourtech.com'], html_message=html_content, fail_silently=False)
    
      return redirect("quote")
  else:
    form = QuoteForm()
  return render(request, 'quote.html', {'form': form, 'quote': quote})


def newsletter_subscribe(request):
  if request.method == "POST":
      email = request.POST["email"].strip()
      
      if email:
        if Subscription.objects.filter(email=email).exists():
          messages.error(request, "Email is already in use. Please choose a different one.")
        
        else:
          Subscription.objects.create(email=email)
          messages.success(request, "You have successfully subscribed!")
          return redirect("home")
      else:
        return HttpResponse("Email field is required", status=400)
  return render(request, "base.html")






