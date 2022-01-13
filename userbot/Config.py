import os

from telethon.tl.types import ChatBannedRights

ENV = bool(os.environ.get("ENV", False))


class Var(object):
    APP_ID = int(os.environ.get("APP_ID", 6))
    # 6 is a placeholder
    LIGHTNING_PRO = os.environ.get("LIGHTNING_PRO", None)
    if not LIGHTNING_PRO:
        LIGHTNING_PRO = "YES"
    else:
        LIGHTNING_PRO = LIGHTNING_PRO

    API_HASH = os.environ.get("API_HASH", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./userbot/DOWNLOADS/")
    BIO_MSG = os.environ.get("BIO_MSG", None)
    ALIVE_MESSAGE = os.environ.get("ALIVE_MESSAGE", None)

    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", )
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/usr/bin/chromedriver")
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "/usr/bin/google-chrome")
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    # Here for later purposes
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "1311769691").split())
    WHITELIST_USERS = set(
        int(x) for x in os.environ.get("WHITELIST_USERS", "1311769691").split()
    )
    MAX_ANTI_FLOOD_MESSAGES = 10
    # warn mode for anti flood
    ANTI_FLOOD_WARN_MODE = ChatBannedRights(
        until_date=None, view_messages=None, send_messages=True
    )
    BLACKLIST_USERS = set(int(x) for x in os.environ.get("BLACKLIST_USERS", "").split())
    DEVLOPERS = set(int(x) for x in os.environ.get("DEVLOPERS", "1311769691").split())
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1311769691").split())
    SUPPORT_USERS = set(int(x) for x in os.environ.get("SUPPORT_USERS", "").split())
    # custom vars
    CUSTOM_ALIVE = os.environ.get("CUSTOM_ALIVE", None)
    CUSTOM_ALIVE_EMOJI = os.environ.get("CUSTOM_ALIVE_EMOJI", None)
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)
    SUDO_HNDLR = os.environ.get("SUDO_HNDLR", r"\!")
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)
    ALIVE_MSG = os.environ.get("ALIVE_MSG", None)
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    CUSTOM_STICKER_PACK_NAME = os.environ.get("CUSTOM_STICKER_PACK_NAME", None)
    NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", True))
    PMBOT_START_MSSG = os.environ.get("PMBOT_START_MSSG", None)
    LESS_SPAMMY = os.environ.get("LESS_SPAMMY", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    CUSTOM_ALIVE = os.environ.get("CUSTOM_ALIVE", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
    TAG_LOG = os.environ.get("TAG_LOG", None)
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
    MAX_FLOOD_IN_P_M_s = os.environ.get("MAX_FLOOD_IN_P_M_s", "3")
    COMBINED_GROUP_ID = int(os.environ.get("COMBINED_GROUP_ID", -100))
    PLUGIN_CHANNEL = os.environ.get("PLUGIN_CHANNEL", f"{COMBINED_GROUP_ID}")
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    MAX_MESSAGE_SIZE_LIMIT = 4095
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    CMD_HNDLR = os.environ.get("CMD_HNDLR", "\.")
    TAG_FEATURE = os.environ.get("TAG_FEATURE", "DISABLE")
    PM_DATA = os.environ.get("PM_DATA", "ENABLE")
    MAX_SPAM = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 5))
    SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME", None)
    NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD = int(
        os.environ.get("NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD", 10)
    )
    NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD = int(
        os.environ.get("NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD", 7)
    )
    EMOJI_TO_DISPLAY_IN_HELP = os.environ.get("EMOJI_TO_DISPLAY_IN_HELP", "〄𝕭〄")
    SPOTIFY_PASS = os.environ.get("SPOTIFY_PASS", None)
    G_BAN_LOGGER_GROUP = int(os.environ.get("G_BAN_LOGGER_GROUP", -1001291663564))
    SPOTIFY_BIO_PREFIX = os.environ.get("SPOTIFY_BIO_PREFIX", None)
    ASSISTANT_LOG = int(os.environ.get("ASSISTANT_LOG", False))
    UPSTREAM_REPO = os.environ.get(
        "UPSTREAM_REPO", "https://github.com/KeinShin/Black-Lightning"
    )
    ALIVE_PIC = os.environ.get(
        "ALIVE_IMAGE", "https://telegra.ph/file/63abc60224dc567e3d441.jpg"
    )
    CUSTOM_ALIVE_PIC = os.environ.get(
        "CUSTOM_ALIVE_IMG", "https://telegra.ph/file/50e422f6b07fa9126c1d1.jpg"
    )
    ALIVE_IMAGE = os.environ.get(
        "ALIVE_PIC", "https://telegra.ph/file/63abc60224dc567e3d441.jpg"
    )
    ASSISTANT_START_PIC = os.environ.get(
        "ASSISTANT_START_PIC",
        "https://telegra.ph/file/63abc60224dc567e3d441.jpg",
    )
    TESSDATA_PREFIX = os.environ.get(
        "TESSDATA_PREFIX", "/usr/share/tesseract-ocr/4.00/tessdata"
    )
    OPEN_LOAD_LOGIN = os.environ.get("OPEN_LOAD_LOGIN", None)
    OPEN_LOAD_KEY = os.environ.get("OPEN_LOAD_KEY", None)
    NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", False))
    ENABLE_ASSISTANTBOT = os.environ.get("ENABLE_ASSISTANTBOT", "ENABLE")
    PM_DATA = os.environ.get("PM_DATA", "ENABLE")
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "Lightning")
    ANTISPAM_FEATURE = os.environ.get("ANTISPAM_FEATURE", "ENABLE")
    ANTI_SPAMINC_TOKEN = os.environ.get("ANTI_SPAMINC_TOKEN", None)
    ASSISTANT_LOG = int(os.environ.get("ASSISTANT_LOG", False))
    PRIVATE_GROUP_BOT_API_ID = os.environ.get("PRIVATE_GROUP_BOT_API_ID",  f"{COMBINED_GROUP_ID}")
    if PRIVATE_GROUP_BOT_API_ID:
        PRIVATE_GROUP_BOT_API_ID = int(PRIVATE_GROUP_BOT_API_ID)
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    PMSECURITY = os.environ.get("PMSECURITY", "ON")
    # for autopic
    AUTOPIC_TEXT = os.environ.get(
        "AUTOPIC_TEXT", "Life Is too Short.\n And so is your TG account."
    )
    AUTO_PIC_FONT = os.environ.get("AUTOPIC_FONT", "DejaVuSans.ttf")
    AUTOPIC_FONT_COLOUR = os.environ.get("AUTOPIC_FONT_COLOUR", None)
    if AUTH_TOKEN_DATA is not None:
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        t_file = open(TEMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    LOAD_MYBOT = os.environ.get("LOAD_MYBOT", "True")
    UB_BLACK_LIST_CHAT = set(
        int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split()
    )
    PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID",  f"{COMBINED_GROUP_ID}")
    if PRIVATE_GROUP_ID is not None:
        try:
            PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
        except ValueError:
            raise ValueError(
                "Invalid Private Group ID. Make sure your ID is starts with -100 and make sure that it is only numbers."
            )

    PM_LOGGR_BOT_API_ID = os.environ.get("PM_LOGGR_BOT_API_ID",  f"{COMBINED_GROUP_ID}")
    if PM_LOGGR_BOT_API_ID:
        PM_LOGGR_BOT_API_ID = int(PM_LOGGR_BOT_API_ID)


class Development(Var):

    LOGGER = True
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/usr/bin/chromedriver")
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "/usr/bin/google-chrome")

    # Here for later purposes


