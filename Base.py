import voiceList
import talk
import csv
import os
import pygame
import time
import random
from mutagen.mp3 import MP3

def makeMusicList(file_path):
    """ファイル内のファイルを取得する"""
    #"X:/XXX/XXXX/music"
    musicList=[]
    #musicList.append("0_test")テスト用ショート音源
    for item in os.listdir(file_path):
        if os.path.splitext(item)[1]==".mp3":
            musicList.append(os.path.splitext(item)[0])
    return musicList

def makeScript():
    """台本を作成する"""
    csv_file = open("./script.csv", "r", encoding="utf-8", errors="", newline="" )
    #リスト形式
    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    #辞書形式
    f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    header = next(f)
    print(header)
    list = []
    for row in f:
        #row[0]で必要な項目を取得することができる
        #print(row)
        list.append(row)
    return list
    

musicDir = "X:/XXXXX/XXXX"
musicList=makeMusicList(musicDir)
scriptList=makeScript()

random.shuffle(musicList)
random.shuffle(scriptList)

musicCnt = len(musicList)
scriptCnt = len(scriptList)
num=0

for item in musicList:
    if(num>musicCnt):
        break #曲がなくなったら終了
    if(num>scriptCnt):
        #台詞がなくなったらリストから再追加
        musicList=makeScript(musicDir)
        random.shuffle(scriptList)
    filename =musicList[num];
    filePath = musicDir+"/"+filename+".mp3";
    audio = MP3(filePath)
    mp3_length = audio.info.length #音源の長さ取得
    talk.talk(voiceList.Voiceroid.getVoice4Name(scriptList[num][1]).value, scriptList[num][2])
    talk.talk(voiceList.Voiceroid.getVoice4Name(scriptList[num][1]).value, "次の曲は"+filename+"です")
    pygame.mixer.init(frequency = 44100)
    pygame.mixer.music.load(filePath)
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(0.3)
    time.sleep(mp3_length)
    if(mp3_length>60):
        pygame.mixer.music.fadeout(5000)
    pygame.mixer.music.stop()
    num+=1
talk.talk(voiceList.Voiceroid.YUKARI.value, "リストの曲はこれで最後ですね。お疲れ様でした。")
