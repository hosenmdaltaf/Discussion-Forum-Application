from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from .models import  Discussion
from .models import Comment
from .models import Category
from .forms import CommentForm 
from django.views.generic import (
    # DetailView,
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
# class DiscussDetailView(DetailView):
#     model= Discussion
#     context_object_name = 'details'
#     template_name='Forum/detail.html'


def postdetail(request,id):
    details=Discussion.objects.get(id=id)
    post = get_object_or_404(Discussion, id=id)
    latest= Discussion.objects.order_by('-qustion_date')[:5]
   
    comments_form = CommentForm()  

    if request.method == 'POST': 
        comments_form = CommentForm(request.POST ) 
        if comments_form.is_valid(): 
            # comments_form.instance.created_by = profile.request.user
            comment = comments_form.save(commit=False)
            comment.post = details
            comments_form.save() 
            return redirect("Forum:articale-detail", id=post.id )  
        else: 
            comments_form = CommentForm() 

    comments=Comment.objects.filter(post=post)
    return render(request,'Forum/detail.html',{'details':details,'comments':comments,'latest':latest})




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

#   class TaskList(LoginRequiredMixin, ListView):
#     model = Task
#     context_object_name = 'tasks'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['tasks'] = context['tasks'].filter(user=self.request.user)
#         context['count'] = context['tasks'].filter(complete=False).count()

#         search_input = self.request.GET.get('search-area') or ''
#         if search_input:
#             context['tasks'] = context['tasks'].filter(    
#                 title__startswith=search_input)

#         context['search_input'] = search_input

#         return context 



# def gallery(request):
#     category = request.GET.get('category')
#     if category == None:
#         photos = Photo.objects.all()
#     else:
#         photos = Photo.objects.filter(category__name=category)

#     categories = Category.objects.all()
#     context = {'categories': categories, 'photos': photos}
#     return render(request, 'photos/gallery.html', context)



def home(request):
    

    category = request.GET.get('category')
    if category == None:
        allquestions = Discussion.objects.all()
    else:
        allquestions = Discussion.objects.filter(category__name=category)

    categories = Category.objects.all()

    # search_input = request.GET.get('search-area') or ''
    # if search_input:
    #     tasks = allquestions.filter(title__startswith=search_input)
    # 'search_input':search_input

    return render(request,'Forum/discuss.html',{'allquestions':allquestions,'categories':categories})
