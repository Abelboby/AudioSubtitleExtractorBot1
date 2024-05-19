#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex

from pyrogram import Client

#from config import Config

if __name__ == "__main__":
    plugins = dict(root="plugins")
    app = Client("SubtitleExtractBot",bot_token=Config.BOT_TOKEN,
                 api_id=Config.APP_ID,
                 api_hash=Config.API_HASH,
                 plugins=plugins,
                 workers=300)
    app.run()