if ENV:

    class Config(object):
        LOGGER = True
        CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/usr/bin/chromedriver")
        GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "/usr/bin/google-chrome")
        # Get this value from my.telegram.org! Please do not steal
        LOCATION = os.environ.get("LOCATION", None)
        OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
        COMBINED_GROUP_ID = int(os.environ.get("COMBINED_GROUP_ID", -100))
        # Get your own ACCESS_KEY from
        # http://api.screenshotlayer.com/api/capture
        SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get(
            "SCREEN_SHOT_LAYER_ACCESS_KEY", None
        )
        # Send .get_id in any channel to fill this value. ReQuired for
        # @Manuel15 inspiration to work!
        PRIVATE_CHANNEL_BOT_API_ID = int(
            os.environ.get("PRIVATE_CHANNEL_BOT_API_ID",  f"{COMBINED_GROUP_ID}")
        )
        # This is required for the plugins involving the file system.
        TMP_DOWNLOAD_DIRECTORY = os.environ.get(
            "TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/"
        )
        CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
        GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)
        # This is required for the speech to text module. Get your USERNAME
        # from
        # https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
        IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
        IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
        # This is required for the hash to torrent file functionality to work.
        HASH_TO_TORRENT_API = os.environ.get(
            "HASH_TO_TORRENT_API", "https://example.com/torrent/{}"
        )
        # This is required for the @telegraph functionality.
        TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "Black-Lightning")
        # Get a Free API Key from OCR.Space
        OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
        # Send .get_id in any group with all your administration bots (added)
        G_BAN_LOGGER_GROUP = int(os.environ.get("G_BAN_LOGGER_GROUP",  f"{COMBINED_GROUP_ID}"))
        # TG API limit. An album can have atmost 10 media!
        GOOGLE_SEARCH_COUNT_LIMIT = int(os.environ.get("GOOGLE_SEARCH_COUNT_LIMIT", 9))
        TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
        # Telegram BOT Token from @BotFather
        TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
        TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
        #
        NO_SONGS = bool(os.environ.get("NO_SONGS", False))
        #
        CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/usr/bin/chromedriver")
        GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "/usr/bin/google-chrome")

        # DO NOT EDIT BELOW THIS LINE IF YOU DO NOT KNOW WHAT YOU ARE DOING
        # TG API limit. A message can have maximum 4096 characters!
        MAX_MESSAGE_SIZE_LIMIT = 4095
        # set blacklist_chats where you do not want userbot's features
        UB_BLACK_LIST_CHAT = set(
            int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split()
        )
        # maximum number of messages for antiflood
        MAX_ANTI_FLOOD_MESSAGES = 10
        # warn mode for anti flood
        ANTI_FLOOD_WARN_MODE = ChatBannedRights(
            until_date=None, view_messages=None, send_messages=True
        )
        # chat ids or usernames, it is recommended to use chat ids,
        # providing usernames means an additional overhead for the user
        CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
        # Get your own API key from https://www.remove.bg/ or
        # feel free to use http://telegram.dog/Remove_BGBot
        REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
        # Set to True if you want to block users that are spamming your PMs.
        SLAP_USERNAME = os.environ.get("SLAP_USERNAME", None)
        GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
        GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
        NO_P_M_SPAM = bool(os.environ.get("NO_P_M_SPAM", False))
        # define "spam" in PMs
        MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
        # set to True if you want to log PMs to your PM_LOGGR_BOT_API_ID
        NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", False))
        # send .get_id in any channel to forward all your NEW PMs to this group
        PM_LOGGR_BOT_API_ID = os.environ.get("PM_LOGGR_BOT_API_ID",  f"{COMBINED_GROUP_ID}")
        if PM_LOGGR_BOT_API_ID:
            PM_LOGGR_BOT_API_ID = int(PM_LOGGR_BOT_API_ID)
        # For Databases
        # can be None in which case plugins requiring
        # DataBase would not work
        DB_URI = os.environ.get("DATABASE_URL", None)
        # number of rows of buttons to be displayed in .helpme command
        NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD = int(
            os.environ.get("NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD", 5)
        )
        # specify command handler that should be used for the plugins
        # this should be a valid "regex" pattern
        CMD_HNDLR = os.environ.get("CMD_HNDLR", r"\.")
        SUDO_HNDLR = os.environ.get("SUDO_HNDLR", r"\!")
        # specify list of users allowed to use bot
        # WARNING: be careful who you grant access to your bot.
        # malicious users could do ".exec rm -rf /*"
        SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
        # VeryStream only supports video formats
        VERY_STREAM_LOGIN = os.environ.get("VERY_STREAM_LOGIN", None)
        VERY_STREAM_KEY = os.environ.get("VERY_STREAM_KEY", None)
        GROUP_REG_SED_EX_BOT_S = os.environ.get(
            "GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot"
        )
        TEMP_DIR = os.environ.get("TEMP_DIR", None)
        CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
        # Google Chrome Stuff
        CHROME_BIN = os.environ.get("CHROME_BIN", "/usr/bin/google-chrome")
        CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/usr/bin/chromedriver")
        # Google Drive ()
        G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
        G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
        GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
        AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
        if AUTH_TOKEN_DATA is not None:
            os.makedirs(TMP_DOWNLOAD_DIRECTORY)
            t_file = open(TMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
            t_file.write(AUTH_TOKEN_DATA)
            t_file.close()
        YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
        GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
        # MongoDB
        MONGO_URI = os.environ.get("MONGO_URI", None)
        # TAG LOG GROUP
        TAG_LOG = os.environ.get("TAG_LOG", None)
        # PMSECURITY
        MAX_SPAM = int(os.environ.get("MAX_SPAM", 3))
        # Lydia API
        LYDIA_API = os.environ.get("LYDIA_API", None)
        FBAN_GROUP_ID = os.environ.get("FBAN_GROUP_ID", None)
        if FBAN_GROUP_ID:
            FBAN_GROUP_ID = int(FBAN_GROUP_ID)
        EXCLUDE_FED = os.environ.get("EXCLUDE_FED", None)


else:

    class Config(object):
        DB_URI = None
        CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/usr/bin/chromedriver")
        GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "/usr/bin/google-chrome")


        # Add your extra vars if any here
