from django.forms import ModelForm
from .models import Todo

# custome form just to crate the todoo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']
