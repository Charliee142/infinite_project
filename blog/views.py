from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.utils.text import slugify
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView
from django.http import HttpResponseRedirect


def blog(request):
    posts = Post.objects.all()
    # Add Paginator
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        "posts": posts
    }
    return render(request, 'blog/blog_index.html', context)


def detail(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.exclude(post_id__exact=post.post_id)
     # Add Paginator
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    comments = post.comments.all()
    post.view_count += 1
    post.save()
    new_comment = None
    msg = False
    form = CommentForm()
    
    if request.user.is_authenticated:
        user = request.user
        if post.likes.filter(id=user.id).exists():
            msg = True
    
    if request.method == "POST":
        if request.user.is_authenticated:
            user = request.user
            
            if post.likes.filter(id=user.id).exists():
                post.likes.remove(user)  
                msg = False  
            else:
                post.likes.add(user)
                msg = True
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('detail', args=[str(post.slug)]))
    else:
        form = CommentForm()
         
    context={
        "post": post,
        "posts": posts,
        "form": form,
        "comments": comments,
        "new_comment": new_comment,
        "msg": msg,
    }
    return render(request, 'blog/blog_detail.html', context)


def Category(request, slug):
    category_posts = Post.objects.get(category_id=slug)
   
    context={
        
        "category_posts": category_posts
    }
    return render(request, 'blog/blog_category.html', context)


def account(request):
    my_account = request.user.userprofile
    context={
        "account": my_account
    }
    return render(request, 'blog/user_account.html', context)


class CreateProfilePageView(CreateView):
    model = UserProfile
    template_name = 'blog/create_profile.html'
    fields = ['first_name', 'last_name', 'email', 'username', 'profession', 'about', 'image', 'website_url', 'facebook_url', 
              'twitter_url', 'instagram_url', 'whatsapp_url', 'linkedin_url', 'telegram_url', 'youtube_url', 'github_url']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def add_category(request):
    form = CategoryForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
        messages.info(request, 'Category was added successfully!')
        return redirect("index")
    context={
        "form": form
    }
    return render(request, 'blog/create_category.html', context)


def Profile(request, pk):
    user_profile = UserProfile.objects.get(profile_id=pk)
    context={
        "profile": user_profile
    }
    return render(request, 'blog/user_profile.html', context)


def account(request):
    my_account = request.user.userprofile
    context={
        "account": my_account
    }
    return render(request, 'blog/user_account.html', context)


def UpdateProfile(request):
    profile = request.user.userprofile
    form = UpdateProfileForm(instance = profile)
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.info(request, 'Congratulations! Your profile was updated successfully.')
            return redirect("account")
    context={
        "form": form
    }
    return render(request, 'blog/update_profile.html', context)


def DeleteProfile(request):
    profile = request.user.userprofile
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
        profile.delete()
        user = request.user
        user.delete()
        #userprofile = UserProfile.objects.get(user=profile)
        #userprofile.delete()
        #messages.info(request, 'Your profile has been deleted successfully!')
        return redirect("index")
    context={
        "form": form
    }
    return render(request, 'blog/delete_profile.html', context)


def createPost(request):
    profile = request.user.userprofile
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            post=form.save(commit=False)
            post.slug = slugify(post.title)
            post.writer = profile
            post.save()
            messages.info(request, 'Article Created Successfully!')
            return redirect("detail", slug=post.slug)
        else:
            messages.error(request, 'Article Not Created due to Error!')
    context={
        "form":form,
    }
    return render(request, 'blog/create_post.html', context)


def updatePost(request, slug):
    post=Post.objects.get(slug=slug)
    form=PostForm(instance=post)
    if request.method == "POST":
        form=PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.info(request, 'Article updated Successfully!')
            return redirect("detail", slug=post.slug)
        else:
            messages.error(request, 'Article Not Updated due to Error!')
    context={
        "form":form,
    }
    return render(request, 'blog/update_post.html', context)


def deletePost(request, slug):
    post=Post.objects.get(slug=slug)
    form=PostForm(instance=post)
    if request.method == "POST":
        post.delete()
        messages.info(request, 'Article deleted Successfully!')
        return redirect("index")
    context={
        "form":form,
    }
    return render(request, 'blog/delete_post.html', context)


def search(request):
	query = request.POST.get("search")
	if query:
		posts = Post.objects.filter(title__icontains=query)
	else:
		posts = []

	context = {
		'posts':posts,
		'query': query,
	}
	return render(request, "blog/search.html", context)
