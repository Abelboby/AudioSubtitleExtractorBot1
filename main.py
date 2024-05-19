#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex

from pyrogram import Client

#from config import Config

if __name__ == "__main__":
    plugins = dict(root="plugins")
    app = Client("SubtitleExtractBot",
                 bot_token="7132282392:AAHWSjExwrcyshy7WgYXqYJOYvv-yMJLFIU",
                 api_id="29761366",
                 api_hash="f895f8fd4d7fd7fc98b3d4108f6f2c66",
                 plugins=plugins,
                 workers=300)
    app.run()
