from fastapi import FastAPI, Query, HTTPException, status
from models.models import KeywordsResponse, TitleResponse
from services.url import Url


app = FastAPI()


@app.get('/')
def home():
    return {'msg': 'Welcome to the url title and keywords extractor API'}

@app.get('/api/v1/title', response_model=TitleResponse)
def url_title(url: str = Query(...)):
    try:
        url_instance = Url(url)
        response = url_instance.get_title_dict()
    except Exception as e:
        print(f'Could not load page {url}. Reason: {e}')
        raise HTTPException(status.HTTP_404_NOT_FOUND, 
                            detail= f'Could not load page {url}. Reason: {e}')
    return response

@app.get('/api/v1/keywords', response_model=KeywordsResponse)
def url_title(url: str = Query(...)):
    try:
        url_instance = Url(url)
        response = url_instance.get_keyworks_statistics()
    except Exception as e:
        print(f'ERROR: Could not load page {url}. Reason: {e}')
        raise HTTPException(status.HTTP_404_NOT_FOUND, 
                            detail= f'Could not load page {url}. Reason: {e}')
    
    return response
