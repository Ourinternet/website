from django import forms
from captcha.fields import ReCaptchaField


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField(label="Your Email")
    cc_myself = forms.BooleanField(required=False, label="CC Your Email")
    message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField(attrs={'theme': 'white'})