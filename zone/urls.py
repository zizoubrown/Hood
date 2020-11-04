from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/<username>/edit/', views.edit_profile, name='edit-profile'),
    path('profile/<username>', views.profile, name='profile'),
    path('all-hoods/',views.neighborhoods,name='hood'),
    path('new-hood/', views.create_neighborhood, name='new-hood'),
    path('join_hood/<id>', views.join_neighborhood, name='join-hood'),
    path('leave_hood/<id>', views.leave_neighborhood, name='leave-hood'),
    path('single_hood/<hood_id>', views.single_neighborhood, name='single-hood'),
    path('<hood_id>/new-post', views.create_post, name='post'),
    
]