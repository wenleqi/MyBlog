from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('all_topics/',views.all_topic_view,name='all_topics'),
    path('topic/<int:topic_id>',views.topic_detail,name='tipic_detail'),
    path('create_topic/',views.create_topic,name='create_topic'),
    path('del_topic/<int:topic_id>',views.del_topic,name='del_topic'),
    path('change_topic/<int:topic_id>',views.change_topic,name='change_topic'),
    path('add_comment/<int:topic_id>',views.add_comment,name='add_comment'),
    path('del_comment/<int:comment_id>',views.del_comment,name='del_comment')
]
app_name = 'blog'