#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex

import os


class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7132282392:AAHWSjExwrcyshy7WgYXqYJOYvv-yMJLFIU
")

    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "29761366"))
    API_HASH = os.environ.get("API_HASH", "f895f8fd4d7fd7fc98b3d4108f6f2c66")
