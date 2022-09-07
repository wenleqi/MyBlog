from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import Topic,Comment
from django.urls import reverse
from .forms import TopicFrom,CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.

"""
话题页面，返回所有话题
url：all_topics/
name: all_topics
template: topic_list.html
"""
def all_topic_view(request):
    topic_list = Topic.objects.filter(is_public = True).filter(is_online=True)
    context = topic_list
    return render(request,'blog/topic_list.html',context = {'topic_list':context})

"""
话题页面里面，显示话题详情，评论等
url: topic/topic_id
name: topic
template :topic_detail
"""
def topic_detail(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    comments = topic.comment_set.order_by('-created_time')
    return render(request,'blog/topic_detail.html',context={'topic':topic,'comments':comments})

"""
创建Topic
url:create_topic
name:create_topic
template:create_topic
"""
@login_required(login_url='user:login')
def create_topic(request):
    if request.method == 'POST':
        form = TopicFrom(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.user = request.user
            new_topic.save()
            form.save()
            return all_topic_view(request)
        else:
            return JsonResponse({'error':'填写有误'})
    else:
        form = TopicFrom()
        return render(request,'blog/create_topic.html',context={'form':form})


"""
删除Topic
url:del_topic/topic_id
"""
def del_topic(request,topic_id):
    topic = Topic.objects.get(id = topic_id)
    if request.user == topic.user:
        topic.delete()
        return JsonResponse({'message':'删除成功'})
    else:
        return all_topic_view(request)

"""
修改话题
url:change_topic/topic_id
tamplate:change_topic.html
"""
def change_topic(request,topic_id):
    topic = Topic.objects.get(id = topic_id)
    if request.user == topic.user:
        if request.method == 'POST':
            form = TopicFrom(instance=topic,data=request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({'message':'修改成功'})
            else:
                return JsonResponse({'message':'填写有误'})
        else:
            form = TopicFrom(instance=topic)
            return render(request,'blog/change_topic.html',context={'form':form})

"""
添加评论
"""
def add_comment(request,topic_id):
    topic = Topic.objects.get(id = topic_id)
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.topic = topic
            new_comment.save()
            form.save()
            return HttpResponse('评论成功!!!')
        else:
            return HttpResponse('评论失败')
    else:
        form = CommentForm()
        return render(request,'blog/add_comment.html',context={'form':form})


"""
删除评论
url:del_comment
"""
def del_comment(request,comment_id):
    comment = Comment.objects.get(id = comment_id)
    if request.user == comment.user:
        comment.delete()
        return HttpResponse('删除成功！！！')
    else:
        return HttpResponse('您没有删除权限!!!!')

def index(request):
    return render(request,'blog/index.html',context=None)


