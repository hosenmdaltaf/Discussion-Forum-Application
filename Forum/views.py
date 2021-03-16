from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from .models import  Discussion

from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
# #      ListView,

)

# class My_profileView(ListView):
#     model = Profile
#     # paginate_by = 10
#     context_object_name = 'profiles'
#     template_name='profiles/user_profile_page.html'

#     # def get_context_data(self,*args,**kwargs):
#     #     context = super().get_context_data(*args,**kwargs)
#     #     context['latest']= Post.objects.order_by('-post_date')[:5]
#     #     return context

#post Create page view
class DiscussCreateView(CreateView):
    model= Discussion
    fields= '__all__'
    template_name='Forum/post_create_form.html'
    success_url = reverse_lazy("Forum:home")

    # def form_valid(self,form):
    #     form.instance.creator =self.request.user
    #     return super().form_valid(form)


# #Detailpage view
class DiscussDetailView(DetailView):
    model= Discussion
    context_object_name = 'details'
    template_name='Forum/detail.html'



#post Update page view
class DiscussUpdateView(UpdateView):
    model= Discussion
    fields ='__all__'
    # fields = ['title','image','details']
    template_name='Forum/post_update_form.html'
    success_url = reverse_lazy("Forum:profile-page")

    # def form_valid(self,form):
    #     form.instance.author =self.request.user
    #     return super().form_valid(form)


#post Delete page view
class DiscussDeleteView(DeleteView):
    model= Discussion
    template_name='Forum/post_delete_form.html'
    success_url = reverse_lazy("Forum:profile-page")

   

def home(request):
    allquestions = Discussion.objects.all()
    return render(request,'Forum/discuss.html',{'allquestions':allquestions})
