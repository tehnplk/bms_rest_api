import os
from flask import Flask, request, jsonify
from datetime import datetime,timezone, timedelta

from get_pt import get_pt_info
from post_data import post_data


from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


data_dummy = {
    "cid": "1111111111111",
    "hn": "111111111",
    "vn": "1111111111111",
    "prefix": "-",
    "first_name": "-",
    "last_name": "-",
    "patient_type": "O",
    "fullname": "ไม่พบข้อมูลผู้รับบริการ",
    "sex": 1,
    "birth": "1980-04-18",
}


@app.route("/tp/post_data_tp", methods=["POST"])
def post_data_tp():
    data = request.json
    print("post_data_tp", data)
    return jsonify({"status": "ok"}), 200


@app.route("/bp/post_data_bp_list", methods=["POST"])
def post_data_bp_list():
    return jsonify({"status": "ok"}), 200


@app.route("/bp/post_data_bp", methods=["POST"])
def post_data_bp():
    data = request.json
    print("post_data_bp", data)
    return jsonify({"status": "ok"}), 200


@app.route("/bmi/post_data_bmi", methods=["POST"])
def post_data_bmi():
    data = request.json
    print("post_data_bmi", data)
    resp = post_data(data)
    return resp, 200


@app.route("/patient/get_patient_by_hn/<hn>", methods=["GET"])
def get_hn(hn):
    if os.getenv("test") == "yes":
        data = {
            "cid": "3101600035300",
            "hn": "570000084",
            "vn": "680819131347",
            "prefix": "Mx.",
            "first_name": "สมชาย",
            "last_name": "สมสันต์",
            "patient_type": "O",
            "fullname": "นายสมชาย สมสันต์",
            "sex": 1,
            "birth": "1980-04-18",
        }
    else:
        try:
            pt = get_pt_info(hn)
            pt = pt.get("result")
            data = {
                "cid": pt.get("cid", ""),
                "hn": pt.get("hn", ""),
                "vn": pt.get("vn", ""),
                "prefix": pt.get("prefix", ""),
                "first_name": pt.get("first_name", ""),
                "last_name": pt.get("last_name", ""),
                "patient_type": "O",
                "fullname": f"{pt.get('prefix', '')} {pt.get('first_name', '')} {pt.get('last_name', '')}",
                "sex": 1,
                "birth": "1980-04-18",
            }
        except:
            data = data_dummy
    return jsonify(data), 200


@app.route("/patient/get_patient_by_vn/<vn>", methods=["GET"])
def get_vn(vn):
    if os.getenv("test") == "yes":
        data = {
            "cid": "3101600035300",
            "hn": "570000084",
            "vn": "680819131347",
            "prefix": "Mx.",
            "first_name": "สมชาย",
            "last_name": "สมสันต์",
            "patient_type": "O",
            "fullname": "นายสมชาย สมสันต์",
            "sex": 1,
            "birth": "1980-04-18",
        }
    else:
        try:
            pt = get_pt_info(vn)
            pt = pt.get("result")
            data = {
                "cid": pt.get("cid", ""),
                "hn": pt.get("hn", ""),
                "vn": pt.get("vn", ""),
                "prefix": pt.get("prefix", ""),
                "first_name": pt.get("first_name", ""),
                "last_name": pt.get("last_name", ""),
                "patient_type": "O",
                "fullname": f"{pt.get('prefix', '')} {pt.get('first_name', '')} {pt.get('last_name', '')}",
                "sex": 1,
                "birth": "1980-04-18",
            }
        except:
            data = data_dummy
    return jsonify(data), 200


@app.route("/patient/get_patient_by_cid/<cid>", methods=["GET"])
def get_cid(cid):
    if os.getenv("test") == "yes":
        data = {
            "cid": "1111111111111",
            "hn": "570000084",
            "vn": "680819131347",
            "prefix": "Mx.",
            "first_name": "สมชาย",
            "last_name": "สมสันต์",
            "patient_type": "O",
            "fullname": "นายสมชาย สมสันต์",
            "sex": 1,
            "birth": "1980-04-18",
        }
    else:
        try:
            pt = get_pt_info(cid)
            pt = pt.get("result")
            data = {
                "cid": pt.get("cid", ""),
                "hn": pt.get("hn", ""),
                "vn": pt.get("vn", ""),
                "prefix": pt.get("prefix", ""),
                "first_name": pt.get("first_name", ""),
                "last_name": pt.get("last_name", ""),
                "patient_type": "O",
                "fullname": f"{pt.get('prefix', '')} {pt.get('first_name', '')} {pt.get('last_name', '')}",
                "sex": 1,
                "birth": "1980-04-18",
            }
        except:
            data = data_dummy

    return jsonify(data), 200


@app.route("/patient/get_patient_by_an/<an>", methods=["GET"])
def get_an(an):
    if os.getenv("test") == "yes":
        data = {
            "cid": "3101600035300",
            "hn": "570000084",
            "vn": "680819131347",
            "prefix": "Mx.",
            "first_name": "สมชาย",
            "last_name": "สมสันต์",
            "patient_type": "O",
            "fullname": "นายสมชาย สมสันต์",
            "sex": 1,
            "birth": "1980-04-18",
        }
    else:
        try:
            pt = get_pt_info(an)
            pt = pt.get("result")
            data = {
                "cid": pt.get("cid", ""),
                "hn": pt.get("hn", ""),
                "an": pt.get("an", ""),
                "prefix": pt.get("prefix", ""),
                "first_name": pt.get("first_name", ""),
                "last_name": pt.get("last_name", ""),
                "patient_type": "O",
                "fullname": f"{pt.get('prefix', '')} {pt.get('first_name', '')} {pt.get('last_name', '')}",
                "sex": 1,
                "birth": "1980-04-18",
            }
        except:
            data = data_dummy
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
