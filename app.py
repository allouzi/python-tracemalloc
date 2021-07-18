from flask import Flask, jsonify
import os,json

app = Flask(__name__)

def generate_data(num):
    numbers = int(num/8)
    data = []
    i=0
    for i in range(numbers):
        i=i+1
        data.append(i)
    return data

custom_list = []
@app.route('/')
def home():
    num = 20000 * 1024
    data = generate_data(num)
    custom_list.append(data)
    custom_list.append(custom_list)
    return jsonify({"msg":"Data generated"})

if __name__ == "__main__":
    app.run()