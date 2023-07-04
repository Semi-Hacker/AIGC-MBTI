# 首先需要提前安装open ai 以及requests包
# pip install openai
# pip install openai requests
# 
# 然后填入API Keys，可以在该网站上生成免费额度：
# https://platform.openai.com/account/api-keys

import openai
import requests

openai.api_key = ''

def get_mbti_type(dialogue):
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=dialogue,
        max_tokens=100, #由于处于测试阶段，输出内容限制100个字符以内，以节约算力成本开销
        n=1,
        stop=None,
        temperature=0.8
    )
    mbti_type = response.choices[0].text.strip()
    return mbti_type

dialogue = "Please analyze people A's MBTI personality type based on this conversation. You only need to tell the MBTI personality type of the speaker, which is a combination of four letters, without adding any further explanation. "+input("请输入对话内容。无论是单人还是双人对话形式，请均以A：或B：开头，其中待判断性格的人为A（比如：A：今天天气真好！好想出去玩！B：我想宅在家里面，追追剧多舒服啊）对话中间请避免空格、换行等非连续性字符")
with open('mbti.txt', 'r') as file:
    for line in file:
        if line.strip() in get_mbti_type(dialogue):
            print("说话人A的MBTI类型是：",line.strip())
            break
file.close

analysis=input("是否需要提供分析过程，需要请输入'Y'，不需要请输入'N'")

def analysis_mbti_type(dialogue):
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=dialogue,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.8
    )    
    analysis_mbti_type = response.choices[0].text.strip()
    return analysis_mbti_type

if analysis=='Y':
    print(analysis_mbti_type("Please give the analysis process of speaker A's mbti_type in Chinese"))
else:
    exit()
