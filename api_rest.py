import os
from flask import Flask, request, jsonify
from datetime import datetime

from get_pt import get_pt_info
from datetime import timezone, timedelta
import requests

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


def gen_date():
    dt1 = (
        datetime.now(timezone.utc)
        .isoformat(timespec="milliseconds")
        .replace("+00:00", "Z")
    )
    return dt1


def gen_date2():
    dt2 = (
        datetime.now(timezone(timedelta(hours=7)))
        .isoformat(timespec="milliseconds")
        .replace("+07:00", "Z")
    )
    return dt2


@app.route("/tp/post_data_tp", methods=["POST"])
async def post_data_tp():
    data = await request.json()
    print("post_data_tp", data)
    return jsonify({"status": "ok"}), 200


@app.route("/bp/post_data_bp_list", methods=["POST"])
async def post_data_bp_list():
    data = await request.json()
    print("post_data_bp_list", data)
    return jsonify({"status": "ok"}), 200


@app.route("/bp/post_data_bp", methods=["POST"])
async def post_data_bp():
    data = await request.json()
    print("post_data_bp", data)
    return jsonify({"status": "ok"}), 200


@app.route("/bmi/post_data_bmi", methods=["POST"])
async def post_data_bmi():
    data = await request.json()
    print("post_data_bmi", data)
    return jsonify({"status": "ok"}), 200


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

    return jsonify(data), 200


@app.route("/patient/get_patient_by_cid/<cid>", methods=["GET"])
def get_cid(cid):
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

    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
