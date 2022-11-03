from query_utils import query_builder
from flask import request, jsonify
from requests import BatchRequest
from marshmallow import ValidationError
from flask import Flask

app = Flask(__name__)


@app.route("/perform_query", methods=["POST"])
def perform_query():
    input_data = request.json
    try:
        params = BatchRequest().load(data=input_data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    res = None
    for query in params['queries']:
        res = query_builder(
            cmd=query['cmd'],
            value=query['value'],
            data=res
        )
    return jsonify(res)


if __name__ == "__main__":
    app.run()
