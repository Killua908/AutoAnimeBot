#    This file is part of the AutoAnime distribution.
#    Copyright (c) 2023 Kaif_00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/kaif-00z/AutoAnimeBot/blob/main/LICENSE > .

from decouple import config


class Var:
    # Telegram Credentials

    API_ID = config("API_ID", default=27108998, cast=int)
    API_HASH = config("API_HASH", default="f4fc03493766db361d7e85ed8974fe2f")
    BOT_TOKEN = config("BOT_TOKEN", default=6068705272:AAE2kbM0_PWvnKJlbJl4KJzm0RVR_IYjy5k)

    # Database Credentials

    REDIS_URI = config("REDIS_URI", default=redis-14575.c83.us-east-1-2.ec2.cloud.redislabs.com:14575)
    REDIS_PASS = config("REDIS_PASSWORD", default=ewN4urDvP9qOG7t7aGFisSfjVq9ADyxO)

    # Channels Ids

    BACKUP_CHANNEL = config("BACKUP_CHANNEL", default=-1002067313192, cast=int)
    MAIN_CHANNEL = config("MAIN_CHANNEL", default=-1002027742156,cast=int)
    LOG_CHANNEL = config("LOG_CHANNEL", default=-1001976332443, cast=int)
    CLOUD_CHANNEL = config("CLOUD_CHANNEL", cast=int)
    OWNER = config("OWNER", default=5191566338, cast=int)

    # Other Configs

    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/37d9d0657d51e01a71f26.jpg"
    )
    FFMPEG = config("FFMPEG", default="ffmpeg")
    SEND_SCHEDULE = config("SEND_SCHEDULE", default=False, cast=bool)
    RESTART_EVERDAY = config("RESTART_EVERDAY", default=True, cast=bool)
