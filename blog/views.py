from django.shortcuts import render, get_object_or_404, redirect
# Allows use of built in generic views that Django supplies
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Allows prepopulating of slug field
from django.template.defaultfilters import slugify
from django.urls import reverse
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def index(request):
    """
    Displays the index page as the home page

    ** Template **
        :template:`blog/index.html`
    """
    return render(request, 'blog/index.html')

    # display success message when user has registered
    messages.add_message(request, messages.SUCCESS, 'Registration successful!')


class AsiaPostList(generic.ListView):
    model = Post
    # Shows posts for related region
    # Only shows posts with a 'published' status
    # and when post has been approved by admin
    queryset = Post.objects.filter(region='ASIA', status='1', approved=True)
    template_name = "post_list.html"
    paginate_by = 6
    context_object_name = "post_list"


class AfricaPostList(AsiaPostList):
    queryset = Post.objects.filter(region='AF', status='1', approved=True)

class AusPostList(AsiaPostList):
    queryset = Post.objects.filter(region='AUS', status='1', approved=True)


class EuropePostList(AsiaPostList):
    queryset = Post.objects.filter(region='EU', status='1', approved=True)


class MenaPostList(AsiaPostList):
    queryset = Post.objects.filter(region='MENA', status='1', approved=True)


class SAmericaPostList(AsiaPostList):
    queryset = Post.objects.filter(region='SA', status='1', approved=True)


