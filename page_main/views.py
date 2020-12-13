from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PostForm


@login_required
def page_main(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("page_main")
    else:
        form = PostForm()
    return render(request, 'page_main/page_main.html', {"form": form})
