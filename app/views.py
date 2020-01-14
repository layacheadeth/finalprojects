
#import generic here is a built-in function where user can use the listview, instead of build the whole thing manually
from django.views import generic
from .models import Post,blog
#basiclly, just import the form in previous file to here.
from .forms import CommentForm
# import this show the error will show erro 404 not found.
from django.shortcuts import render, get_object_or_404


#created_on mean the order define in previous class, and -created-on mean reverse order so the last come to the front page.
class PostList(generic.ListView):
    #queryset get the valued by displaying the post in database start from 1 in reverse order
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'app/index.html'


#views of post_detail page
def post_detail(request, slug):
    template_name = 'app/post_detail.html'
    #in case any error occur when rendering the post, show 404 not found
    post = get_object_or_404(Post, slug=slug)
    #all the comments from the post will go to this variable 'comments', if active=false, it wont receieve any.
    comments = post.comments.filter(active=True)
    new_comment = None
        # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
                # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
                # Assign the current post to the comment
            new_comment.post = post
                # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                            'comments': comments,
                                            'new_comment': new_comment,
                                            'comment_form': comment_form})

#django central source
#reference:https://djangocentral.com/creating-comments-system-with-django/

#views of about_us page
def about_us(request):
    obj=blog.objects.get(id=3)
    context={
        'object':obj,
        'description': 'hello I am LAY, 20 years old, and a student dream to be a full-stack-developer',
        'title':['deth','lay acheadeth','ace is the best in the world'],
    }
    return render(request, 'app/about_us.html',context)

