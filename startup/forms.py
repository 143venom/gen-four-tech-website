from django import forms

class ContactForm(forms.Form):
  name = forms.CharField(max_length=255)
  email = forms.EmailField()
  subject = forms.CharField()
  message = forms.CharField(widget=forms.Textarea)



SERVICE_CHOICES = [
  ('Web Design', 'Web Design'),
  ('Web Development', 'Web Development'),
  ('Digital Marketing', 'Digital Marketing'),
  ('Email Marketing', 'Email Marketing'),
]

class QuoteForm(forms.Form):
  name = forms.CharField(max_length=255)
  email = forms.EmailField()
  service = forms.ChoiceField(choices=SERVICE_CHOICES)
  message = forms.CharField(widget=forms.Textarea)