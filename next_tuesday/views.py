from django.views.generic import TemplateView

class NextTuesday(TemplateView):
	template_name = "nexttuesday.html"

	def get_context_data(self, **kwargs):
		context = super(NextTuesday, self).get_context_data(**kwargs)

		context['phrase'] = "I can't thing of anything"

		return context
