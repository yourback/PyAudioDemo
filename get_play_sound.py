import pyaudio
import wave

# 声音块
CHUNK = 1024
# 音频文件内容格式
FORMAT = pyaudio.paInt16
# 声道数目
CHANNELS = 2
# 音频频率
RATE = 44100
# 录音时长
RECORD_SECONDS = 20
# 生成文件名称
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()
# 新建输入音频流
stream_in = p.open(format=FORMAT,
                   channels=CHANNELS,
                   rate=RATE,
                   input=True,
                   output=True,
                   frames_per_buffer=CHUNK)

# 新建输出音频流
stream_out = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=CHUNK)

print("* playing")
# 新建数组
frames = []
# 音频流数据以块为单位放入数组
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    # data = stream_in.read(CHUNK)
    # frames.append(data)
    stream_out.write(stream_in.read(CHUNK))

print("* done playing")
# 停止输入音频流
stream_in.stop_stream()
# 关闭输入音频流
stream_in.close()
# 停止输出音频流
stream_out.stop_stream()
# 关闭输出音频流
stream_out.close()
# 录音终止
p.terminate()

# # 写入音频文件
# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# # 设置声道数目
# wf.setnchannels(CHANNELS)
# # 设置采样大小
# wf.setsampwidth(p.get_sample_size(FORMAT))
# # 设置音频频率
# wf.setframerate(RATE)
# # 数组写入数据
# wf.writeframes(b''.join(frames))
# # 写入完毕
# wf.close()
