# encoding: utf-8
import re
from googletrans import Translator

target_language = ''
# read srt file
def read_srt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# parse srt content, extract time and subtitle
def parse_srt_content(content):
    content = '\n' + content
    print(content)
    pattern = r'\n(\d+)\n(\d{2}:\d{2}:\d{2}[,.]\d{3}) --> (\d{2}:\d{2}:\d{2}[,.]\d{3}) .+\n([\s\S]*?)(?=\n\n|$)'
    matches = re.findall(pattern, content)
    # print(matches)
    continues_matches = []
    new_matches = []
    for match in matches:
        print('------------------')
        subtitle_number, time_start, time_end, subtitle_text = match
        print(f"Subtitle Number: {subtitle_number}")
        print(f"Time Desc: {time_start}, {time_end}")
        print(f"Subtitle Text: {subtitle_text}")
        # if subtitle_text not end with symbol [.,?!，。？！♪]
        if not re.search(r'[.?!。？！♪]$', subtitle_text):
            continues_matches.append(match)
            continue
        else:
            if len(continues_matches) > 0:
                time_start = continues_matches[0][1]
                time_end = match[2]
                time_sec = f'{time_start} --> {time_end}'
                subtitle_text = ' '.join([match[3] for match in continues_matches]) + ' ' + match[3]
                new_matches.append((subtitle_number, time_sec, subtitle_text))
                continues_matches = []
            else:
                time_sec = f'{time_start} --> {time_end}'
                new_matches.append((subtitle_number, time_sec, subtitle_text))
        
    return new_matches

# translate subtitle
def translate_subtitle(subtitle):
    print(f"Subtitle: {subtitle}")
    translator = Translator()
    result = translator.translate(text=subtitle, src='en', dest=target_language)
    print(f"Translated Subtitle: {result}")
    return result.text

# translate srt file
def translate_srt_file(file_path):
    content = read_srt_file(file_path)
    subtitles = parse_srt_content(content)
    translated_subtitles = []

    subtitle_numbers = []
    time_secs = []
    subtitle_texts = []

    # store subtitle_number, time_sec, subtitle_text
    for subtitle in subtitles:
        subtitle_number, time_sec, subtitle_text = subtitle
        subtitle_numbers.append(subtitle_number)
        time_secs.append(time_sec)
        subtitle_texts.append(subtitle_text)
    
    # structure like: [[0, text], [95, text]]
    cues_text_list = []
    for (index, subtitle_text) in enumerate(subtitle_texts):
        if len(cues_text_list) > 0 and (len(cues_text_list[len(cues_text_list) - 1][1]) + len(subtitle_text)) < 3000:
            # need to insert a separator(\n\n) for split after translated
            # remove \n in subtitle_text, because it will affect the translation result
            cues_text_list[len(cues_text_list) - 1][1] += '\n\n' + subtitle_text.replace('\n', ' ')
        else:
            cues_text_list.append([index, subtitle_text.replace('\n', ' ')])
    
    # translate
    for (index, cues_text) in enumerate(cues_text_list):
        print(f"translate {index} subtitle")
        translated_texts = translate_subtitle(cues_text[1])
        translatedTextList = translated_texts.split('\n\n')
        for (jndex, translatedText) in enumerate(translatedTextList):
            subtitle_texts[cues_text[0] + jndex] = translatedText + '\n' + subtitle_texts[cues_text[0] + jndex].replace('\n', ' ')
    
    # organize translated content
    translated_content = ''
    for (index, subtitle_text) in enumerate(subtitle_texts):
        translated_content += f'{subtitle_numbers[index]}\n{time_secs[index]}\n{subtitle_text}\n\n'

    return translated_content


def translate(src_file_path, dest_file_path, target_lang='zh-CN'):
    global target_language
    target_language = target_lang
    translated_content = translate_srt_file(src_file_path)
    print('------------------save to file------------------')
    with open(dest_file_path, 'w', encoding='utf-8') as file:
        file.write(translated_content)
