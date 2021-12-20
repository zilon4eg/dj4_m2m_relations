from django.shortcuts import render

from articles.models import Article, Tag, Scope


def articles_list(request):
    template = 'articles/news.html'

    article_objects = Article.objects.all()
    articles = []
    for art in article_objects:
        article = {
            'id': art.id,
            'title': art.title,
            'text': art.text,
            'published_at': art.published_at,
            'image': art.image
        }
        scope_objects = Scope.objects.filter(tag_id=article['id'])
        scopes = list(sc.article_id for sc in scope_objects)
        print(scopes)

        tag_objects = Tag.objects.filter(id__in=scopes)
        tag = list({'name': t.name} for t in tag_objects)
        # print(tag)

        article['scopes'] = tag_objects
        articles.append(article)

    context = {
        'object_list': articles
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)


