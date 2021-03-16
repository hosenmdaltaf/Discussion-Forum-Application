from django.urls import path
from .import views
from .views import(
   DiscussCreateView  
 ) 
app_name='Forum'

urlpatterns = [
    path('',views.home,name='home'),
    path('create/', DiscussCreateView.as_view(), name='profile_create')
    # path('update/<int:pk>', ProfileUpdateView.as_view(), name='profile_update'),
    # path('delete/<int:pk>', ProfileUpdateView.as_view(), name='profile_delete')
]


