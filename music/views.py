from django.views import  generic
from .models import Album,Song

class IndexView(generic.ListView):
	template_name='music/index.html'
	context_object_name='all_albums'

	def get_queryset(self):
		return Album.objects.all()


class DetailView1(generic.DetailView):
	model=Album
	template_name='music/detail1.html'

class DetailView2(generic.DetailView):
	model=Album
	template_name='music/detail2.html'






