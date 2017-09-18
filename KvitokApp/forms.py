from django import forms
from KvitokApp.models import ZapisTable

kvitki = ZapisTable.objects.all()
how_objects = len(kvitki)
last_object = kvitki[how_objects - 1]
last_name_akt = last_object.number_akt + 1

class KvitokAddForm(forms.ModelForm):
    akt_num = forms.IntegerField(label='Акт№', initial=last_name_akt)
    class Meta:
        model = ZapisTable
        exclude = ('date', 'number_akt')