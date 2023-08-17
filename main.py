# encoding: utf-8
import json
import youtube_dl
import os
from translate_subtitle import translate
import shutil

# helper: download video
def download_video(video_url, dest_path):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # set video quality
        'outtmpl': dest_path,  # set output dir
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# get input
year_id = input('which year?[2023,2022,2021,2020,2019]: ')
if year_id not in ['2023', '2022', '2021', '2020', '2019']: 
    print('year not support')
    exit(0)
session_id = input('input session id: ')

# read json 
with open(f'data/wwdc{year_id}_session.json', 'r') as f:
    session_dct = json.load(f)
    key = f'{year_id}_{session_id}'
    # check if session id exists
    if key not in session_dct.keys():
        print('session id not exists')
        exit(0)
    values = session_dct[key]
    video_url = values['video_url']
    title = values['title']
    print(title)
    subtitle_path = values['subtitle_path']
    # destination path
    # remove rest after ` - WWDC`
    title = title.split(' - WWDC')[0]
    # title = title.replace(' - WWDC23 - Videos - Apple Developer', '').strip()
    dest_dir = f'download/{year_id}-{session_id}-{title}'

    should_download_video = input('download video? (y/n): ')
    should_download_video = should_download_video.lower()

    should_translate_subtitle = input('translate subtitle? (y/n): ')
    should_translate_subtitle = should_translate_subtitle.lower()
    if should_translate_subtitle == 'y':
        print("check language code in [Language support](https://cloud.google.com/translate/docs/languages)")
        dual_subtitle_target_lang = input('dual subtitle target language (default: zh-CN): ')

    # make dir
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    # download video
    if should_download_video == 'y':
        download_video(video_url, dest_dir + f'/{session_id}-{title}.mp4')
    # translate subtitle
    if should_translate_subtitle == 'y':
        if dual_subtitle_target_lang == '':
            dual_subtitle_target_lang = 'zh-CN'
        translate(subtitle_path, dest_dir + f'/{session_id}-{title}.srt', dual_subtitle_target_lang)
    else:
        # copy subtitle file to dest dir
        target_subtitle_path = dest_dir + f'/{session_id}-{title}.srt'
        shutil.copyfile(subtitle_path, target_subtitle_path)
    print('done')
    print('find your video and subtitle in ' + dest_dir)