from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import UserCreationForm
from .models import User

class CreateUser(TemplateView):
    template_name="cadastro.html"
    form_class = UserCreationForm

    def post(self, request):
        data = {}
        data["email"] = request.POST ["email"]
        data["first_name"] = request.POST["first_name"]
        data["last_name"] = request.POST["last_name"]
        data["password"] = request.POST["password"]

        user = User.objects.create(
            email=data["email"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            password=data["password"],
        )

        data["user_obj"]=user_obj

        return render(request, "cadastro.html")