import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
# tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", model_path="~/Downloads/coqui-XTTS-v2").to(device)
model_name = TTS().list_models()[0]
tts = TTS(model_path="/Users/zhangsan/Downloads/coqui-XTTS-v2", config_path="/Users/zhangsan/Downloads/coqui-XTTS-v2/config.json").to(device)

# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
#  speaker_wav="reference/dongdie/81-120_11.wav"
tts.tts_to_file(text="几颗大而亮的星星挂在夜空，仿佛是天上的人儿提着灯笼在巡视那浩瀚的太空。", speaker_wav="reference/dongdie/81-120_11.wav",
                language="zh", file_path="output_dongdie.wav")
