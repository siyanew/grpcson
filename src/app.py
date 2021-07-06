import json
import os
import re
import subprocess

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)


@app.route("/")
def index():
    try:
        services = subprocess.check_output(
            ["grpcurl", "--plaintext", f"{HOST}:{PORT}", "list"]
        )
        return render_template('index.html', services=services.decode().splitlines())
    except Exception as e:
        return str(e)


@app.route("/<service>")
def service(service):
    try:
        methods = subprocess.check_output(
            ["grpcurl", "--plaintext", f"{HOST}:{PORT}", "list", service]
        )
        return render_template('service.html', title=service, brand_title=service, service=service,
                               methods=methods.decode().splitlines())
    except Exception as e:
        return str(e)


@app.route("/<service>/<method_name>", methods=['GET'])
def method_get(service, method_name):
    try:
        method = subprocess.check_output(
            ["grpcurl", "--plaintext", f"{HOST}:{PORT}", "describe", method_name]
        ).decode()

        regex = r"rpc.*(\(.*\)).*(\(.*\))"

        req, res = re.findall(regex, method, re.MULTILINE)[0]
        req = req.strip('(.) ')
        res = res.strip('(.) ')

        req = subprocess.check_output(
            ["grpcurl", "--plaintext", f"{HOST}:{PORT}", "describe", req]
        ).decode().splitlines()[1:]

        res = subprocess.check_output(
            ["grpcurl", "--plaintext", f"{HOST}:{PORT}", "describe", res]
        ).decode().splitlines()[1:]

        return render_template('method.html', title=method_name, brand_title=method_name, method_name=method_name,
                               res=res, req=req)
    except Exception as e:
        return str(e)


@app.route("/<service>/<method_name>", methods=['POST'])
def method_post(service, method_name):
    try:
        result = subprocess.check_output(
            ["grpcurl", "-d", json.dumps(request.form), "-plaintext", f"{HOST}:{PORT}",
             method_name]
        )
        print(json.loads(result))
        return jsonify(json.loads(result))
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5912)
