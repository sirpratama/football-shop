from django.forms import ModelForm
from main.models import FootballItem

class FootballItemForm(ModelForm):
    class Meta:
        model = FootballItem
        fields = ["name", "price", "description", "thumbnail", "category", "is_featured", "brand", "stock", "size"]