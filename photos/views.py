from django.views.generic.list import ListView

from photos.models import Photo
from feedback.forms import FeedbackForm


class PhotoView(ListView):
    model = Photo
    template_name = 'photos/photo_list.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        context = super(PhotoView, self).get_context_data(**kwargs)
        context['form'] = FeedbackForm()
        return context
