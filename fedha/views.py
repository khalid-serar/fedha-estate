from fedha.models import Business, Neighbourhood, Post
from fedha.forms import BusinessForm, NewNeighbourHood, PostForm, SignupForm, UserProfileForm
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    all_hoods = Neighbourhood.objects.all()

    return render(request,'index.html',{"all_hoods":all_hoods})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration/registration_form.html', {'form': form})


def neighbourhoods(request):
    all_hoods = Neighbourhood.objects.all()
    all_hoods = all_hoods[::-1]
  
    return render(request, 'index.html',{'all_hoods':all_hoods})

@login_required(login_url='/accounts/login/')
def create_neighbourhood(request):
    if request.method == 'POST':
        form = NewNeighbourHood(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.user = request.user
            neighbourhood.save()
            messages.success(request, 'A new Neighbourhood has been created! Join it and become a member')
            return redirect('index')
    else:
        form = NewNeighbourHood()
    return render(request, 'new_neighbourhood.html', {'form': form})

@login_required(login_url='/accounts/login/')    
def profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if  profile_form.is_valid():
            profile_form.save()
            return redirect('home')
    else:
        profile_form = UserProfileForm(instance=request.user)
    return render(request, 'profile.html',{ "profile_form": profile_form})

@login_required(login_url='/accounts/login/')
def joinhood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = hood
    request.user.profile.save()
    return redirect('index')

@login_required(login_url='/accounts/login/')
def leave_neighbourhood(request, id):
    neighbourhood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    messages.success(
        request, 'Success! You have succesfully exited this Neighbourhood ')
    return redirect('index')

@login_required(login_url='/accounts/login/')
def single_neighbourhood(request, id):
    neighbourhood = Neighbourhood.objects.get(id=id)
    business = Business.objects.filter(neighbourhood_id=id)
    # posts = Post.objects.filter(hood=neighbourhood)
    # posts = posts[::-1]
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business_form = form.save(commit=False)
            business_form.neighbourhood = neighbourhood
            business_form.user = request.user.profile
            business_form.save()
            return redirect('single-hood', id)
    else:
        form = BusinessForm()
    context = {
        'neighbourhood': neighbourhood,
        'form': form,
        'business': business,
    }
    return render(request, 'single_hood.html', context)


@login_required(login_url='/accounts/login/')
def create_post(request, hood_id):
    neighbourhood = Neighbourhood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.neighbourhood = neighbourhood
            post.user = request.user.profile
            post.save()
            messages.success(
                    request, 'You have succesfully created a Post')
            return redirect('single-hood', hood_id)
    else:
        form = PostForm()
    return render(request, 'posty.html', {'form': form})

@login_required(login_url='/accounts/login/')
def search_business(request):
    if 'business_name' in request.GET and request.GET["business_name"]:
        search_term = request.GET.get("business_name")
        found_businesses = Business.search_by_name(search_term)
        message = f"{search_term}"
        print(search_term)
        context = {"found_businesses":found_businesses,"message":message}
        return render(request, 'search.html',context)
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})