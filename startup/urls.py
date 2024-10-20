from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('about', views.about, name="about"),
  path('service', views.service, name="service"),
  path('quote', views.quote, name="quote"),
  path('price', views.price_plan, name="price"),
  path('testimonial', views.testimonial, name="testimonial"),
  path('team', views.team, name="team"),
  path('feature', views.feature, name="feature"),
  path('contact', views.contact, name="contact"),
  path('subscribed', views.newsletter_subscribe, name="subscribe"),
]