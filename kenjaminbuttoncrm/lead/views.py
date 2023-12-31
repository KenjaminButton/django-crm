import csv
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from .forms import AddCommentForm, AddFileForm
from .models import Lead
from team.models import Team
from client.models import Client, Comment as ClientComment


# @login_required
def leads_export(request):
    leads = Lead.objects.filter(created_by=request.user)
    response = HttpResponse(
        content_type='text/css',
        headers={'Content-Disposition': 'attachment; filename="leads.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(["Lead", "Description", "Created at", "Created by"])

    for lead in leads:
        writer.writerow([lead.name, lead.description,
                        lead.created_at, lead.created_by])

    return response


# @login_required
# def show_leads(request):
#     leads = Lead.objects.filter(
#         created_by=request.user, converted_to_client=False)
#     return render(request, 'lead/leads_list.html', {
#         'leads': leads
#     })

class LeadListView(LoginRequiredMixin, ListView):
    model = Lead

    def get_queryset(self):
        queryset = super(LeadListView, self).get_queryset()
        return queryset.filter(
            created_by=self.request.user, converted_to_client=False)


# @login_required
# def leads_detail(request, pk):
#     # Django shortcut for the same functionality as below
#     lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
#     # lead = Lead.objects.filter(created_by=request.user).get(pk=pk)
#     return render(request, 'lead/leadsdetail.html', {
#         'lead': lead
#     })

class LeadDetailView(LoginRequiredMixin, DetailView):
    model = Lead

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddCommentForm()
        context['fileform'] = AddFileForm()
        return context

    def get_queryset(self):
        queryset = super(LeadDetailView, self).get_queryset()
        return queryset.filter(created_by=self.request.user, pk=self.kwargs.get('pk'))

# @login_required
# def leads_delete(request, pk):
#     lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
#     lead.delete()
#     messages.success(request, 'your lead has been deleted')
#     return redirect('leads:show')


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    model = Lead
    success_url = reverse_lazy('leads:list')

    def get_queryset(self):
        queryset = super(LeadDeleteView, self).get_queryset()

        return queryset.filter(created_by=self.request.user, pk=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

# @login_required
# def leads_edit(request, pk):
#     lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

#     if request.method == 'POST':
#         form = AddLeadForm(request.POST, instance=lead)

#         if form.is_valid():
#             form.save()
#             messages.success(
#                 request, 'your lead has been edited successfully and saved')
#             return redirect('leads:list')
#     else:
#         form = AddLeadForm(instance=lead)

#     return render(request, 'lead/leadsedit.html', {
#         'form': form
#     })


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    model = Lead
    fields = ('name', 'email', 'description', 'priority', 'status',)
    success_url = reverse_lazy('leads:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit lead'
        return context

    def get_queryset(self):
        queryset = super(LeadUpdateView, self).get_queryset()
        return queryset.filter(created_by=self.request.user, pk=self.kwargs.get('pk'))

# @login_required
# def add_lead(request):
#     team = Team.objects.filter(created_by=request.user)[0]
#     if request.method == 'POST':
#         form = AddLeadForm(request.POST)
#         if form.is_valid():
#             team = Team.objects.filter(created_by=request.user)[0]
#             lead = form.save(commit=False)
#             lead.created_by = request.user
#             lead.team = team
#             lead.save()
#             messages.success(
#                 request, 'your lead has been created successfully')
#             return redirect('leads:list')
#     else:
#         form = AddLeadForm()

#     return render(request, 'lead/addlead.html', {
#         'form': form,
#         'team': team
#     })


class LeadCreateView(LoginRequiredMixin, CreateView):
    model = Lead
    fields = ('name', 'email', 'description', 'priority', 'status',)
    success_url = reverse_lazy('leads:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team = Team.objects.filter(created_by=self.request.user)[0]
        context['team'] = team
        context['title'] = 'Add lead'

        return context

    def form_valid(self, form):
        team = Team.objects.filter(created_by=self.request.user)[0]
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.team = team
        self.object.save()
        return redirect(self.get_success_url())

# @login_required
# def convert_to_client(request, pk):
#     lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
#     team = Team.objects.filter(created_by=request.user)[0]

#     client = Client.objects.create(
#         name=lead.name,
#         email=lead.email,
#         description=lead.description,
#         created_by=request.user,
#         team=team,
#     )
#     lead.converted_to_client = True
#     lead.save()
#     messages.success(request, 'lead has been converted to a client')
#     return redirect('leads:show')


class ConvertToClientView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
        team = Team.objects.filter(created_by=request.user)[0]

        client = Client.objects.create(
            name=lead.name,
            email=lead.email,
            description=lead.description,
            created_by=request.user,
            team=team,
        )

        lead.converted_to_client = True
        lead.save()
        # Converting lead comments to client comments
        comments = lead.comments.all()
        for comment in comments:
            # Comment renamed to ClientComment so as to not clash with lead Comment
            ClientComment.objects.create(
                client=client,
                content=comment.content,
                created_by=comment.created_by,
                team=team
            )

        messages.success(request, 'lead has been converted to a client')
        return redirect('leads:list')


class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        form = AddCommentForm(request.POST)

        if form.is_valid():
            team = Team.objects.filter(created_by=self.request.user)[0]
            comment = form.save(commit=False)
            comment.team = team
            comment.created_by = request.user
            comment.lead_id = pk
            comment.save()

        return redirect('leads:detail', pk=pk)


class AddFileView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        form = AddFileForm(request.POST, request.FILES)

        if form.is_valid():
            team = Team.objects.filter(created_by=self.request.user)[0]
            file = form.save(commit=False)
            file.team = team
            file.lead_id = pk
            file.created_by = request.user
            file.save()

        return redirect('leads:detail', pk=pk)
