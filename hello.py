from flask import Flask
import pandas as pd
app = Flask(__name__)

@app.route('/')
def read_file():
    with open ('app.json', 'r', encoding='utf8') as file:
        print(file.read())
    return

read_file()

if __name__ == '__main__':
    app.run()
