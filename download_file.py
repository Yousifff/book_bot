import requests
import pathlib

def download_file_from_url():
    url = 'https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt'
    r = requests.get(url)
    for line in r.text.splitlines():
        yield line


def save_to_file(fname,text):
    file_path = pathlib.Path(fname)
    with pathlib.Path.open(file_path,'w') as saveToFile:
        for line in text:
            saveToFile.write(line+"\n")
