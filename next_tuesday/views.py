from django.views.generic import TemplateView
from django.conf import settings

class NextTuesdayView(TemplateView):
	template_name = "nexttuesday.html"

	def get_context_data(self, **kwargs):
		context = super(NextTuesdayView, self).get_context_data(**kwargs)

		phrase = settings.NEXT_TUESDAY_COMPILED.create_phrase()

		context['phrase'] = phrase or "I can't thing of anything"

		return context
