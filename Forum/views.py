from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from .models import  Discussion

from django.views.generic import (
#     #  DetailView,
      CreateView
#       UpdateView,
# #      ListView,
#      DeleteView
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


# #post Update page view
# class ProfileUpdateView(UpdateView):
#     model = Profile
#     # context_object_name = 'profiles'
#     fields=['profile_picture','bio','full_name','work','loaction','educations','email']
#     template_name='Forum/profile_update_form.html'
#     success_url = reverse_lazy("user_feeds:profile-page")

#     # def form_valid(self,form):
#     #     form.instance.author =self.request.user
#     #     return super().form_valid(form)


# #post Delete page view
# class ProfileDeleteView(DeleteView):
#     model=Profile
#     # context_object_name = 'profile_delete'
#     template_name='Forum/profile_delete_form.html'
#     success_url = reverse_lazy("homepage:article-list")

   

def home(request):
    return render(request,'Forum/discuss.html')
