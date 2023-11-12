from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "users/register.html"
    success_url = "/login/"

class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "users/login.html"

    def get_success_url(self):
        return reverse("books:book_list")

class PostView(ListView):
    queryset = User.objects.all()
    template_name = "users/post.html"

    def get_queryset(self):
        return User.objects.all()

class AuthLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")