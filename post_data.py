import requests
import json
from datetime import datetime, timezone, timedelta

import os

from get_pt import get_pt_info

from dotenv import load_dotenv

load_dotenv()


url = os.getenv("url")
end_point = f"{url}/vs/PostVitalsignService"
token = os.getenv("token")

hospital_code = os.getenv("hospital_code")
hospital_name = os.getenv("hospital_name")
company_name = os.getenv("company_name")
machine_name = os.getenv("machine_name")


def post_data(data):
    pt = get_pt_info(data.get("hn"))
    pt = pt.get("result")

    dt = (
        datetime.now(timezone(timedelta(hours=7)))
        .isoformat(timespec="milliseconds")
        .replace("+07:00", "Z")
    )

    data = data.get("data")

    body_weight = data.get("weight", "")
    body_height = data.get("height", "")
    bmi = data.get("bmi", "")
    body_temp = data.get("tp", "")
    bp_systolic = data.get("bps", "")
    bp_diastolic = data.get("bpd", "")
    pulse = data.get("pulse", "")

    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    payload = {
        "hospital": {
            "hospital_code": hospital_code,
            "hospital_name": hospital_name,
        },
        "device": {
            "company_name": company_name,
            "machine_name": machine_name,
        },
        "patient": {
            "cid": pt.get("cid", ""),
            "hn": pt.get("hn", ""),
            "vn": pt.get("vn", ""),
            "prefix": pt.get("prefix", ""),
            "first_name": pt.get("first_name", ""),
            "last_name": pt.get("last_name", ""),
            "patient_type": "O",
        },
        "vital_signs": {
            "body_weight": {"valueQuantity": {"value": body_weight, "unit": "kg"}},
            "body_height": {"valueQuantity": {"value": body_height, "unit": "cm"}},
            "bmi": {"valueQuantity": {"value": bmi, "unit": ""}},
            "body_temp": {"valueQuantity": {"value": body_temp, "unit": "cel"}},
            "bp_systolic": {"valueQuantity": {"value": bp_systolic, "unit": "mmHg"}},
            "bp_diastolic": {"valueQuantity": {"value": bp_diastolic, "unit": "mmHg"}},
            "pulse": {"valueQuantity": {"value": pulse, "unit": "bpm"}},
            # "respiratory_rate": {"valueQuantity": {"value": , "unit": "bpm"}},
            # "heartrate": {"valueQuantity": {"value": 73, "unit": "bpm"}},
            # "o2sat": {"valueQuantity": {"value": 98, "unit": ""}},
            # "dtx": {"valueQuantity": {"value": 115, "unit": "mg/dL"}},
            "vital_sign_datetime": dt,
        },
    }
    if os.getenv("test") != "yes":
        response = requests.post(end_point, headers=headers, json=payload)
        return response
    else:
        return {"status": "test-ok"}
