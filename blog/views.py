from django.shortcuts import render

# Create your views here.
def post_list(request):
    """docstring for post_list"""
    return render(request, 'blog/post_list.html', {})


