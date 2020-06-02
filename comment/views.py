from .models import Comment
from .forms import CommentForm
from django.http import JsonResponse
# Create your views here.


def submit_comment(request):
    comment_form = CommentForm(request.POST, user=request.user)
    data = {}
    if comment_form.is_valid():
        # 验证通过，保存数据
        comment = Comment()
        comment.comment_user = comment_form.cleaned_data['user']
        comment.text = comment_form.cleaned_data['text']
        comment.content_object = comment_form.cleaned_data['content_type']
        # 判断是否是主评论
        parent = comment_form.cleaned_data['parent']
        if parent is not None:
            comment.parent = parent
            comment.root = parent.root if parent.root is not None else parent
            comment.reply_to = parent.comment_user
        comment.save()
        # 返回数据
        data['status'] = 'SUCCESS'
        data['username'] = comment.comment_user.username
        data['comment_time'] = comment.comment_time.strftime('%Y-%m-%d %H %M %S')
        data['text'] = comment.text
        if parent is not None:
            data['reply_to'] = comment.reply_to.username
        else:
            data['reply_to'] = ''
        data['pk'] = comment.pk
        data['root_pk'] = comment.root.pk if comment.root is not None else ''
    else:
        data['status'] = 'ERROR'
        data['message'] = list(comment_form.errors())[0][0]
    return JsonResponse(data, safe=False)