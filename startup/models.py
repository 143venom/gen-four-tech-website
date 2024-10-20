from django.db import models
import datetime

# Create your models here.

class Slider(models.Model):
  title = models.CharField(max_length=120)
  subtitle = models.CharField(max_length=200)
  image = models.ImageField(upload_to='slider_images')
  uploaded_on = models.DateTimeField(default=datetime.datetime.now)

  def __str__(self):
      return self.title
  

class Quality(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class About(models.Model):
  title =  models.CharField(max_length=200)
  description =  models.TextField()
  qualities = models.ManyToManyField(Quality, related_name='qualities')
  phone = models.CharField(max_length=20)
  image = models.ImageField(default="default.jpg", upload_to='about_pic')

  def __str__(self):
    return self.title
  
  
class Quote(models.Model):
  description = models.TextField()
  phone = models.CharField(max_length=20)


class Feature(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  image = models.ImageField(default="default.jpg", upload_to='feature_pics')


  def __str__(self):
    return self.title
  
class FeaturePage(models.Model):
  image = models.ImageField(default="default.jpg", upload_to='feature_pics')


class Team(models.Model):
  name = models.CharField(max_length=120)
  designation = models.CharField(max_length=120)
  image = models.ImageField(default="default.jpg", upload_to='team_pics')
  twitter_link = models.URLField(blank=True, null=True)
  facebook_link = models.URLField(blank=True, null=True)
  instagram_link = models.URLField(blank=True, null=True)
  linkedin_link = models.URLField(blank=True, null=True)
  
  def __str__(self):
      return self.name
  


class Service(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  image = models.ImageField(default="default.jpg", upload_to='service_pics')
  
  def __str__(self):
      return self.title
  

class Testimonial(models.Model):
  client_name = models.CharField(max_length=120)
  profession = models.CharField(max_length=200)
  description = models.TextField()
  image = models.ImageField(default="default.jpg", upload_to='testimonial_pics')
  
  def __str__(self):
      return self.client_name
  

class Subscription(models.Model):
  email = models.EmailField()
  subscribed_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.email


class Technology(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Price(models.Model):
  TIME_DURATION_CHOICES = [
        ('MONTH', 'Month'),
        ('YEAR', 'Year'),
    ]
  
  plan = models.CharField(max_length=200)
  business_type = models.CharField(max_length=200)
  technology_need = models.ManyToManyField(Technology, related_name='needed_in_plans')
  technology_noneed = models.ManyToManyField(Technology, related_name='not_needed_in_plans', blank=True)
  price = models.DecimalField(max_digits=5, decimal_places=2)
  time_duration = models.CharField(max_length=5, choices=TIME_DURATION_CHOICES, default='MONTH')
  
  def __str__(self):
      return self.plan
  

class VendorImage(models.Model):
  vendor_name = models.CharField(max_length=200)
  logo = models.ImageField(default="defaultvendor.jpg", upload_to='vendor_pics')

  def __str__(self):
      return self.vendor_name
  

class CompanyLogo(models.Model):
  name = models.CharField(max_length=200)
  logo = models.ImageField(default="defaultvendor.jpg", upload_to='company_logo')

  def __str__(self):
      return self.name
      
      
class SiteContent(models.Model):
  email = models.EmailField()
  phone = models.CharField(max_length=20)
  company_address = models.CharField(max_length=150)

  def __str__(self):
      return 'Site Settings'
  


  