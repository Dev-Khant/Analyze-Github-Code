from flask import Flask, request
from flask_cors import cross_origin

from analyze import AnalyzeRepo

app = Flask(__name__)


@app.route("/", methods=["POST"])
@cross_origin()  # Avoid CORS errors
def process():
    data = request.get_json()
    openai_key = data.get("openaiKey")
    currentPageLink = data.get("currentPageLink")

    if openai_key and currentPageLink:
        # Call AnalyzeRepo and get detailed summary
        summary_generator = AnalyzeRepo(openai_key, currentPageLink)
        result = summary_generator.run()

        return result
    else:
        return "Error"


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)
