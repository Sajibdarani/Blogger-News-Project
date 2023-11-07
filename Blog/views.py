from django.http import HttpResponse
from django.shortcuts import render


blog_post = [
    {
        'tittle': " sdfdkjlsj",
        'content': " jdhshfsfh",
        'author': "sajib",
        'post_create_date':"45566",

    },
    {
        'tittle': " sdfdkjlsj",
        'content': " jdhshfsfh",
        'author': "sajib",
        'post_create_date': "45566",

    }
]


def home(request):
    return render(request, 'blog/index.html',{"blog_post":blog_post})
    # return HttpResponse('yekgk')
