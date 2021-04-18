from django import forms
from .models import Post, Comment


class CreatePostForm(forms.ModelForm):

    class Meta :
        model = Post        

        fields = [            
        "title",
        "body",
        "image",
        ]

    class Meta:
        model = Post
        fields = ["title", "body", "image"]
        
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

class CreateCommentForm(forms.ModelForm):
    class Meta :
        model = Comment           

        fields = ["body"]

        widgets = {"body": forms.TextInput({"class": "form-control comentbar", "rows": 6})}
        labels = {"body": "Digite aqui seu comentário"}