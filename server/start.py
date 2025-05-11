from flask import Flask, request
from flask_cors import CORS
import json

from settings import API_BASE_URL, SERVER_HOST, SERVER_PORT

app = Flask(__name__)
CORS(app)

base_url = API_BASE_URL

stories = {}
passages = {}

def load_from_file():
    global stories
    global passages
    try:
        with open('stories.json', 'r') as f:
            stories = json.loads(f.read())
        with open('passages.json', 'r') as f:
            passages = json.loads(f.read())
    except FileNotFoundError:
        print('files not found')
        pass

def save_to_file():
    with open('stories.json', 'w') as f:
        f.write(json.dumps(stories, indent=2))
    with open('passages.json', 'w') as f:
        f.write(json.dumps(passages, indent=2))

@app.route(f"{base_url}/save/story", methods=["POST"])
def save_story():
    story_data = request.get_json()
    stories[story_data['id']] = story_data
    save_to_file()
    return {
    }


@app.route(f"{base_url}/save/passage", methods=["POST"])
def save_passage():
    passage_data = request.get_json()
    passages[passage_data['id']] = passage_data
    save_to_file()
    return {
    }

@app.route(f"{base_url}/delete/passage/<passage_id>", methods=["DELETE"])
def delete_passage(passage_id):
    del passages[passage_id]
    save_to_file()
    return {
    }

@app.route(f"{base_url}/get/passage/<passage_id>", methods=["GET"])
def get_passage(passage_id):
    return passages[passage_id]


@app.route(f"{base_url}/stories", methods =["GET"])
def get_stories():
    return stories

@app.route(f"{base_url}/passages", methods=["GET"])
def get_passages():
    return passages


if __name__ == '__main__':
    load_from_file()
    app.run(SERVER_HOST, SERVER_PORT)
