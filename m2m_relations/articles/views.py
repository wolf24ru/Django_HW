from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all().prefetch_related('tags')
    context = {
        'articles': articles
    }
    return render(request, template, context)
