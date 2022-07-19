from django import forms

from backend.models import User


class RegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    password = forms.CharField(max_length=255)
    confirm_password = forms.CharField(max_length=255)

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            self.add_error('password', 'Parol va tasdiqlash mos kelmayapti')

        if User.objects.filter(email=self.cleaned_data.get('email', 'None')):
            self.add_error('email', 'Bunday elektron manzil mavjud')
