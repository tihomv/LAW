from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView
from chamber.forms import CaseForm
from chamber.models import Case
from django.contrib.auth.mixins import LoginRequiredMixin


class ChamberHome(LoginRequiredMixin, ListView):
    model = Case
    context_object_name = "cases"
    def get_queryset(self):
        return self.request.user.Case.all()

class CaseDetail(LoginRequiredMixin, DetailView):
    model = Case
    context_object_name = "case"
    # def get_queryset(self):
    #     return self.request.user.Case.all()



class AddCase(CreateView):
    model = Case
    form_class = CaseForm
    success_url = "/chamber/"
    template_name = "chamber/case_new.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
