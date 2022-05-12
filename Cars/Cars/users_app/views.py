from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.urls import reverse_lazy
from django.views import generic as views
from Cars.cars_rest.models import UserCar, CarModel, CarBrand
from Cars.users_app.models import CustomCarUser
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import mixins as auth_mixin
from django.contrib.auth import forms as auth_forms



class MyLoginView(LoginView,auth_mixin.LoginRequiredMixin):
    template_name = 'index.html'
    def get_success_url(self):
        return reverse_lazy('main')





class LogoutPageView(LogoutView):
    """ by pressing logout, redirect to fitst page"""
    def get_success_url(self):
        return reverse_lazy('index')



class CreateNewUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = CustomCarUser
        fields = ('username','password1', 'password2','first_name',
                  'last_name','hometown','data_birth','picture' )
        widgets = {
            'data_birth': DatePickerInput,

        }




class RegistrationView(views.CreateView):
    form_class = CreateNewUserForm
    template_name = 'registration.html'
    success_url = reverse_lazy('loginJ')




class MainPageView(views.TemplateView, auth_mixin.LoginRequiredMixin):

    """ overwrite dispatch for is_deleted users not permission"""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.is_deleted:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = UserCar.objects.all()
        context['models'] = CarModel.objects.all()
        context['brands'] = CarBrand.objects.all()
        context['users'] = CustomCarUser.objects.all()
        return context
    template_name = 'login.html'