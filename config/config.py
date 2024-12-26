# GPT 相关配置
# model list
model_quester_anster = "text-davinci-003"
model_gpt_35_turbo = "gpt-3.5-turbo"
model_programming_translate = "code-davinci-002"
model4free = "gpt-4o-mini-2024-07-18"
# gpt key
openai_api_key = "EXAMPLE"

# openai api
openai_baseurl = "https://api.moonshot.cn/v1"

# gpt model
openai_model_name = "moonshot-v1-8k"

# 2. 提示词
gpt_message = """
         你是一位资深编程专家，gitlab的分支代码变更将以git diff 字符串的形式提供，请你帮忙review本段代码。然后你review内容的返回内容必须严格遵守下面的格式，包括标题内容。模板中的变量内容解释：变量5是代码中的优点儿 变量1是给review打分，分数区间为0~100分。 变量2 是code review发现的问题点。  变量3是具体的修改建议。变量4是你给出的修改后的代码。 必须要求：1. 以精炼的语言、严厉的语气指出存在的问题。2. 你的反馈内容必须使用严谨的markdown格式 3. 不要携带变量内容解释信息。4. 有清晰的标题结构。有清晰的标题结构。有清晰的标题结构。
返回格式严格如下：



### 😀代码评分：{变量1}

#### ✅代码优点：
{变量5}

#### 🤔问题点：
{变量2}

#### 🎯修改建议：
{变量3}

#### 💻修改后的代码：
```python
{变量4}

         """

# -------------Gitlab info------------------
# Gitlab url
gitlab_server_url = "http://192.168.1.28:8000/"

# Gitlab private token
gitlab_private_token = "glpat-TS97bxB9MVfGuVu_SSWP"

# Gitlab modifies the maximum number of files
maximum_files = 50


# ------------- Message notification --------------------
# dingding notification （un necessary）
dingding_bot_webhook = "https://open.feishu.cn/open-apis/bot/v2/hook/fffe39c9-2bf9-4d4b-ab8a-62d89c2121ac"
dingding_secret = "ghXvCPAi6krHDmW2GXTdsc"
