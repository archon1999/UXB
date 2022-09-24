import os
import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from payments.models import PaymentStatus
from django.http.response import HttpResponseRedirect
from django.utils import translation

from backend.models import User, IndividualRequest, EntityRequest, Payment
from .forms import RegistrationForm


class HomeView(View):
    template_name = 'index.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name, {**kwargs})


class RegistrationView(View):
    template_name = 'registration.html'

    def get(self, request):
        return render(request, self.template_name, {
            'payment_value': os.getenv('REGISTRATION_PAYMENT_VALUE')
        })

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            if len(full_name.split()) == 1:
                first_name = full_name
                last_name = ''
            else:
                first_name, last_name = full_name.split(maxsplit=1)

            phone_number = form.cleaned_data['phone_number'].removeprefix('+')
            user = User.users.create_user(
                username=form.cleaned_data['phone_number'],
                phone_number=phone_number,
                password=form.cleaned_data['password'],
                first_name=first_name,
                last_name=last_name,
            )
            payment_value = int(os.getenv('REGISTRATION_PAYMENT_VALUE'))
            payment = Payment.objects.create(
                variant='',
                currency='UZS',
                total=payment_value,
                user=user,
            )
            return redirect('request_payment', payment_id=payment.id)

        else:
            return render(request, self.template_name, {
                'form': form,
                'payment_value': os.getenv('REGISTRATION_PAYMENT_VALUE')
            })


class RequestIndividual(View):
    def post(self, request):
        key = request.POST['key']
        if not User.users.filter(key=key).exists():
            return HomeView().get(request, key_error=True)

        user = User.users.get(key=key)
        year, month, day = map(int, request.POST['birth_day'].split('-'))
        birth_day = datetime.date(year, month, day)
        individual_request = IndividualRequest.objects.create(
            user=user,
            full_name=request.POST['full_name'],
            birth_day=birth_day,
            phone_number=request.POST['phone_number'],
            region=request.POST['region'],
            city=request.POST['city'],
            street=request.POST['street'],
            street_number=request.POST['street_number'],
            debt_value=request.POST['debt_value'],
            term=request.POST['term'],
            created_workplace=request.POST.get('created_workplace', 0) or 0,
            proposition=request.POST['proposition'],
        )
        payment_value = int(os.getenv('REQUEST_PAYMENT_VALUE'))
        payment = Payment.objects.create(
            variant='',
            currency='UZS',
            total=payment_value,
            individual_request=individual_request,
        )
        return redirect('request_payment', payment_id=payment.id)


class RequestEntity(View):
    def post(self, request):
        key = request.POST['key']
        if not User.users.filter(key=key).exists():
            return HomeView().get(request, key_error=True)

        user = User.users.get(key=key)
        entity_request = EntityRequest.objects.create(
            user=user,
            company_name=request.POST['company_name'],
            address=request.POST['address'],
            MFO=request.POST['MFO'],
            INN=request.POST['INN'],
            phone_number=request.POST['phone_number'],
            account_number=request.POST['account_number'],
            debt_value=request.POST['debt_value'],
            term=request.POST['term'],
            created_workplace=request.POST['created_workplace'],
            proposition=request.POST['proposition'],
        )
        payment_value = int(os.getenv('REQUEST_PAYMENT_VALUE'))
        payment = Payment.objects.create(
            variant='',
            currency='UZS',
            total=payment_value,
            entity_request=entity_request,
        )
        return redirect('request_payment', payment_id=payment.id)


class RequestPaymentView(View):
    template_name = 'request_payment.html'

    def get(self, request, payment_id):
        payment = get_object_or_404(Payment, id=payment_id)
        if payment.user:
            payment_value = int(os.getenv('REGISTRATION_PAYMENT_VALUE'))
        else:
            payment_value = int(os.getenv('REQUEST_PAYMENT_VALUE'))

        return render(request, self.template_name, {
            'payment_value': payment_value,
            'PaymentStatus': PaymentStatus,
            'payment': payment,
        })


class ContactView(View):
    template_name = 'contact.html'

    def get(self, request):
        return render(request, self.template_name, {})


class IndividualsView(View):
    template_name = 'individuals.html'

    def get(self, request):
        return render(request, self.template_name, {})


class EntitiesView(View):
    template_name = 'entities.html'

    def get(self, request):
        return render(request, self.template_name, {})


class ForBuildingsView(View):
    template_name = 'for_buildings.html'

    def get(self, request):
        return render(request, self.template_name, {})


class ForInstrumentsView(View):
    template_name = 'for_instruments.html'

    def get(self, request):
        return render(request, self.template_name, {})


class ForStructuresView(View):
    template_name = 'for_structures.html'

    def get(self, request):
        return render(request, self.template_name, {})


class ForAgriculturalMachineryView(View):
    template_name = 'for_agricultural_machinery.html'

    def get(self, request):
        return render(request, self.template_name, {})


class ForGetCarView(View):
    template_name = 'for_get_car.html'

    def get(self, request):
        return render(request, self.template_name, {})


class ForHousingView(View):
    template_name = 'for_housing.html'

    def get(self, request):
        return render(request, self.template_name, {})


class ForLandView(View):
    template_name = 'for_land.html'

    def get(self, request):
        return render(request, self.template_name, {})


class ForTaxiView(View):
    template_name = 'for_taxi.html'

    def get(self, request):
        return render(request, self.template_name, {})


class ForStudentsView(View):
    template_name = 'for_students.html'

    def get(self, request):
        return render(request, self.template_name, {})


class SetLanguageView(View):
    def get(self, request, language):
        translation.activate(language)
        response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        response.set_cookie('django_language', language)
        return response
