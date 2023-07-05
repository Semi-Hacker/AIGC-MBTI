# AIGC-MBTI
面向下沉市场：AIGC与MBTI结合性格测试交互产品

## 简介
_______ 是一款AIGC与MBTI相结合的性格测试交互产品
![image](https://github.com/Semi-Hacker/AIGC-MBTI/assets/138411034/91783d1f-346a-43d8-bae5-62d61b1c0dde)

### 用户画像
下沉市场（即三四线城市）中40-50岁的有相亲交友需求的男女用户
### 应用场景
1. 将产品嵌入相亲交友APP、微信小程序、Web端网站，使用chatbot交互式界面学习用户的MBTI特征，供用户在相亲匹配以及聊天过程中作参考
2. 直接对用户聊天进行语义分析，分析用户MBTI特征，推送给用户，同时加入到匹配系统中


## 数据
1111
2222


## 效果展示
### Phase 1：用户输入选择题答案  
- I try not to draw attention to myself?是，请输入Yes；否，请输入No 
- I feel uncomfortable when I disagree with someone?是，请输入Yes；否，请输入No  
- I lose my belongings?是，请输入Yes；否，请输入No 
- I have a vivid imagination?是，请输入Yes；否，请输入No 
- I would enjoy attending a large party in my honor?是，请输入Yes；否，请输入No  
- I dislike being in competition with others?是，请输入Yes；否，请输入No 
- I prefer to follow a schedule?是，请输入Yes；否，请输入No 
- I question the wisdom of my elders?是，请输入Yes；否，请输入No 
- I enjoy being the center of attention?是，请输入Yes；否，请输入No  
- I try to avoid conflict?是，请输入Yes；否，请输入No  
- I make sure my work is finished on time?是，请输入Yes；否，请输入No  
- It is important to me to follow traditions?是，请输入Yes；否，请输入No  
- I make an effort to be popular?是，请输入Yes；否，请输入No  
- I sympathize with the homeless?是，请输入Yes；否，请输入No   
- I have trouble controlling my impulses?是，请输入Yes；否，请输入No  
- I think about why people do the things they do?是，请输入Yes；否，请输入No  
- Being around lots of people energizes me?是，请输入Yes；否，请输入No  
- I am helpful to the people around me?是，请输入Yes；否，请输入No  
- I am ambitious?是，请输入Yes；否，请输入No  
- I like to do things as they were done in the past?是，请输入Yes；否，请输入No  
- I avoid being alone?是，请输入Yes；否，请输入No  
### Phase 2：调用OPEN AI接口，输出MBTI以及对应的爱情观和适合的伴侣性格  
**您的MBTI类型是：** INFJ  
根据对于您性格的分析，您的爱情观与适合的伴侣性格为：  
爱情观：爱情在我的脑海里，在我的心灵里，在我的灵魂里  
适配人格：ENTP，INFP，ENFP，INTP  
### Phase 3：输入A与B的MBTI类型，以及A与B的聊天记录  
请输入对话人A的MBTI类型：ENTJ  
请输入对话人B的MBTI类型：ENFP  
请输入对话内容,请以A：或B：开头（如A：今天天气真好！好想出去玩！B：我想宅在家里面，追追剧多舒服啊。对话中间请避免空格、换行等非连续性字符）：  
A：你好，请问你Olivia是吗？B：是的，你好。A：我是Max，很高兴见到你。听说你喜欢经历不一样的生活，可以跟我分享一下吗？B：是的，我觉得生活中有很多不同的 
事情和经历，我希望能够尝试不同的生活方式，认识不同的人和文化，让自己更加开放和充实。A：我也很认同你的观点。你平时有什么兴趣和爱好吗？B：我喜欢旅游和尝
试新的美食，也喜欢阅读和看电影，认为这些可以让我更好地了解世界和人性。A：听起来很有意思啊，我也喜欢旅游和美食，最近去了趟日本，感觉非常不错。B：哇，日
本是我的梦想旅行地之一，你觉得怎么样？A：非常不错，特别是食物和文化，非常值得一去。B：我也想去一次！A：那我们可以一起去啊，如果你愿意的话。不过，我也 
想在事业上取得更大的成功，你对事业有什么想法吗？B：我认为事业很重要，也希望自己能够在工作中有所成就。我目前在一家财务公司工作，但也在考虑未来的发展和 
转型。A：我也非常重视事业发展，希望能够在自己的职业生涯中不断挑战和提高自己。你在工作中遇到过什么挑战吗？B：我觉得最大的挑战就是要不断学习和更新自己的
知识和技能，因为金融行业的发展速度非常快，我们需要不断地跟进和提高自己。A：对，这个非常重要，我也在不断地学习和提升自己的技能和能力。你觉得未来的职业 
发展方向是什么？B：我觉得未来的职业发展方向可能会更加数字化和智能化，需要掌握更多的技术和数据分析的能力。A：我也觉得，我们需要不断学习和提高自己的技能
和能力，才能跟上时代的步伐。B：我也完全同意你的观点。如果有机会，我们可以分享一下自己的学习和成长经历。A：好的，那我们可以先交换联系方式，以后再商量细
节。B：好的，我把我的微信号给你。A：好的，我加你微信。
### Phase 4：调用OPEN AI接口，分析双方成为情侣的匹配程度  
根据MBTI性格理论，A和B可能适合成为情侣，因为他们都喜欢旅游、尝试新的美食、阅读、看电影，共同喜欢探索世界和人性，有一定的共同点，可以给他们的关系带来更
多的活力和激情。此外，他们都重视事业的发展，都希望自己能够在工作中有所成就，可以通过分享彼此的学习和成长经历给关系带来更多的支持和帮助。然而，A和B在性
格上存在一定差异，A属于外向性格的ENTJ，他喜欢领导别人，喜欢发挥自己的能力，而B属于内向性格的ENFP，他喜欢分析思考，喜欢探索新的事物，因此，A和B在性格上
有一定的不匹配，可能会给他们的关系带来一定的挑战。

## 未来计划
### 商业模式
我们参考了市面上主流的交友相亲类产品，最终决定采用【虚拟币购买单次服务+订阅制】的形式：
- 单次测试服务10金币，测试结果分析20金币，匹配度程度10金币，匹配程度结果分析20金币
- VIP：每月5次测试服务、看访客
- SVIP：在VIP的基础上，每月5次分析服务、MBTI专属群组权限、个性图标

### 功能优化
- 状态：主打短暂心情，加入各个关键词选项（如美滋滋、胡思乱想、玩游戏、听歌）
- 动态：主打长期个人特质&关键节点，如运动习惯、换城市/工作
- 名片：兴趣爱好、对另一半的期待等；当亲密值上升后，可逐级解锁游戏账号、抖音账号等
- 亲密值设计：使用MBTI测试、送礼、聊天等，可以增加亲密值
- 娱乐：一起听歌、一起唱歌，满足中老年休闲的需求

