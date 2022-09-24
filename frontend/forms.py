from django import forms

from backend.models import User


class RegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=255, required=True)
    phone_number = forms.CharField(max_length=255, required=True)
    password = forms.CharField(max_length=255, required=True)
    confirm_password = forms.CharField(max_length=255, required=True)
    confirmation = forms.BooleanField(required=True)

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            self.add_error('password', 'Parol va tasdiqlash mos kelmayapti')

        if User.objects.filter(phone_number=self.cleaned_data.get(
           'phone_number', 'None').removeprefix('+')):
            self.add_error('phone_number', 'Bunday telefon raqami mavjud')
