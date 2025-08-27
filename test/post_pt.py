import requests
import json
from datetime import datetime, timezone, timedelta

import os

from dotenv import load_dotenv

load_dotenv()

url = os.getenv("url")
token = os.getenv("token")
hospital_code = os.getenv("hospital_code")
hospital_name = os.getenv("hospital_name")
company_name = os.getenv("company_name")
machine_name = os.getenv("machine_name")


from get_pt import get_pt_info


def post_data(id, token):

    pt = get_pt_info(id, token)
    pt = pt.get("result")

    url = os.getenv("url")
    end_point = f"{url}/vs/PostVitalsignService"

    hosname = "โรงพยาบาลทดสอบ"
    hoscode = "99999"
    company_name = "TN Network"
    machine_name = "opd01"

    dt1 = (
        datetime.now(timezone.utc)
        .isoformat(timespec="milliseconds")
        .replace("+00:00", "Z")
    )
    dt2 = (
        datetime.now(timezone(timedelta(hours=7)))
        .isoformat(timespec="milliseconds")
        .replace("+07:00", "Z")
    )
    print("dt1", dt1)
    print("dt2", dt2)

    # GET with  Authorization  Bearer
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    payload = {
        "hospital": {
            "hospital_code": hoscode,
            "hospital_name": hosname,
        },
        "device": {
            "company_name": company_name,
            "machine_name": machine_name,
        },
        "patient": {
            "cid": pt.get("cid",""),
            "hn": pt.get("hn",""),
            "vn": pt.get("vn", ""),
            "prefix": pt.get("prefix",""),
            "first_name": pt.get("first_name",""),
            "last_name": pt.get("last_name",""),
            "patient_type": "O",
        },
        "vital_signs": {
            "body_weight": {"valueQuantity": {"value": 77.5, "unit": "kg"}},
            "body_height": {"valueQuantity": {"value": 165, "unit": "cm"}},
            "bmi": {"valueQuantity": {"value": 28.5, "unit": ""}},
            "body_temp": {"valueQuantity": {"value": 37.8, "unit": "cel"}},
            "bp_systolic": {"valueQuantity": {"value": 125, "unit": "mmHg"}},
            "bp_diastolic": {"valueQuantity": {"value": 88, "unit": "mmHg"}},
            "pulse": {"valueQuantity": {"value": 74, "unit": "bpm"}},
            "respiratory_rate": {"valueQuantity": {"value": 21, "unit": "bpm"}},
            "heartrate": {"valueQuantity": {"value": 73, "unit": "bpm"}},
            "o2sat": {"valueQuantity": {"value": 98, "unit": ""}},
            "dtx": {"valueQuantity": {"value": 115, "unit": "mg/dL"}},
            "vital_sign_datetime": dt2,
        },
    }

    response = requests.post(end_point, headers=headers, json=payload)
    return response


if __name__ == "__main__":
    token = os.getenv("token")

    CID = "3101600035349"
    HN1 = "570000084"
    VN = "680819131347"

    CID = "1709900185554"
    HN2 = "570000607"

    r = post_data(HN2, token)
    print(r.json())
