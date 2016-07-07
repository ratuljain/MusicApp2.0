from django import forms

from .models import Genre, Track

class AddTrackForm(forms.ModelForm):

    class Meta:
        model = Track
        fields = ('title', 'artist', 'album', 'track_rating', 'genre',)

        widgets={
                      "title":forms.TextInput(attrs={'class':'form-control'}),
                      "artist":forms.TextInput(attrs={'class':'form-control'}),
                    #   "genre":forms.TextInput(attrs={'class':'selectpicker'}),
                    #   "description":forms.TextInput(attrs={'placeholder':'description','name':'description','id':'common_id_for_imputfields','class':'input-class_name'}),

                  }


class AddGenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = ('name',)

        widgets={
                      "name":forms.TextInput(attrs={'class':'form-control'}),
                    #   "artist":forms.TextInput(attrs={'class':'form-control'}),
                    #   "genre":forms.TextInput(attrs={'class':'selectpicker'}),
                    #   "description":forms.TextInput(attrs={'placeholder':'description','name':'description','id':'common_id_for_imputfields','class':'input-class_name'}),

                  }
