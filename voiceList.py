from enum import Enum  

class Voiceroid(Enum):
    """ボイロの声指定用enum"""
    YUKARI = "yukari_emo_44"
    """結月ゆかり"""
    AKANE = "akane_west_emo_44"
    """琴葉茜（関西弁）"""
    AOI = "aoi_emo_44"
    """琴葉葵"""

    def getVoice4Name(name):
        if name=="ゆかり":
            return Voiceroid.YUKARI
        elif name=="茜":
            return Voiceroid.AKANE
        elif name=="葵":
            return Voiceroid.AOI
        else:
            print("名前に該当なし：Voiceroid.getVoice4Name("+name+")")
            return None