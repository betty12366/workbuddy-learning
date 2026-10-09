from zhipuai import ZhipuAI

# 在这里填入你最新的密钥，注意：一定要保留双引号！
# 智谱的密钥格式通常是 xxxxxxxx.yyyyyyyy（中间必须有一个英文小数点）
api_key = "你的密钥"

# 这一步非常关键！打印出来看看到底读到了什么
print("----- 实际读取到的密钥是：【", api_key, "】 -----")

client = ZhipuAI(api_key=api_key)

try:
    response = client.chat.completions.create(
        model="glm-4-flash",
        messages=[{"role": "user", "content": "你好"}]
    )
    print("✅ 成功！", response.choices[0].message.content)
except Exception as e:
    print("❌ 依然失败：", e)
