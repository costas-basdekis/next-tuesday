from django.views.generic import TemplateView
from django.conf import settings

class NextTuesdayView(TemplateView):
	template_name = "nexttuesday.html"

	def get_context_data(self, word='cunt'):
		context = super(NextTuesdayView, self).get_context_data(word=word)

		#word = self.word
		phrase = settings.NEXT_TUESDAY_COMPILED.create_phrase(word=word)

		context['phrase'] = phrase or "I can't thing of anything"

		return context
