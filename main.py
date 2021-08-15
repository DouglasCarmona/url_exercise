from fastapi import FastAPI, Query, HTTPException, status
from utils import count_freq_keywords, count_short_tail_keywords, count_total_keywords, count_unique_keywords, get_keywords, get_title

app = FastAPI()

@app.get('/')
def home():
    return 'This is my fucking awesome API I am a crack'

@app.get('/title')
def url_title(url: str = Query(...)):
    result = {}
    result['url'] = url
    try:
        result['title'] = get_title(url)
    except Exception as e:
        print(f'Could not load page {url}. Reason: {e}')
        raise HTTPException(status.HTTP_404_NOT_FOUND, 
                            detail= f'Could not load page {url}. Reason: {e}')
    return result

@app.get('/keywords')
def url_title(url: str = Query(...)):
    result = {}
    result['url'] = url
    try:
        keywords_list = get_keywords(url)
    except Exception as e:
        print(f'ERROR: Could not load page {url}. Reason: {e}')
        raise HTTPException(status.HTTP_404_NOT_FOUND, 
                            detail= f'Could not load page {url}. Reason: {e}')
    result['Count total keywords'] = count_total_keywords(keywords_list)
    result['Count unique keywords'] = count_unique_keywords(keywords_list)
    result['Keyword frequency'] = count_freq_keywords(keywords_list)
    result['Count short tail keywords'] = count_short_tail_keywords(keywords_list)
    return result
