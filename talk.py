"""ボイスロイドを発話用ラッパー"""
import voiceList
import pyvcroid2
import threading
import time
import winsound

def display_phonetic_label(tts_events):
    start = time.perf_counter()
    now = start
    for item in tts_events:
        tick = item[0] * 0.001
        type = item[1]
        if type != pyvcroid2.TtsEventType.PHONETIC:
            continue
        while (now - start) < tick:
            time.sleep(tick - (now - start))
            now = time.perf_counter()
        value = item[2]
        print(value, end="", flush=True)
    print("")

def talk(voiceValue:voiceList, text):
    """ボイスロイドを発話させる
        Args:
        voice (voiceList): キャラをvalueで指定
        text (文字列): 台詞を指定
    """
    with pyvcroid2.VcRoid2() as vc:
        vc.loadLanguage("standard")
        vc.loadVoice(voiceValue)
        speech, tts_events = vc.textToSpeech(text)
        
        t = threading.Thread(target=display_phonetic_label, args=(tts_events,))
        t.start()
        winsound.PlaySound(speech, winsound.SND_MEMORY)
        t.join()