class NAmericaPostList(AsiaPostList):
    queryset = Post.objects.filter(region='US', status='1', approved=True)


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.
    Allows a user to submit an individual comment :model:`blog.Comment`

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        An instance of :model:`blog.Comment`
        Only shows comments related to the post instance
    ``comment_form``
        An instance of :model:`forms.CommentForm`

    **Template:**

    :template:`blog/post_detail.html`
    """

    # Queryset only contains post that have a 'Publish' status
    queryset = Post.objects.filter(status=1)
    # Gets specified post object using the queryset and slug arg
    post = get_object_or_404(queryset, slug=slug)
    # Reverse look up for comments related to specific post
    # Show all comments from newest to oldest
    comments = post.comments.all().order_by("-created_on")

    # Create instance of a comment form
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            # Fills in user field with the logged in user
            comment.user = request.user
            # Fills post field with the current post instance
            comment.post = post
            comment.save()

            messages.success(
                request,
                'Your comment has been submitted and is awaiting approval.'
            )
        else:
            messages.error(
                request,
                'There was a problem submitting your comment. '
                'Please try again'
            )

    # Create another blank comment form after submission
    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
        },
    )


@login_required
def create_post(request):
    """
    Allows registered user to create a post using :model:`blog.Post`

    ** Context **
    ``post_form``
        An instance of :model:`forms.PostForm`

    ** Template **
        :template:`blog/create_post.html`
    """

    # Create new instance of a blog form
    post_form = PostForm()

    # Save a post to the database
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
                # Creates an instance of the Post object from the form
                # model = Post defined in the Meta class for PostForm
                post = post_form.save(commit=False)
                # Ensure the post's user matches the user currently logged in
                post.user = request.user
                # Get the url value from the hidden input field
                post.image_url = request.POST.get('image_url')
                # Prepopulate the slug field from the title using Django's slugify
                # Method adapted from:
                # https://stackoverflow.com/questions/55314246/pre-populate-slug-field-into-a-form-field-of-a-django-site
                post.slug = slugify(post.title)
                post.save()
                if post.status == "0":
                    messages.warning(request, 'Your post has been saved as a draft.')
                elif post.status == "1":
                    messages.success(request, 'Your post has been published and is awaiting approval.')
                else:
                    messages.error(request, 'There was an error saving your post. Please try again.')

    # When post is saved, create blank instance of PostForm()
    post_form = PostForm()

    return render(request, 'blog/create_post.html',
                  {
                      'post_form': post_form
                  })


@login_required
def cancel_create_post(request):
    """
    Allows cancelling of creating a post from :model:`blog.Post`
    without saving it as a draft. Will display a message to the
    user that their post was not saved when 'Yes cancel' is
    clicked in the warning modal.

    ** Template **
        :template:`blog/create_post.html`

    """

    # Display message to user that there post was not saved
    messages.warning(
        request,
        'Your post has not been saved.'
    )

    # Redirect user back to homepage when Cancel is clicked
    return HttpResponseRedirect(reverse('index'))


@login_required
def edit_post(request, slug):
    """
    Allows user to edit their post from :model:`blog.Post`.

    ** Context **

    ``post_form``
        An instance of :model:`forms.PostForm`
    ``post``
        An instance of :model:`blog.Post`

    ** Template **
        :template:`blog/create_post.html`

    """

    # Creates a post instance using the slug parameter
    # passed through the view function
    post = get_object_or_404(Post, slug=slug)

    # Create a post form instance using the post instance
    # To prepopulate the form with the post data for editing
    post_form = PostForm(instance=post)

    if request.method == "POST" and post.user == request.user:
        # Creates the post form instance with the post instance
        # and the data being sent from the POST request
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            # Set post back to unapproved after edit to maintain quality
            post.approved = False
            post.save()
            # Display messages to user
            messages.success(
                request,
                'Your post has been updated and is awaiting approval.'
            )
            return redirect(reverse('post_detail', args=[slug]))
        else:
            messages.error(
                request,
                'There was a problem updating your post. Please try again.'
            )

    return render(request, 'blog/edit_post.html',
                  {'post_form': post_form,
                  'post': post})

@login_required
def cancel_edit_post(request, slug):
    """
    Allows cancelling changes when updating a post from :model:`blog.Post`
    without saving it as a draft. Will display a message to the
    user that their changes were not saved when 'Yes cancel' is
    clicked in the warning modal.

    ** Template **
        :template:`blog/edit_post.html`

    """

    # Display message to user that there post was not saved
    messages.warning(
        request,
        'Your post has not been updated.'
    )

    # Redirect user back to post detail page when changes are cancelled
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

@login_required
def delete_post(request, slug):
    """
    Allows user to permanently delete their post from the database.
    Post instance from :model:`blog.Post`. This view is only triggered
    when the user clicks the 'Yes, delete post' button in the warning
    modal.

    ** Template **
        :template:`blog/edit_post.html`
    """

    # Creates a post instance using the slug parameter
    # passed through the view function
    post = get_object_or_404(Post, slug=slug)

    # Create a post form instance using the post instance
    # To prepopulate the form with the post data for editing
    post_form = PostForm(instance=post)

    # Checks that the logged in user is the user who wrote the post
    # So that only the creator can delete their post
    if post.user == request.user:
        post.delete()
        messages.success(
            request,
            'Your post has been deleted.'
        )
    else:
        messages.error(
            request,
            'You are not permitted to delete this post.'
        )

    # Redirects user back to homepage after deletion
    return HttpResponseRedirect(reverse('index'))


# View to get user's blog posts
class UserPostList(generic.ListView):
    model = Post
    # Shows posts for related region
    # Only shows posts with a 'published' status
    # and when post has been approved by admin
    queryset = Post.objects.all()
    template_name = "blog/view_user_posts.html"
    paginate_by = 6
    context_object_name = "user_post_list"

    # Gets the username from the url to pass through the queryset
    # To return all posts from that user
    # Code adapted from:
    # 1. https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-display/#dynamic-filtering
    # 2. https://stackoverflow.com/questions/66511758/can-you-pass-an-argument-to-listview-in-django
    def get_queryset(self):
        # Username key used to capture the username parameter from the url
        # kwargs must match exactly with what is defined in the url path
        # in this case, <str:username> therefore username
        posts = None

        username = self.kwargs['username']

        # Gets a single user object using the username value
        user = User.objects.get(username=username)
        # If the current logged in user matches the user object
        # Show all posts
        if self.request.user == user:
            posts = Post.objects.filter(user__username=user.username)
        # Otherwise, show only approved and published posts
        else:
            posts = Post.objects.filter(user__username=user.username, status='1', approved=True)

        return posts


@login_required
def edit_comment(request, slug, comment_id):
    """
    Allows user to edit their own comments based on
    :model:`blog.Comment`.

    **Context**


    **Template**
        :template:`blog/post_detail.html`

    """

    if request.method == "POST":
        # Get post instance which comment is related to
        post = get_object_or_404(Post, slug=slug)
        # Get the comment instance with the comment id
        comment = get_object_or_404(Comment, pk=comment_id)
        # Pass the POST data and comment instance into the comment form
        comment_form = CommentForm(request.POST, instance=comment)

        # Checks form is valid and only the user who made the comment is editing it
        if comment_form.is_valid() and request.user == comment.user:
            comment = comment_form.save(commit=False)
            # Change approved back to false for quality
            comment.approved = False
            comment.save()
            messages.success(
                request,
                'Your comment has been updated and is awaiting approval.'
            )
        else:
            messages.error(
                request,
                'There was a problem updating your comment. Please try again.'
            )

    # Refresh page that user was on once comment is edited
    return(HttpResponseRedirect('post_detail', args=[slug]))