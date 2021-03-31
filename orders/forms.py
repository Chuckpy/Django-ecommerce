from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, Layout, Submit
from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "cpf",
            "name",
            "email",
            "postal_code",
            "address",
            "number",
            "complement",
            "district",
            "state",
            "city",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = "."
        self.helper.add_input(
            Submit(
                "submit",
                "Finalizar compra",
                css_class="btn btn-success btn-lg btn-block",
            )
        )
        self.helper.layout = Layout(
            Fieldset(
                "",
                "cpf",
                "name",
                "email",
                Div(
                    Field("postal_code", onchange="getAddress()", wrapper_class="col"),
                    Field("state", wrapper_class="col"),
                    Field("city", wrapper_class="col"),
                    css_class="row",
                ),
                Div(
                    Field("address", wrapper_class="col"),
                    Field("district", wrapper_class="col"),
                    css_class="row",
                ),
                Div(
                    Field("number", wrapper_class="col"),
                    Field("complement", wrapper_class="col"),
                    css_class="row",
                ),
                css_class="border-bottom mb-3",
            )
        )