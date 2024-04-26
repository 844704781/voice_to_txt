# 将mp4中的音频提取成文字输出

## 使用方法

1. 需要有python环境
2. 安装依赖库

```shell
pip install -r requirements.txt
```

3. 将你的mp4文件放入mp4目录
4. 执行提取脚本

```shell
python main.py
```

5. 提取的文本将会出现在requirements.txt中

## 注意
> 该工具使用的是speech_recognition模块中google的接口，如果出现请求失败等字样，请检查您的网络