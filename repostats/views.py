from django.views.generic.edit import FormView

from repostats.forms import RepoForm
from repostats.githubapi import GitHubAPI


class Index(FormView):

    form_class = RepoForm
    template_name = 'index.html'
    success_url = ''
    repo1 = None
    repo2 = None

    def form_valid(self, form):
        self.repo1 = GitHubAPI(repo=form.cleaned_data['repo1'])
        self.repo2 = GitHubAPI(repo=form.cleaned_data['repo2'])
        return self.render_to_response(self.get_context_data())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        if self.repo1 and self.repo2:
            context['repo1'] = self.repo1
            context['repo2'] = self.repo2
        return context
