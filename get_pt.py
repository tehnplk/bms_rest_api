import requests
import json

import os

from dotenv import load_dotenv

load_dotenv()

url = os.getenv("url")
token = os.getenv("token")
end_point = f"{url}/vs/GetPatientInfo"
hospital_code = os.getenv("hospital_code")
hospital_name = os.getenv("hospital_name")
company_name = os.getenv("company_name")
machine_name = os.getenv("machine_name")


def get_pt_info(id):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    if len(id) == 13:
        payload = {
            "hospital_code": hospital_code,
            "hospital_name": hospital_name,
            "cid": id,
        }
    elif len(id) == 9:
        payload = {
            "hospital_code": hospital_code,
            "hospital_name": hospital_name,
            "hn": id,
        }
    elif len(id) == 12:
        payload = {
            "hospital_code": hospital_code,
            "hospital_name": hospital_name,
            "vn": id,
        }
    else:
        return "Invalid ID"

    response = requests.get(end_point, headers=headers, params=payload)
    # json.dumps(response.json(), indent=4, ensure_ascii=False)
    return response.json()


if __name__ == "__main__":

    CID = "3101600035300"   
    HN = "570000000"
    VN = "680819131347"
    
    resp = get_pt_info(HN)
    print(resp.get("result"))
