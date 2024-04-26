import os
import speech_recognition as sr
import moviepy.editor as mp
import logging

logging.getLogger("moviepy").setLevel(logging.ERROR)


def extract_audio_to_text(mp4_file, txt_file):
    # 创建语音识别器
    recognizer = sr.Recognizer()

    # 使用moviepy提取音频
    audio_clip = mp.AudioFileClip(mp4_file)
    total_duration = audio_clip.duration  # 获取音频总时长
    # print("音频总时长:", total_duration, "秒")

    # 初始化进度计数器
    current_time = 0

    # 循环处理音频
    while current_time < total_duration:
        # 计算本次处理的时间范围
        start_time = current_time
        end_time = min(current_time + 10, total_duration)  # 每次处理10秒，不超过总时长
        # print("处理时间范围:", start_time, "-", end_time, "秒")

        # 提取当前时间范围内的音频
        audio_segment = audio_clip.subclip(start_time, end_time)
        audio_segment.write_audiofile("temp.wav", logger=None)

        # 识别音频文件
        with sr.AudioFile("temp.wav") as source:
            audio_data = recognizer.record(source)

        # 使用CMU Sphinx进行语音识别
        try:
            # print("开始识别...")
            print(f"{mp4_file}---->{txt_file},进度:{round(start_time / total_duration, 4) * 100}%")
            text = recognizer.recognize_google(audio_data, language='zh-CN')
            with open(txt_file, "a") as f:  # 追加模式写入文本
                f.write(text + "\n")
            print(f"{mp4_file}---->{txt_file},进度:{round(end_time / total_duration, 4) * 100}%")
            # print("识别成功！")
        except sr.UnknownValueError:
            print("无法识别音频！")
        except sr.RequestError as e:
            print("请求错误：", e)

        # 更新进度计数器
        current_time = end_time

    # 删除临时音频文件
    os.remove("temp.wav")


# 调用函数并传入mp4文件路径和要保存文本的txt文件路径

file_names = os.listdir("./mp4")
for file_name in file_names:
    txt_name = file_name.replace("mp4", "txt")
    mp4_file = "./mp4/" + file_name
    txt_file = "./txt/" + txt_name
    extract_audio_to_text(mp4_file, txt_file)
