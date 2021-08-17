from typing import Dict, List, Union
from utils import get_title, get_keywords, count_freq_keywords, count_unique_keywords, count_short_tail_keywords, count_total_keywords


class Url:
    def __init__(self, url: str) -> None:
        self.url = url

    def get_title_dict(self) -> Dict[str,str]:
        response = {}
        response['url'] = self.url

        try:
            response['title'] = get_title(self.url)
        except Exception as e:
            raise Exception(str(e))

        return response

    def get_keyworks_statistics(self) -> Dict[str, Union[str,int, List[tuple]]]:
        try:
            keywords = get_keywords(self.url)
        except Exception as e:
            raise Exception(str(e))

        response = {}
        response['url'] = self.url
        response['count_total_keywords'] = count_total_keywords(keywords)
        response['count_unique_keywords'] = count_unique_keywords(keywords)
        response['keyword_frequency'] = count_freq_keywords(keywords)
        response['count_short_tail_keywords'] = count_short_tail_keywords(keywords)

        return response
