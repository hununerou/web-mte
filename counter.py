import json
from flask import Flask

app = Flask(__name__)


@app.route('/')
def top_page():
    try:
        with open('./counter.json', 'r') as f:
            counter_data = json.load(f)
    except FileNotFoundError:
        counter_data = {'count': 0}
    counter_data['count'] += 1
    with open('./counter.json', 'w') as f:
        json.dump(counter_data, f, indent=4)
    #return f"あなたは{counter_data['count']}人目のお客様です。"
    return ''


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
