from django.shortcuts import render
from django.http import HttpResponse

from .models import Recipe


from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

#added for the detail view class
from django.views.generic import DetailView

# Create your views here.
def home(request):
    myDict = {
        "title": "Home",
        "current_page": "home",
    }
    return render(request,'index.html', context=myDict)

def browse(request):
    num = int(request.GET.get('num', 1))  # 1 is the default value
    max_recipes_per_page = 3  # Set the maximum number of recipes to display per page

    recipes = Recipe.objects.all()
    paginator = Paginator(recipes, max_recipes_per_page)

    page = paginator.get_page(num)
    page_range = paginator.page_range
    max_pages = paginator.num_pages

    myDict = {
        "title": "Browse",
        "current_page": "browse",  # Set current_page to 'browse'
        "num": num,
        "recipes": page,
        "max_recipes_per_page": max_recipes_per_page,
        "page_range": page_range,
        "max_pages": max_pages,
    }
    return render(request, 'browse.html', context=myDict)

class RecipeDetailView(DetailView): 
    model = Recipe
    


@login_required
def following(request):
    num = int(request.GET.get('num', 1))  # 1 is the default value
    max_recipes_per_page = 3  # Set the maximum number of recipes to display per page

    followed_users = request.user.userprofile.following.all()
    recipes = Recipe.objects.filter(user__in=followed_users)

    paginator = Paginator(recipes, max_recipes_per_page)
    page = paginator.get_page(num)
    page_range = paginator.page_range
    max_pages = paginator.num_pages

    myDict = {
        "title": "Browse",
        "current_page": "following",  # Set current_page to 'following'
        "num": num,
        "recipes": page,
        "max_recipes_per_page": max_recipes_per_page,
        "page_range": page_range,
        "max_pages": max_pages,
    }
    return render(request, 'browse-following.html', context=myDict)

@login_required
def myrecipes(request):
    num = int(request.GET.get('num', 1))  # 1 is the default value
    max_recipes_per_page = 3  # Set the maximum number of recipes to display per page

    recipes = Recipe.objects.filter(user=request.user)
    paginator = Paginator(recipes, max_recipes_per_page)

    page = paginator.get_page(num)
    page_range = paginator.page_range
    max_pages = paginator.num_pages

    myDict = {
        "title": "myrecipes",
        "current_page": "myrecipes",  
        "num": num,
        "recipes": page,
        "max_recipes_per_page": max_recipes_per_page,
        "page_range": page_range,
        "max_pages": max_pages,
    }
    return render(request,'myrecipes.html', context = myDict)

@login_required
def create(request):
    return HttpResponse("Create")

@login_required
def favorites(request):
    num = int(request.GET.get('num', 1))  # 1 is the default value
    max_recipes_per_page = 3  # Set the maximum number of recipes to display per page

    recipes = request.user.userprofile.favouriteRecipes.all()
    paginator = Paginator(recipes, max_recipes_per_page)

    page = paginator.get_page(num)
    page_range = paginator.page_range
    max_pages = paginator.num_pages

    myDict = {
        "title": "Favorites",
        "current_page": "favorites",  
        "num": num,
        "recipes": page,
        "max_recipes_per_page": max_recipes_per_page,
        "page_range": page_range,
        "max_pages": max_pages,
    }
    return render(request,'favorites.html', context = myDict)