
# wwdc_video_subtitle_downloader

English | [中文](README_zh.md)

## what is this

this is a simple script to download wwdc video and subtitle. it will download the specified wwdc session video and subtitle, and translate the subtitle to other languages if you want.

see `download` folder for example.


# how to use
## 1. install

clone this repository and install requirements. use python virtual environment is recommended.

```bash
# clone this repository
git clone git@github.com:veraposeidon/wwdc_video_subtitle_downloader.git
cd wwdc_video_subtitle_downloader

# create virtual environment and activate it
python3 -m venv venv
source venv/bin/activate

# install requirements
pip install -r requirements.txt
```

## 2. run

```bash
python3 main.py
```

first you will be asked to input the session number of the video you want to download.
you can find the session number in the url of the video page. like `10140` in `https://developer.apple.com/videos/play/wwdc2023/10140/`.


then you will be asked if you want to translate the subtitle to other languages. if you want, input the language code. if not, just press enter.
if you not familiar with language code, you can find it in [Language support](https://cloud.google.com/translate/docs/languages), find code in *ISO-639* code column.

after that, the video and subtitle will be downloaded to `./download` folder.


# want to contribute?

feel free to open an issue or pull request.

# have a question? or any suggestion?

open an issue or contact me via email: veraposeidon@users.noreply.github.com
