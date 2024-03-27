from django import forms;
from . import models;

class ReviewForm(forms.ModelForm) :
    class Meta :
        model = models.Review;
        fields = "__all__"
        widgets = {
            "review": forms.Textarea(attrs={"row": 3})
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['book'] = forms.ModelChoiceField(queryset=models.Booko.objects.all())