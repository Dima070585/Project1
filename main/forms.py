from ckeditor.widgets import CKEditorWidget
from django import forms
from main.models import Category, Post

class PostForms(forms.ModelForm):
    title = forms.CharField(label=False,widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'title'
    }))
    content = forms.CharField(widget=CKEditorWidget, label='')
    image = forms.FileField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ['title','content','image','category','prise']
