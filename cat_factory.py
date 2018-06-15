import shutil
import requests
import os


def download_cats():
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    response = requests.get(url, stream=True)
    return response.raw


def save_cats(file_name, data, full_path):
    file_name = os.path.join(full_path, file_name + '.jpg')
    with open(file_name, 'wb') as fout:
        shutil.copyfileobj(data, fout)
