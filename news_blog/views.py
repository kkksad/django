from django.shortcuts import render

articles = [
   {
       'id': 1,
       'title': 'First news',
       'text': 'This is the worst first article'
   },
   {
       'id': 2,
       'title': 'Second news',
       'text': 'This is the amazing second article'
   }]


def index(request):
    return render(request, 'news_list.html', {'articles':articles})
def get_article(request, article_id):
    article = None
    for a in articles:
        if a['id'] == article_id:
            article = a
            break
    return render(request, 'news_blog/news_article.html', {'article': article})
def about(request):
    return render(request, 'news_blog/about.html')

