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
file_path = 'data/wwdc2023_hd_video_links.txt'
subtitle_dir = 'data/WWDC_2023_Video_Subtitles/HD/'
session_dict = {}
with open(file_path, 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # https://devstreaming-cdn.apple.com/videos/wwdc/2023/10309/4/21D925C8-2EE0-4C96-9C68-96174159990A/downloads/wwdc2023-10309_hd.mp4
        year = line.split('/')[-1].split('.')[0].split('-')[0].removeprefix('wwdc')
        print(year)
        session = line.split('/')[-1].split('.')[0].split('-')[-1].removesuffix('_hd')
        print(session)
        title = get_wwdc_video_title(year=year, session=session)
        print(title)
        # find the subtitle file
        subtitle_path  = subtitle_dir + 'wwdc' + year + '-' + session + '_hd.srt'
        if os.path.exists(subtitle_path):
            pass
        else:
            print('subtitle file not exists')
        session_dict[year+'_'+session] = {
            'title': title,
            'video_url': line.strip(),
            'subtitle_path': subtitle_path
        }


# save to json file
with open('data/wwdc_session.json', 'w') as f:
    f.write(json.dumps(session_dict, indent=4))