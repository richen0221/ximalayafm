import json
from os import path
from os import makedirs
from requests import get
from tqdm import tqdm
from math import ceil

# Change the json file name
playlist = 'ooo.json'


with open(playlist, encoding='utf8') as reader:
    jf = json.loads(reader.read())

total_files = len(jf['data']['tracksAudioPlay'])
dl_progress = 1

for plays in range(len(jf['data']['tracksAudioPlay'])):
    name = jf['data']['tracksAudioPlay'][plays]['trackName']
    url = jf['data']['tracksAudioPlay'][plays]['src']
    album_name = jf['data']['tracksAudioPlay'][plays]['albumName']
    save_file = path.join(album_name, f"{name}.mp3")
    req = get(url, stream=True)
    total_size = float(req.headers.get('content-length'))
    block_size = 1024
    wrote = 0

    if not path.exists(album_name):
        makedirs(album_name)
    print(">>>>>>>>>> " + save_file + f" is downloading.... {dl_progress}/{total_files} <<<<<<<<<< \n")
    with open(save_file, 'wb') as f:
        for data in tqdm(req.iter_content(block_size), total=ceil(total_size // block_size),
                         unit='', unit_scale=False):
            wrote = wrote + len(data)
            f.write(data)
    if total_size != 0 and wrote != total_size:
        print("######## ERROR, something went wrong ########")
    print("\n==========" + save_file + " is ready ==========\n")
    dl_progress += 1
