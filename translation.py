import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

class Translation(object):
    START_TEXT = f"""Hii,
I am Mega.nz Downloader bot!
Just send me any mega.nz File link, I will return you that file on telegram"""
    
    DOWNLOAD_START = "📥Downloading..."
    UPLOAD_START = "📤Uploading..."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS =  "✅Your File is successfully Downloaded!"
    SAVED_CUSTOM_THUMB_NAIL = "☑️This thumbnail is saved to my database, I will add this thumbnail when you Download next video file.\nUse /deletethumbnail to delete that thumbnail right now!"
    DEL_ETED_CUSTOM_THUMB_NAIL = "🟢Thumbnail successfully deleted!"

    HELP_USER = f"""Using this bot is straight Forward, Just send me mega link to get that file.
Send image file anytime to set that image as thumbnail.
You can use /deletethumbnail to delete that thumbnail.
"""
