import os, sys
from utils import get_title
from typing import IO
import progressbar

def url_title_from_csv(filepath: str) -> IO:
    """
    Returns a file with all url and titles.
            Parameters:
                    filepath (str): filepath where urls are listed. 
                    This file must have a header and a diferent line for each url
            Returns:
                    url_titles.txt (IO): tab separated file where the given url are listed 
                    with their corresponding titles. 
                    If a error ocurred for an url an error message is returned.
                    This file is save in the same directory where the script is located.  
    """
    ## Check whether the filepath is valid.
    if not os.path.isfile(filepath):
        print(f'{filepath} does not exist. Please provide a valid filepath')
        sys.exit()

    print(f'\nBeggining to read file: {filepath}\n')
    
    results = []
    with open(filepath, 'r') as f:
        bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
        for index, line in enumerate(f):
            url = line.strip('\n').strip('"')
            if index != 0:
                try:
                    title = get_title(url)
                except Exception as e:
                    title = f'Could not load page {url}. Reason: {e}'
                result_line = '\t'.join([url, title])
                results.append(result_line)
                bar.update(index)
        bar.finish()
    
    print(f'\nFinished reading {index} urls from file: {filepath}\n')

    result_filename = './urls_titles.txt'

    print(f'\nBeggining to create file: {result_filename}\n')

    try:
        with open(result_filename, mode='w', encoding='utf-8') as nf:
            headers = '\t'.join(['url', 'title'])
            nf.write(headers + '\n')
            for line in results:
                nf.write(line + '\n')
            print(f'\nFinished writing {len(results)} records to {result_filename} file')
    except Exception as e:
        print(f'Error ocurred creating file {result_filename}. Reason: {e}')


if __name__ == '__main__':
    titles = url_title_from_csv('/home/douglas/projects/url_exercise/errorers.txt')