from pydub import AudioSegment
from pydub.playback import play

#读取想要倒放的音频文件 
ted = AudioSegment.from_file("nanjing_1.mp3")
#将音频倒转
backwards = ted.reverse()
#保存倒放的音频
backwards.export("nanjing_2.mp3")
#播放倒放文件 
play(backwards)