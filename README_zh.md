# wwdc_video_subtitle_downloader

中文 | [English](README.md)

## 这是什么

这是一个简单的脚本，用于下载 WWDC 视频和字幕。它可以下载指定的 WWDC session 视频和字幕，并且如果需要的话，可以将字幕翻译成其他语言。

请查看 `download` 文件夹中的示例。

# 如何使用
## 1. 安装

克隆这个仓库并安装所需的依赖。推荐使用 Python 虚拟环境。

```bash
# 克隆这个仓库
git clone git@github.com:veraposeidon/wwdc_video_subtitle_downloader.git
cd wwdc_video_subtitle_downloader

# 创建虚拟环境并激活
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

## 2. 运行

```bash
python3 main.py
```

首先，您将被要求输入要下载的视频的 session 编号。您可以在视频页面的 URL 中找到 session 编号，例如在 `https://developer.apple.com/videos/play/wwdc2023/10140/` 中的 `10140`。

然后，您将被询问是否要将字幕翻译成其他语言。如果需要翻译，请输入语言代码。如果不需要，请直接按回车键。如果您对语言代码不熟悉，可以在[语言支持](https://cloud.google.com/translate/docs/languages)中找到它们，在 *ISO-639* 代码列中查找代码。

之后，视频和字幕将会下载到 `./download` 文件夹中。


# 想要做贡献吗？

请随意提交一个 issue 或 pull request。

# 有问题或建议吗？

请提交一个 issue 或通过电子邮件联系我：veraposeidon@users.noreply.github.com

