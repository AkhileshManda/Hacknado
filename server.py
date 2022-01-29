from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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

# run the server
if __name__ == '__main__':
    app.run(debug=True)