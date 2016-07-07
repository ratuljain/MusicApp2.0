import datetime
from haystack import indexes
from musicapp.models import Track


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # title = indexes.CharField(model_attr='title')
    # artist = indexes.CharField(model_attr='artist')
    

    def get_model(self):
        return Track

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
