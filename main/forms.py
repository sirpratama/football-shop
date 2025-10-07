from django.forms import ModelForm
from main.models import FootballItem
from django.utils.html import strip_tags

class FootballItemForm(ModelForm):
    class Meta:
        model = FootballItem
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured", "brand", "stock", "size"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)