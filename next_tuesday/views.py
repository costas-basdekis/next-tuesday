from django.views.generic import TemplateView

class NextTuesday(TemplateView):
	template_name = "nexttuesday.html"

	def get_context(self):
		context = super(NextTuesday, self).get_context()

		context['phrase'] = "I can't thing of anything"

		return context
