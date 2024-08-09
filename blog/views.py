from django.shortcuts import render, get_object_or_404, redirect
# Allows use of built in generic views that Django supplies
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
# Use paginator in function views
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
# Allows prepopulating of slug field
from django.template.defaultfilters import slugify
from django.urls import reverse
from profile_page.models import Profile
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


class AllPostList(AsiaPostList):
    queryset = Post.objects.filter(
        status='1', approved=True).order_by("-created_on")


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
    queryset = Post.objects.all()
    # Gets specified post object using the queryset and slug arg
    post = get_object_or_404(queryset, slug=slug)
    # Reverse look up for comments related to specific post
    # Show all comments from newest to oldest
    comments = post.comments.all().order_by("-created_on")

    # Checks if user is logged in before allowing comment form to be created
    if request.user.is_authenticated:
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
                messages.warning(
                    request, 'Your post has been saved as a draft.')
            elif post.status == "1":
                messages.success(
                    request, 'Your post has been published and is awaiting approval.')
            else:
                messages.error(
                    request, 'There was an error saving your post. Please try again.')

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


def user_post_list(request, username):
    """
    Returns a list of posts that the user has created.
    This is accessed through the user's profile.

    Context:
    - user: an instance of the User model
    - posts: a queryset based on the Post model

    Template:
    - blog/view_user_posts.html
    """
    # Gets a user instance where it matches the username in the db
    # With the username passed through with the request
    # 'username' used as the variable to not get confused with 'user' in base.html
    username = User.objects.get(username=username)

    # If the logged in user matches the user from the above instance
    # All posts are displayed
    # Otherwise only approved and published posts can be seen
    if request.user == username:
        posts = Post.objects.filter(user__username=username.username)
    else:
        posts = Post.objects.filter(
            user__username=username.username, status='1', approved=True
        )

    # Applying pagination to a function view
    # Splits posts queryset into subqueries of 6 posts each
    # Adapted from: https://docs.djangoproject.com/en/4.2/topics/pagination/#using-paginator-in-a-view-function
    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    return render(request, 'blog/view_user_posts.html', {
        "username": username,
        "page_obj":page_obj
    })


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
        print(comment.post)
        # Pass the POST data and comment instance into the comment form
        comment_form = CommentForm(data=request.POST, instance=comment)

        # Checks form is valid and only the user who made the comment is editing it
        if comment_form.is_valid() and request.user == comment.user:
            comment = comment_form.save(commit=False)
            # Change approved back to false for quality
            comment.approved = False
            comment.post = post
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
    return (HttpResponseRedirect(reverse('post_detail', args=[slug])))


@login_required
def cancel_edit_comment(request, slug):
    """
    Allows user to cancel updating their comment without updating db.
    """

    messages.warning(
        request,
        'Your comment was not updated.'
    )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def delete_comment(request, slug, comment_id):
    """
    Allows user to delete instance of a comment based on :model:`blog.Comment`.
    This view is only triggered when the user clicks the 'Yes, delete comment'
    button in the modal.

    ** Context **


    ** Template **
    """
    # Get post instance using the slug from the request
    post = get_object_or_404(Post, slug=slug)
    # Get the comment instance to be deleted using the comment id
    comment = get_object_or_404(Comment, pk=comment_id)

    # If logged in user is the creator of the comment, allow deletion
    if request.user == comment.user:
        comment.delete()
        messages.success(
            request,
            'Your comment has been deleted.'
        )
    else:
        messages.error(
            request,
            'You are not permitted to delete this comment.'
        )

    # Refresh post detail page
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class SearchPostList(generic.ListView):
    """
    Uses query searches based off user input to show posts.
    Code adapted from:
    https://learndjango.com/tutorials/django-search-tutorial
    https://stackpython.medium.com/django-search-with-q-objects-tutorial-9c701db74e0e
    """
    model = Post
    template_name = "blog/search_list.html"
    paginate_by = 6
    context_object_name = 'search_list'

    def get_queryset(self):
        search_post = self.request.GET.get('search')
        # Returns posts which contain the search term in either the title or country
        # Filters posts by showing only approved and published posts
        return Post.objects.filter(
            Q(title__icontains=search_post) | Q(
                country__icontains=search_post) | Q(body__icontains=search_post),
                status='1', approved=True
        )
