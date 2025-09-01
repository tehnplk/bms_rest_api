import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timezone, timedelta
from typing import Optional, Dict, Any
import uvicorn

from get_pt import get_pt_info
from post_data import post_data

from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="BMS REST API", version="1.0.0")

# Add CORS middleware
test = os.getenv("test", "no")

# Add CORS middleware if not in test mode
if test != "yes":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Pydantic models for request bodies
class PostDataRequest(BaseModel):
    hn: str
    data: Dict[str, Any]

class PostDataBPRequest(BaseModel):
    # Define the structure based on your actual data
    pass

class PostDataTPRequest(BaseModel):
    # Define the structure based on your actual data
    pass

class PostDataBMIRequest(BaseModel):
    hn: str
    data: Dict[str, Any]

# Error data
data_err = {
    "cid": "เกิดข้อผิดพลาด",
    "hn": "เกิดข้อผิดพลาด",
    "vn": "เกิดข้อผิดพลาด",
    "prefix": "เกิดข้อผิดพลาด",
    "first_name": "เกิดข้อผิดพลาด",
    "last_name": "เกิดข้อผิดพลาด",
    "patient_type": "เกิดข้อผิดพลาด",
    "fullname": "เกิดข้อผิดพลาด",
    "sex": "เกิดข้อผิดพลาด",
    "birth": "เกิดข้อผิดพลาด",
}

@app.post("/tp/post_data_tp")
async def post_data_tp(data: PostDataTPRequest):
    print("post_data_tp", data)
    return {"status": "ok"}

@app.post("/bp/post_data_bp_list")
async def post_data_bp_list():
    return {"status": "ok"}

@app.post("/bp/post_data_bp")
async def post_data_bp(data: PostDataBPRequest):
    print("post_data_bp", data)
    return {"status": "ok"}

@app.post("/bmi/post_data_bmi")
async def post_data_bmi(request: PostDataBMIRequest):
    data = {"hn": request.hn, "data": request.data}
    print("post_data_bmi", data)
    resp = post_data(data)
    return resp

@app.get("/patient/get_patient_by_hn/{hn}")
async def get_hn(hn: str):
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
        except Exception as e:
            print('err_get_pt', e)
            data = data_err
    return data

@app.get("/patient/get_patient_by_vn/{vn}")
async def get_vn(vn: str):
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
        except Exception as e:
            print('err_get_pt', e)
            data = data_err
    return data

@app.get("/patient/get_patient_by_cid/{cid}")
async def get_cid(cid: str):
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
        except Exception as e:
            print('err_get_pt', e)
            data = data_err

    return data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000, log_level="info")
