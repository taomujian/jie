import wave
import numpy as np
from PIL import Image, ImageDraw

wav_A = wave.open("c424ffe6766148459efc80fb01bb1ae5/玩具车/L293_1_A1.wav", 'r')
wav_B = wave.open("c424ffe6766148459efc80fb01bb1ae5/玩具车/L293_1_B1.wav", 'r')
wav_En = wave.open("c424ffe6766148459efc80fb01bb1ae5/玩具车/L293_1_EnA.wav", 'r')

def read_wav(wav):
    num_frame = wav.getnframes()
    num_channel = wav.getnchannels()
    framerate = wav.getframerate()
    str_data = wav.readframes(num_frame)
    wave_data = np.fromstring(str_data, dtype = np.short)
    wave_data.shape = -1, num_channel
    return wave_data, framerate

def convert_level(level):
    if level != 0: return 1
    return 0

def draw(wav_A, wav_B, wav_En):
    wave_data_A, framerate_A = read_wav(wav_A)
    wave_data_B, framerate_B = read_wav(wav_B)
    wave_data_En, framerate_En = read_wav(wav_En)

    width = 4000
    height = 500
    im = Image.new('RGB',(width,height),'white')
    draw = ImageDraw.Draw(im)
    pos = [300, 300]
    direction = 1
    walk = 0

    cnt = 0
    rotate_cnt = 0
    for i in range(len(wave_data_A)):
        cnt += 1
        if cnt % 200 != 0: continue
        level_A = convert_level(wave_data_A[i][0])
        level_B = convert_level(wave_data_B[i][0])
        level_En = convert_level(wave_data_En[i][0])


        if level_En == 1:
            if level_A == 0 and level_B == 0:
                rotate_cnt = 0
                walk = 1
                draw.point((pos[0],pos[1]),'black')
                if direction == 0:
                    pos[0] -= 1
                if direction == 2:
                    pos[0] += 1
                if direction == 1:
                    pos[1] += 1
                if direction == 3:
                    pos[1] -= 1
            if level_A == 1 and level_B == 1:
                rotate_cnt = 0
                walk = 1
                draw.point((pos[0],pos[1]),'black')
                if direction == 0:
                    pos[0] += 1
                if direction == 2:
                    pos[0] -= 1
                if direction == 1:
                    pos[1] -= 1
                if direction == 3:
                    pos[1] += 1
            if level_A == 0 and level_B == 1:
                walk = 0
                rotate_cnt += 1
                if rotate_cnt % 40 == 0:
                    direction += 1
                    direction = direction % 4
            if level_A == 1 and level_B == 0:
                walk = 0
                rotate_cnt += 1
                if rotate_cnt % 40 == 0:
                    direction -= 1
                    if direction < 0: direction = 3

    im.show()

draw(wav_A, wav_B, wav_En)
