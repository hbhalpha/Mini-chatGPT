import os
import requests

# 请求页面
url = 'http://localhost:5173'
response = requests.get(url)

# 检查响应状态码
if response.status_code == 200:
    # 获取桌面路径
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    # 拼接保存文件路径
    save_path = os.path.join(desktop_path, 'chatIndex.html')
    # 将响应内容写入文件
    with open(save_path, 'wb') as f:
        f.write(response.content)
    print(f'已保存文件到 {save_path}')
else:
    print('请求失败')
