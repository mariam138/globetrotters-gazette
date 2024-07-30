from django.shortcuts import render, get_object_or_404
# Allows use of built in generic views that Django supplies
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Allows prepopulating of slug field
from django.template.defaultfilters import slugify
from django.urls import reverse
from .models import Post
from .forms import PostForm

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


# Use of Django's generic Detail View to view each post in a separate view
class PostDetailView(generic.DetailView):
    model = Post


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
        if post_form.is_valid():
            post = post_form.save(commit=False)
            # Set post back to unapproved after edit to maintain quality
            post.approved = False
            post.save()

            # Display messages to user
            messages.success = (
                request,
                'Your post has been updated and is awaiting approval.'
            )
        else:
            messages.error = (
                request,
                'There was a problem updating your post. Please try again.'
            )


    return render(request, 'blog/create_post.html',
                  {
                      'post_form': post_form
                  })
