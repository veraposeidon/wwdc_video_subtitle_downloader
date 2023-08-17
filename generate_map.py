# encoding: utf-8
from bs4 import BeautifulSoup
import requests
import json
import os

def get_wwdc_video_title(year, session):
    session_url = "https://developer.apple.com/videos/play/wwdc{year}/{session}/".format(year=year, session=session)
    # get video title by GET request and parse html get title in <title> tag
    request = requests.get(session_url)
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, 'html.parser')
        title = soup.title.string
        return title
    return ''

# iterate all video links
year_id = 2020
file_path = f'data/wwdc{year_id}_hd_video_links.txt'
subtitle_dir = f'data/WWDC_{year_id}_Video_Subtitles/HD/'
session_dict = {}
with open(file_path, 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if year_id >= 2021:
            # https://devstreaming-cdn.apple.com/videos/wwdc/2023/10309/4/21D925C8-2EE0-4C96-9C68-96174159990A/downloads/wwdc2023-10309_hd.mp4
            session = line.split('/')[-1].split('.')[0].split('-')[-1].removesuffix('_hd')
            print(session)
        elif year_id == 2020:
            # https://devstreaming-cdn.apple.com/videos/wwdc/2020/10004/5/7436A537-996F-4CD6-B553-9303BFB99348/wwdc2020_10004_hd.mp4
            session = line.split('/')[-1].split('.')[0].split('_')[1]
            print(session)
        else:
            #https://devstreaming-cdn.apple.com/videos/wwdc/2019/103bax22h2udxu0n/103/103_hd_platforms_state_of_the_union.mp4
            session = line.split('/')[-1].split('.')[0].split('_')[0]
            print(session)
        title = get_wwdc_video_title(year=year_id, session=session)
        print(title)
        # find the subtitle file
        if year_id >= 2021:
            subtitle_path  = subtitle_dir + 'wwdc' + str(year_id) + '-' + session + '_hd.srt'
        elif year_id == 2020:
            subtitle_path  = subtitle_dir + 'wwdc' + str(year_id) + '_' + session + '_hd.srt'
        else:
            filename = line.split('/')[-1].split('.')[0] + '.srt'
            subtitle_path  = subtitle_dir + filename
        if os.path.exists(subtitle_path):
            pass
        else:
            print('subtitle file not exists')
        session_dict[f'{year_id}_{session}'] = {
            'title': title,
            'video_url': line.strip(),
            'subtitle_path': subtitle_path
        }


# save to json file
with open(f'data/wwdc{year_id}_session.json', 'w') as f:
    f.write(json.dumps(session_dict, indent=4))