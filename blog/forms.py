from django import forms
from .models import Post


class CreatePostForm(forms.ModelForm):
<<<<<<< HEAD
    class Meta :
        model = Post        

        fields = [            
        "title",
        "body",
        "image",
        ]
=======
    class Meta:
        model = Post
        fields = ["title", "body", "image"]
>>>>>>> 6a214b205146a312414758232b92226d7890f9a9
        widgets = {
            "title": forms.TextInput(
                {
                    "class": "form-control bform",
                    "placeholder": "O titulo da sua publicação",
                }
            ),
            "body": forms.TextInput({"class": "form-control bform", "rows": 3}),
            "image": forms.FileInput(
                {"class": "form-control-file bform", "accept": "image/*"}
            ),
        }

        labels = {
            "title": "Título ",
            "body": "Texto da publicação :",
            "image": "Insira aqui a imagem dessa publicação",
        }
