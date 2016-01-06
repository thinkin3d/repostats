from django import forms
from django.utils.translation import ugettext_lazy as _

from repostats.githubapi import GitHubAPI


class RepoForm(forms.Form):

    repo1 = forms.CharField(help_text='format: https://github.com/[USER]/[REPOSITORY]')
    repo2 = forms.CharField(help_text='format: https://github.com/[USER]/[REPOSITORY]')

    def clean_repo1(self):
        repo1 = GitHubAPI(repo=self.cleaned_data['repo1'])
        if not repo1.exists():
            raise forms.ValidationError(_(u'Repository 1 not found'))
        return self.cleaned_data['repo1']

    def clean_repo2(self):
        repo2 = GitHubAPI(repo=self.cleaned_data['repo2'])
        if not repo2.exists():
            raise forms.ValidationError(_(u'Repository 2 not found'))
        return self.cleaned_data['repo2']
