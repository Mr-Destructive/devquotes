from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Quote
from .forms import QuoteForm, UpdateQuoteForm, DeleteQuoteForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
# Create your views here.

class HomeView(ListView):
    model = Quote
    template_name = 'base.html'
    
    
class QuoteView(DetailView):
    model = Quote
    template_name = 'quote/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(QuoteView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Quote,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddQuoteView(LoginRequiredMixin, CreateView):
    model = Quote
    form_class = QuoteForm
    template_name = 'quote/add.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddQuoteView, self).form_valid(form)

class UpdateQuoteView(LoginRequiredMixin, UpdateView):
    model = Quote
    form_class = UpdateQuoteForm
    template_name = 'quote/update.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(UpdateQuoteView, self).form_valid(form)

class DeleteQuoteView(DeleteView):
    model = Quote
    form_class = DeleteQuoteForm
    template_name = 'quote/delete.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(DeleteQuoteView, self).form_valid(form)

class MyQuote(LoginRequiredMixin, ListView):
    model = Quote
    template_name = 'quote/myquote.html'

def LikeView(request, pk):
    quote = Quote.objects.get(id=pk)
    liked = False
    if quote.likes.filter(id=request.user.id).exists():
        quote.likes.remove(request.user)
        liked=False
    else:
        quote.likes.add(request.user)
        like =True
    return HttpResponseRedirect(reverse('quote', args=[str(pk),]))

def HomeLikeView(request, pk):
    quote = Quote.objects.get(id=pk)
    liked = False
    if quote.likes.filter(id=request.user.id).exists():
        quote.likes.remove(request.user)
        liked=False
    else:
        quote.likes.add(request.user)
        liked =True
    return HttpResponseRedirect(reverse('home', ))

class ProfileView(DetailView):
    model = Quote
    template_name = 'quote/profile.html'

