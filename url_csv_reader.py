import os, sys
from utils import get_title

def url_title_from_csv(filepath: str) -> list:
    if not os.path.isfile(filepath):
        print(f'{filepath} does not exist.')
        sys.exit()

    results = []
    
    with open(filepath, 'r') as f:
        for index, line in enumerate(f):
            if index != 0:
                url = line.strip('\n"')  
                try:
                    title = get_title(url)
                except Exception as e:
                    title = f'Could not load page {url}. Reason: {e}'
                
                url_dict = {'url': url,
                            'title': title}
                results.append(url_dict)
        
    return results

if __name__ == '__main__':
    titles = url_title_from_csv('/home/douglas/projects/url_exercise/prueba.txt')