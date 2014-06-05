from django import forms
from simplemathcaptcha.fields import MathCaptchaField


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField(label="Your Email")
    cc_myself = forms.BooleanField(required=False, label="CC Your Email")
    message = forms.CharField(widget=forms.Textarea)
    name = forms.CharField(max_length=100, widget=forms.HiddenInput,
                           required=False)
    captcha = MathCaptchaField()

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get("name")

        if name:
            raise forms.ValidationError("Name field should not be filled out.")

        return cleaned_data

