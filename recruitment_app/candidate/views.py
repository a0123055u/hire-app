from datetime import timezone

from django.contrib import messages
from django.core.exceptions import PermissionDenied, ValidationError
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.views.generic import ListView, UpdateView

from .forms import CandidateForm
from .models import CandidateProfile


def add_candidate(request):
    context = {}
    if request.method == "POST":
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
        context['form'] = form
        return HttpResponseRedirect('/candidate/list/')
    else:
        form = CandidateForm()
        context['form'] = form
        candidates = CandidateProfile.objects.all()
        context['candidates'] = candidates
    return render(request, 'candidate_list.html', context)


class CandidateListView(ListView):
    model = CandidateProfile
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CandidateUpdateView(UpdateView):
    model = CandidateProfile
    fields = ['stage']
    template_name_suffix = '_update_form'
    OLD_STATUS = None
    STATUS_CHOICES = (('pending', '1'),
                      ('reviewing', '2'),
                      ('shortlisted', '3'),
                      ('interviewing', '4'),
                      ('advanced_interviewing', '5'),
                      ('rejected', '8'),
                      ('offered', '6'),
                      ('hired', '7'),)

    def form_valid(self, form):
        status_dict = dict(self.STATUS_CHOICES)
        if self.OLD_STATUS == form.instance.stage:
            return super().form_invalid(form)
        if int(status_dict[self.OLD_STATUS]) > int(status_dict[form.instance.stage]):
            return super().form_invalid(form)
        if self.OLD_STATUS == 'pending' and form.instance.stage not in ['reviewing', 'shortlisted']:
            return super().form_invalid(form)
        if self.OLD_STATUS == 'reviewing' and form.instance.stage != 'rejected':
            return super().form_invalid(form)
        if self.OLD_STATUS == 'shortlisted' and form.instance.stage != 'interviewing':
            return super().form_invalid(form)
        if self.OLD_STATUS == 'interviewing' and form.instance.stage not in ['advanced_interviewing', 'offered', 'rejected']:
            return super().form_invalid(form)
        if self.OLD_STATUS == 'advanced_interviewing' and form.instance.stage not in ['offered', 'rejected']:
            return super().form_invalid(form)
        if self.OLD_STATUS == 'offered' and form.instance.stage not in ['hired', 'rejected']:
            return super().form_invalid(form)
        recruiter = self.request.user.groups.filter(name='Recruiter')
        if recruiter and recruiter.exists():
            return super().form_valid(form)

    def get_object(self, *args, **kwargs):
        obj = super(CandidateUpdateView, self).get_object(*args, **kwargs)
        self.OLD_STATUS = obj.stage
        recruiter = self.request.user.groups.filter(name='Recruiter')
        if recruiter and recruiter.exists():
            return obj

