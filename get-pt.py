import requests
import json

ip = "26.44.109.104:8555"
end_point = f"http://{ip}/vs/GetPatientInfo"
hosname = "โรงพยาบาลทดสอบ"
hoscode = "99999"
company_name = "TN Network"
machine_name = "opd01"

CID = "1361000126531"
HN = "580002328"
VN = "680814103517"
#HN = "570000607"


# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb21wYW55IjoiWEVHOWk5d3R3SnZWVldGUHBEQzJyZz09IiwiZGV2aWNlcyI6InVFaTBCMHZQMnZBODBYbExSbCtpU2c9PSIsImhvc3Bjb2RlIjoiUzFNVVppZ3JDb3JuT3kwbGJtRXFTUT09IiwiZW5jcnlwdGVkIjoiVmxhMEJVb1JIeVRVRGM3cmhxcFcyZz09IiwiZXhwIjoiMTc1NTYyMjc5OSIsImlhdCI6MTc1NTE0MjEyM30.pjtjySH_e_5INprzGlsoHIReiFOZ13ndh0i66gaEKLc"

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb21wYW55IjoiWEVHOWk5d3R3SnZWVldGUHBEQzJyZz09IiwiZGV2aWNlcyI6InVFaTBCMHZQMnZBODBYbExSbCtpU2c9PSIsImhvc3Bjb2RlIjoiMGZDaTVVM1BWWDRTQVNhRDVLb01KQT09IiwiZW5jcnlwdGVkIjoiVmxhMEJVb1JIeVRVRGM3cmhxcFcyZz09IiwiZXhwIjoiMTc1NTYyMjc5OSIsImlhdCI6MTc1NTE1MjUzMn0.L59AcjT2p01fixqlEHr63ZFvANTljOpdsdKo_RuY_d8"

# GET with  Authorization  Bearer
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

payload = {"hospital_code": hoscode, "hospital_name": hosname, "cid": CID}

response = requests.get(end_point, headers=headers, params=payload)
print(json.dumps(response.json(), indent=4, ensure_ascii=False))
