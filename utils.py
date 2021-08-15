from enum import unique
import requests, re
from bs4 import BeautifulSoup
from typing import List

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_title(url: str) -> str:
    res = requests.get(url, timeout=60.05)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    title = ''
    if soup.title:
        title = soup.title.string
    return title


def get_keywords(url: str) -> List[str]:
    res = requests.get(url, timeout=60.05)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    meta_list = soup.find_all('meta')
    meta_keywords_list = []
    for meta in meta_list:
        meta_name = meta.attrs.get('name', '')
        if re.fullmatch(r'keyword(s)?\b', meta_name):
            meta_keywords_list.append(meta.attrs.get('content'))
 
    all_keywords_list = []
    for meta_keyword in meta_keywords_list:
        keywords_list = meta_keyword.split(',')
        keywords_list = [key.strip() for key in keywords_list if key]
        all_keywords_list.extend(keywords_list)
    return all_keywords_list

def count_total_keywords(keywords: List[str]) -> int:
    return len(keywords)

def count_unique_keywords(keywords: List[str]) -> int:  
    unique_keywords = set(keywords)
    return len(unique_keywords)


def count_freq_keywords(keywords: List[str]) -> List[tuple]:
    unique_keywords = set(keywords)
    return [(keyword, keywords.count(keyword)) for keyword in unique_keywords]

def count_short_tail_keywords(keywords: List[str]) -> int:
    total = 0
    for keyword in keywords:
        keyword_list = keyword.split()
        if len(keyword_list) >= 1 and len(keyword_list) <= 2:
            total += 1
    return total

if __name__ == '__main__':
    keywords = get_keywords('https://www.mobafire.com/league-of-legends/build/rework-urgot-top-tank-bruiser-build-512162')
    print(keywords)
    print(count_total_keywords(keywords))
    print(count_unique_keywords(keywords))
    print(count_freq_keywords(keywords))
    print(count_short_tail_keywords(keywords))