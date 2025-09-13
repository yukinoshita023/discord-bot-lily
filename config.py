import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

VOICE_CHANNEL_ID = 860122545381572608

# 女性の場合: ja-JP-NanamiNeural, 男性の場合: ja-JP-KeitaNeural
VOICE_MODEL = "ja-JP-NanamiNeural"