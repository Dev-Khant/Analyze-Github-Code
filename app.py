from flask import Flask, request
from flask_cors import cross_origin

app = Flask(__name__)


@app.route("/", methods=["POST"])
@cross_origin()  # Avoid CORS errors
def process():
    data = request.get_json()
    openai_key = data.get("openaiKey")
    currentPageLink = data.get("currentPageLink")

    if openai_key and currentPageLink:
        print("Received OpenAI Key:", openai_key)
        print("Received Link:", currentPageLink)

        # Process the key in Python as needed
        return openai_key + "  " + currentPageLink
    else:
        return "Error"


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)
