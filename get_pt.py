import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()

url = os.getenv("url")
end_point = f"{url}/vs/GetPatientInfo"
hosname = "โรงพยาบาลทดสอบ"
hoscode = "99999"
company_name = "TN Network"
machine_name = "opd01"


def get_pt_info(id, token):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    if len(id) == 13:
        payload = {"hospital_code": hoscode, "hospital_name": hosname, "cid": id}
    elif len(id) == 9:
        payload = {"hospital_code": hoscode, "hospital_name": hosname, "hn": id}
    elif len(id) == 12:
        payload = {"hospital_code": hoscode, "hospital_name": hosname, "vn": id}
    else:
        return "Invalid ID"

    response = requests.get(end_point, headers=headers, params=payload)
    # json.dumps(response.json(), indent=4, ensure_ascii=False)
    return response.json()


if __name__ == "__main__":
    token = os.getenv("token")

    CID = "3101600035349"
    HN1 = "570000084"
    VN = "680819131347"

    CID = "1709900185554"
    HN2 = "570000607"

   
    resp1 = get_pt_info(HN1, token)
    print(resp1.get("result"))

    resp2 = get_pt_info(HN2, token)
    print(resp2.get("result"))
    
