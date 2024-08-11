from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    num = request.GET.get('num', 2)  # Получаем значение из GET параметра
    paginator = Paginator(posts, num)  # Количество постов на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})

