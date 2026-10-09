from zhipuai import ZhipuAI

# 替换成你最新的密钥，保留引号！
api_key = "你的密钥"

print("准备使用的密钥是：【", api_key, "】")

client = ZhipuAI(api_key=api_key)

try:
    response = client.chat.completions.create(
        model="glm-4-flash",
        messages=[{"role": "user", "content": "你好"}]
    )
    print("成功啦！", response.choices[0].message.content)
except Exception as e:
    print("依然失败，完整报错：", e)