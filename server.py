from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import random
import pandas as pd

app = Flask(__name__)
CORS(app)

# PUT YOUR WEBSITE STUFF IN THE TEMPLATES DIRECTORY

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_event')
def get_event():
    event_id = request.args.get('event_id')

    temp_data = {
        'event_id': event_id,
        'event_name': 'Event Name',
        'event_description': 'Event Description',
        'event_location': 'Event Location',
        'event_date': 'Event Date',
        'event_time': 'Event Time',
        'tweets_list': [
            "1487385441292754946",
            "1486846468887560201",
            "1487295769749168128",
            "1486827458632503297",
            "1486753860555358216"
        ]
    }

    return jsonify(temp_data)

@app.route("/create_event", methods=['POST'])
def create_event():
    hashtags = request.form.get('hashtags')
    event_location = request.form.get('event_location')
    event_date = request.form.get('event_date')
    event_type = request.form.get('event_type')

    event_id = random.randint(100000, 999999)

    update_db({
        'event_id': event_id,
        'relevent_hashtags': hashtags,
        'event_location': event_location,
        'event_date': event_date,
        'event_type': event_type,
        "recent_tweets": "",
        "is_active": True
    })

    return jsonify({
        'event_id': event_id,
        'event_name': 'Event Name',
        'event_description': 'Event Description',
        'event_location': 'Event Location',
        'event_date': 'Event Date',
        'event_time': 'Event Time',
        'tweets_list': [
            "1487385441292754946",
            "1486846468887560201",
            "1487295769749168128",
            "1486827458632503297",
            "1486753860555358216"
        ]
    })

@app.route("/list")
def list():
    items = {}
    for i in db.index:
        items[i] = db.loc[i].to_dict()
    
    return jsonify(items)

# Eg: /untrack/<id>
@app.route("/untract")
def update_event():
    event_id = request.args.get('event_id')
    db.loc[db['event_id'] == event_id, 'is_active'] = "no"
    return "Event untracked"

db = pd.read_csv("./data/data.csv")
def update_db(_dict):
    db = db.append(_dict, ignore_index=True)
    db.to_csv("./data/data.csv", index=False)
    pass
# run the server
if __name__ == '__main__':
    app.run(debug=True)