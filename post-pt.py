import requests
import json
from datetime import datetime, timezone

ip = "26.44.109.104:8555"
end_point = f"http://{ip}/vs/PostVitalsignService"
hosname = "โรงพยาบาลทดสอบ"
hoscode = "99999"
company_name = "TN Network"
machine_name = "opd01"

CID = "1361000126531"
HN = "580002328"
VN = "680814103517"


dt = (
    datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
)


# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb21wYW55IjoiWEVHOWk5d3R3SnZWVldGUHBEQzJyZz09IiwiZGV2aWNlcyI6InVFaTBCMHZQMnZBODBYbExSbCtpU2c9PSIsImhvc3Bjb2RlIjoiUzFNVVppZ3JDb3JuT3kwbGJtRXFTUT09IiwiZW5jcnlwdGVkIjoiVmxhMEJVb1JIeVRVRGM3cmhxcFcyZz09IiwiZXhwIjoiMTc1NTYyMjc5OSIsImlhdCI6MTc1NTE0MjEyM30.pjtjySH_e_5INprzGlsoHIReiFOZ13ndh0i66gaEKLc"

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb21wYW55IjoiWEVHOWk5d3R3SnZWVldGUHBEQzJyZz09IiwiZGV2aWNlcyI6InVFaTBCMHZQMnZBODBYbExSbCtpU2c9PSIsImhvc3Bjb2RlIjoiMGZDaTVVM1BWWDRTQVNhRDVLb01KQT09IiwiZW5jcnlwdGVkIjoiVmxhMEJVb1JIeVRVRGM3cmhxcFcyZz09IiwiZXhwIjoiMTc1NTYyMjc5OSIsImlhdCI6MTc1NTE1MjUzMn0.L59AcjT2p01fixqlEHr63ZFvANTljOpdsdKo_RuY_d8"

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
        "cid": CID,
        "hn": HN,
        "vn": VN,
        "prefix": "นาย",
        "first_name": "ธนายุต",
        "last_name": "รวมธรรม",
        "patient_type": "O",
    },
    "vital_signs": {
        "body_weight": {"valueQuantity": {"value": 78.5, "unit": "kg"}},
        "body_height": {"valueQuantity": {"value": 167, "unit": "cm"}},
        "bmi": {"valueQuantity": {"value": 28.5, "unit": ""}},
        "body_temp": {"valueQuantity": {"value": 36.8, "unit": "cel"}},
        "bp_systolic": {"valueQuantity": {"value": 129, "unit": "mmHg"}},
        "bp_diastolic": {"valueQuantity": {"value": 89, "unit": "mmHg"}},
        "pulse": {"valueQuantity": {"value": 72, "unit": "bpm"}},
        "respiratory_rate": {"valueQuantity": {"value": 22, "unit": "bpm"}},
        "heartrate": {"valueQuantity": {"value": 82, "unit": "bpm"}},
        "o2sat": {"valueQuantity": {"value": 98, "unit": ""}},
        "dtx": {"valueQuantity": {"value": 120, "unit": "mg/dL"}},
        "vital_sign_dattime": dt,
    },
}

response = requests.post(end_point, headers=headers, json=payload)
print(json.dumps(response.json(), indent=4, ensure_ascii=False))
