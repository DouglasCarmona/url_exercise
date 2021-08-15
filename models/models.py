from typing import Dict, Union
from pydantic import BaseModel

class KeywordsResponse(BaseModel):
    url: str
    count_total_keywords: int
    count_unique_keywords: int
    keyword_frequency: Dict[str, Union[str,int]]
    count_short_tail_keywords: int

class TitleResponse(BaseModel):
    url: str
    title: str