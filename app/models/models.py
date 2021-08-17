from typing import Dict
from pydantic import BaseModel

class KeywordsResponse(BaseModel):
    """
    API Response model for url's keywords statistics
    """
    url: str
    count_total_keywords: int
    count_unique_keywords: int
    keyword_frequency: Dict[str, int]
    count_short_tail_keywords: int

class TitleResponse(BaseModel):
    """
    API Response model for url's title
    """
    url: str
    title: str