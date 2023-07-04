# 首先需要提前安装open ai 以及requests包
# pip install openai
# pip install openai requests
# 
# 然后填入API Keys，可以在该网站上生成免费额度：
# https://platform.openai.com/account/api-keys

import openai
import requests

openai.api_key = ''

########## phase 1 ##########
dialogue2=""
with open('questions.txt','r') as file2:
    for line2 in file2:
        line2=line2.strip()
        dialogue2=line2+input(line2+"是，请输入Yes；否，请输入No")+"."
dialogue2="Please analyze the MBTI type of this individual based on his responses to these questions. You only need to tell his MBTI personality type!"+dialogue2

def get_mbti_type(dialogue2):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=dialogue2,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.8
    )    
    get_mbti_type = response.choices[0].text.strip()
    return get_mbti_type

with open('mbti.txt', 'r') as file:
    for line in file:
        if line.strip() in get_mbti_type(dialogue2):
            print("您的MBTI类型是：",line)
            line = line.strip()
            break

with open('pair_type.txt', 'r',encoding='utf-8') as file3:
    lines3 = file3.readlines() 
    for i in range(len(lines3)):
        line3 = lines3[i].strip()
        if line3 in line:
            print("根据对于您性格的分析，您的爱情观与适合的伴侣性格为：")
            if i + 1 < len(lines3):
                print(lines3[i + 1].strip())
            if i + 2 < len(lines3):
                print(lines3[i + 2].strip()) 
            break  

########## phase 2 ##########
mbti_A=input("请输入对话人A的MBTI类型：")
mbti_B=input("请输入对话人B的MBTI类型：")
print("请输入对话内容,请以A：或B：开头（如A：今天天气真好！好想出去玩！B：我想宅在家里面，追追剧多舒服啊。对话中间请避免空格、换行等非连续性字符）：")
phase2_dialogue = input()
phase2_dialogue = "请你给予MBTI性格理论只给出中文分析：以下这段聊天记录中的A和B是否适合成为【情侣】？他们有什么匹配或不匹配的地方？Please DO NOT CONTINUE THIS CONVERSATION! JUST ANALYSE！对话如下："+phase2_dialogue+"其中，说话人A的MBTI是"+mbti_A+"说话人A的MBTI是"+mbti_B
def be_couple(dialogue):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=dialogue,
        max_tokens=800,
        n=1,
        stop=None,
        temperature=0.6
    )    
    couple = response.choices[0].text.strip()
    return couple

print(be_couple(phase2_dialogue))
