from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
        # widgets = {
        #     "title": forms.TextInput(attrs={"class": "form-control"}),
        #     "details": forms.Textarea(attrs={"class": "form-control"}),
        # }