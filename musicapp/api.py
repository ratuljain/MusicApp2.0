from tastypie.resources import Resource

from .models import Track

class AjaxSearchResource(Resource):

    class Meta:
        resource_name = 'ajaxsearch'
        allowed_methods = ['post']

    def post_list(self, request, **kwargs):
        phrase = request.POST.get('q')
        if phrase:
            posts = list(Track.objects.filter(title__icontains=phrase).values('id', 'title', 'genre', 'album', 'artist'))
            return self.create_response(request, {'posts': posts})
