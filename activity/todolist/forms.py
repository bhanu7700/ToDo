from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content')
        
    


        # widgets = {
        #     'category' : Select(choices = choice_list),
        #     'auther' : forms.TextInput(attrs = {'value':'','id': 'elder','type':'hidden'})