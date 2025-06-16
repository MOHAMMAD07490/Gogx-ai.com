from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
generator = pipeline('text-generation', model='gpt2')

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    output = generator(prompt, max_length=50)
    return jsonify(output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
