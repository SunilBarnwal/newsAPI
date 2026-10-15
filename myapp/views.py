
import requests
from django.shortcuts import render
from datetime import datetime, timedelta

from myproject.settings import News_API_KEY


def index_view(request):
    from_date = (
        datetime.now() - timedelta(days=1)
    ).strftime('%Y-%m-%d')

    news_url = (
        "https://newsapi.org/v2/everything"
        f"?q=india&from={from_date}"
        "&sortBy=publishedAt"
        f"&apiKey={News_API_KEY}"
    )

    

    news_data = []
    

    try:
        news_response = requests.get(news_url, timeout=10)
        news_response.raise_for_status()
        news_json = news_response.json()

        news_data = news_json.get("articles", [])

    except requests.RequestException as e:
        print("News API Error:", e)

    

    context = {
        "news_data": news_data,
    }

    return render(request, "index.html", context)

def search_menu(request):
    
    if request.method=='POST':
        query=request.POST.get("query")
        
        from_date=(datetime.now() - timedelta(days=1))
        
        
        request_url=f"https://newsapi.org/v2/everything?q={query}&from={from_date.strftime('%Y-%m-%d')}&sortBy=publishedAt&apiKey={News_API_KEY}"
        news_data=requests.get(request_url).json()
    
    
        news_data={
        'news_data':news_data.get("articles")
    }
    return render(request, "index.html", news_data)

    
