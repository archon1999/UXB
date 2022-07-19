import datetime
from django.shortcuts import render
from django.views import View

from backend.models import User, IndividualRequest, EntityRequest
from .forms import RegistrationForm


class HomeView(View):
    template_name = 'index.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name, {**kwargs})


class RegistrationView(View):
    template_name = 'registration.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            if len(full_name.split()) == 1:
                first_name = full_name
                last_name = ''
            else:
                first_name, last_name = full_name.split(maxsplit=1)

            user = User.users.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=first_name,
                last_name=last_name,
            )
            subject = 'Saytdan ro`yhatdan o`tish'
            message = f'Kalit: {user.key}'
            user.email_user(subject, message)
            return render(request, self.template_name, {
                'registration_success': True
            })
        else:
            return render(request, self.template_name, {
                'form': form
            })


class RequestIndividual(View):
    def post(self, request):
        key = request.POST['key']
        if not User.users.filter(key=key).exists():
            return HomeView().get(request, key_error=True)

        user = User.users.get(key=key)
        year, month, day = map(int, request.POST['birth_day'].split('-'))
        birth_day = datetime.date(year, month, day)
        IndividualRequest.objects.create(
            user=user,
            full_name=request.POST['full_name'],
            birth_day=birth_day,
            region=request.POST['region'],
            city=request.POST['city'],
            street=request.POST['street'],
            street_number=request.POST['street_number'],
        )
        return HomeView().get(request, request_success=True)


class RequestEntity(View):
    def post(self, request):
        key = request.POST['key']
        if not User.users.filter(key=key).exists():
            return HomeView().get(request, key_error=True)

        user = User.users.get(key=key)
        EntityRequest.objects.create(
            user=user,
            company_name=request.POST['company_name'],
            address=request.POST['address'],
            MFO=request.POST['MFO'],
            INN=request.POST['INN'],
            phone_number=request.POST['phone_number'],
            account_number=request.POST['account_number'],
        )
        return HomeView().get(request, request_success=True)


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
