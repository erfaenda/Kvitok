from django import forms
from KvitokApp.models import ZapisTable

class KvitokAddForm(forms.ModelForm):
    class Meta:
        model = ZapisTable
        exclude = ('date',)