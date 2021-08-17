import requests, re
from bs4 import BeautifulSoup
from typing import List


def get_title(url: str) -> str:
    """
    Returns the title of a given url.
            Parameters:
                    url (str): a website url
            Returns:
                    title (str): url's title. 
                    If the url does not have a title a empty string is returned.
    """
    res = requests.get(url, timeout=60.05)
    res.raise_for_status()
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    title = ''
    if soup.title:
        title = soup.title.string
    title = re.sub(r'[\n\t\r]', '', title)
    return title.strip()


def get_keywords(url: str) -> List[str]:
    """
    Returns the keywords of a given url.
        Parameters:
            url (str): a website url
        Returns:
            all_keywords_list (List[str]): list with all keywords as strings.
            If the url does not have keywords a empty list is returned.
    """
    res = requests.get(url, timeout=60.05)
    res.raise_for_status()
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    meta_list = soup.find_all('meta')
    meta_keywords_list = []
    for meta in meta_list:
        meta_name = meta.attrs.get('name', '')
        if re.fullmatch(r'keywords?\b', meta_name):
            meta_keywords_list.append(meta.attrs.get('content'))
 
    all_keywords_list = []
    for meta_keyword in meta_keywords_list:
        keywords_list = meta_keyword.split(',')
        keywords_list = [key.strip() for key in keywords_list if key]
        all_keywords_list.extend(keywords_list)
    return all_keywords_list


def count_total_keywords(keywords: List[str]) -> int:
    """
    Returns the count of total keywords of a list of keywords as a integer.
        Parameters:
            keywords (List[str]): list with all keywords as strings.
    """
    return len(keywords)


def count_unique_keywords(keywords: List[str]) -> int:
    """
    Returns the count of unique keywords of a list of keywords as a integer.
        Parameters:
            keywords (List[str]): list with all keywords as strings.
    """ 
    unique_keywords = set(keywords)
    return len(unique_keywords)


def count_freq_keywords(keywords: List[str]) -> List[tuple]:
    """
    Returns the count of each unique keyword of a list of keywords.
        Parameters:
            keywords (List[str]): list with all keywords as strings.
        Returns:
            a list of tuples of the form (keyword, count).
    """ 
    unique_keywords = set(keywords)
    return [(keyword, keywords.count(keyword)) for keyword in unique_keywords]


def count_short_tail_keywords(keywords: List[str]) -> int:
    """
    Returns the count of short tail keywords in a list of keywords.
        Parameters:
            keywords (List[str]): list with all keywords as strings.
        Returns:
            total (int): count of short tail keywords (1 o 2 words per keyword).
    """ 
    total = 0
    for keyword in keywords:
        keyword_list = keyword.split()
        if len(keyword_list) > 1 and len(keyword_list) < 3:
            total += 1
    return total

if __name__ == '__main__':
    title = get_title('https://www.publimetro.com.mx/mx/entretenimiento/2013/05/30/fotos-belinda-sexy-geisha-mexico-suena.html')

    print(title)