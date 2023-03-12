import os
from flask import Flask, jsonify,request
from flask_cors import CORS
import pymysql
from threading import Lock
from dbutils.pooled_db import PooledDB
import json
app = Flask(__name__)
CORS(app)

# 定义一个计数器，用于记录已经连接到数据库的客户端数量
connection_count = 0
# 定义一个锁，用于保证对计数器的修改是线程安全的
counter_lock = Lock()
# 定义一个常量，表示最大连接尝试次数
MAX_CONNECTION_ATTEMPTS = 3

pool = PooledDB(
    creator=pymysql,  # 使用pymysql作为连接器
    maxconnections=5,  # 最大连接数
    blocking=True,  # 连接数达到最大时是否阻塞
    host='localhost', port=3306, user='root', password='hbh0526'
)

@app.route('/data2')
def get_data2():
    global connection_count
    with counter_lock:
        connection_count += 1
        if connection_count > MAX_CONNECTION_ATTEMPTS:
            return 'Connection refused. Too many attempts.'
    conn = pool.connection();
    try:

        strValue = request.args.get('str')
        print(strValue)
        cursor = conn.cursor()
        cursor.execute("UPDATE minichatgpt.`q&a` SET HotValue = HotValue + 1 WHERE questions = '"+strValue+"';")
        conn.commit()
        data=[]
        for i in cursor.fetchall():
            data.append({'id':i[0],'questions':i[1],'answers': i[2], 'HotValue':i[3]});
        print(data)
        cursor.close()
        conn.close()
        with counter_lock:
            connection_count -= 1
        return jsonify(data)
    except Exception as e :
        print(e)
        with counter_lock:
            connection_count -= 1
        return 'Failed to connect to database.'
@app.route('/data')
def get_data():
    global connection_count
    with counter_lock:
        connection_count += 1
        if connection_count > MAX_CONNECTION_ATTEMPTS:
            return 'Connection refused. Too many attempts.'
    conn = pool.connection();
    try:
        strValue = request.args.get('str')

        print('Connection')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM minichatgpt.`q&a`;")
        print('Sucees')
        data=[]
        for i in cursor.fetchall():
            data.append({'id':i[0],'questions':i[1],'answers': i[2], 'HotValue':i[3]});
        print(data)
        cursor.close()
        conn.close()
        print('Connection')
        with counter_lock:
            connection_count -= 1
        return jsonify(data)
    except Exception as e:

        with counter_lock:
            connection_count -= 1
        return 'Failed to connect to database.'
@app.route('/DataPost',methods=['POST'])
def process_data():
    data = request.json
    indicator = data['Indicator']
    json_data = json.loads(data['JsonData'])
    print(json_data)
    if indicator == "update":
        update_messages(json_data)
        print(messages)
        return jsonify({'success': True})
    elif indicator == "geturl":
        url = save_messages()
        return jsonify({'url': url})
    else:
        return jsonify({'error': 'Invalid indicator'})

def update_messages(data):
    global messages
    messages = data;
    print(messages)

def save_messages():
    folder_path = r'D:\user\hbh\Downloads\element-plus-vite-starter-main\element-plus-vite-starter-main\src\components\chatdata'
    file_path = os.path.join(folder_path, 'messages.json')
    with open(file_path, 'w') as f:
        json.dump(messages, f)
    # 返回本地文件路径
    return file_path

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
