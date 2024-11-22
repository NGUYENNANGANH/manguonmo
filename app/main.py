# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, EmailStr
# from typing import List
# from datetime import datetime
# from motor.motor_asyncio import AsyncIOMotorClient
# from bson import ObjectId
# from .models import Donation

# # Khởi tạo FastAPI
# app = FastAPI()

# # Kết nối MongoDB (Motor)
# client = AsyncIOMotorClient("mongodb+srv://admin:12345678@cluster0.a77gm.mongodb.net/final")
# db = client["donation_system"]  # Tên database
# donation_collection = db["donations"]  # Tên collection

# # Convert ObjectId thành string
# def donation_serializer(donation) -> dict:
#     return {
#         "id": str(donation["_id"]),
#         "Bank_Account_Number": donation["Bank_Account_Number"],
#         "Bank_Name": donation["Bank_Name"],
#         "Campaign_Name": donation["Campaign_Name"],
#         "Contact_Information": donation["Contact_Information"],
#         "Donation_Amount": donation["Donation_Amount"],
#         "Donation_Type": donation["Donation_Type"],
#         "Name": donation["Name"],
#         "Note": donation.get("Note", ""),
#         "Quantity_of_Goods": donation["Quantity_of_Goods"],
#         "Status": donation["Status"],
#         "Type_of_Goods": donation.get("Type_of_Goods", ""),
#         "Unit": donation.get("Unit", ""),
#         "date": donation["date"],
#     }

# # Route POST - Tạo quyên góp mới
# @app.post("/donations/")
# async def create_donation(donation: Donation):
#     donation_dict = donation.dict(exclude_unset=True)
#     result = await donation_collection.insert_one(donation_dict)
#     created_donation = await donation_collection.find_one({"_id": result.inserted_id})
#     return {"message": "Donation created", "donation": donation_serializer(created_donation)}

# # Route GET - Lấy danh sách tất cả quyên góp
# @app.get("/donations/", response_model=List[Donation])
# async def get_donations():
#     donations = []
#     async for donation in donation_collection.find():
#         donations.append(donation_serializer(donation))
#     return donations

# # Route GET - Lấy chi tiết quyên góp theo ID
# @app.get("/donations/{donation_id}", response_model=Donation)
# async def get_donation(donation_id: str):
#     donation = await donation_collection.find_one({"_id": ObjectId(donation_id)})
#     if donation is None:
#         raise HTTPException(status_code=404, detail="Donation not found")
#     return donation_serializer(donation)





















# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, EmailStr
# from typing import List
# from datetime import datetime
# from motor.motor_asyncio import AsyncIOMotorClient
# from bson import ObjectId
# from .models import Donation

# # Khởi tạo FastAPI
# app = FastAPI()

# # Kết nối MongoDB (Motor)
# client = AsyncIOMotorClient("mongodb+srv://admin:N.anh1992003@cluster0.a77gm.mongodb.net/final")
# db = client["final"]  # Tên database
# donation_collection = db["Quyengops"]  # Tên collection

# # Convert ObjectId thành string
# def donation_serializer(donation) -> dict:
#     return {
#         "id": str(donation["_id"]),
#         "Bank_Account_Number": donation["Bank_Account_Number"],
#         "Bank_Name": donation["Bank_Name"],
#         "Campaign_Name": donation["Campaign_Name"],
#         "Contact_Information": donation["Contact_Information"],
#         "Donation_Amount": donation["Donation_Amount"],
#         "Donation_Type": donation["Donation_Type"],
#         "Name": donation["Name"],
#         "Note": donation.get("Note", ""),
#         "Quantity_of_Goods": donation["Quantity_of_Goods"],
#         "Status": donation["Status"],
#         "Type_of_Goods": donation.get("Type_of_Goods", ""),
#         "Unit": donation.get("Unit", ""),
#         "date": donation["date"],
#     }

# # Route GET - Trang chủ (check xem ứng dụng có hoạt động không)
# @app.get("/")
# async def root():
#     return {"message": "Welcome to the Donation API!"}

# # Route POST - Tạo quyên góp mới
# @app.post("/donations/")
# async def create_donation(donation: Donation):
#     donation_dict = donation.dict(exclude_unset=True)
#     result = await donation_collection.insert_one(donation_dict)
#     created_donation = await donation_collection.find_one({"_id": result.inserted_id})
#     return {"message": "Donation created", "donation": donation_serializer(created_donation)}

# # Route GET - Lấy danh sách tất cả quyên góp
# @app.get("/donations/", response_model=List[Donation])
# async def get_donations():
#     donations = []
#     async for donation in donation_collection.find():
#         donations.append(donation_serializer(donation))
#     return donations

# # Route GET - Lấy chi tiết quyên góp theo ID
# @app.get("/donations/{donation_id}", response_model=Donation)
# async def get_donation(donation_id: str):
#     donation = await donation_collection.find_one({"_id": ObjectId(donation_id)})
#     if donation is None:
#         raise HTTPException(status_code=404, detail="Donation not found")
#     return donation_serializer(donation)


















# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, EmailStr
# from typing import List, Optional
# from datetime import datetime
# from motor.motor_asyncio import AsyncIOMotorClient
# from bson import ObjectId

# # Khởi tạo FastAPI
# app = FastAPI()

# # Kết nối MongoDB (Motor)
# client = AsyncIOMotorClient("mongodb+srv://admin:N.anh1992003@cluster0.a77gm.mongodb.net/final")
# db = client["final"]  # Tên database
# donation_collection = db["Quyengops"]  # Tên collection

# # Mô hình Donation
# class Donation(BaseModel):
#     id: Optional[str]
#     Bank_Account_Number: str
#     Bank_Name: str
#     Campaign_Name: str
#     Contact_Information: str
#     Donation_Amount: int
#     Donation_Type: str
#     Name: str
#     Note: Optional[str] = None
#     Quantity_of_Goods: int
#     Status: str
#     Type_of_Goods: Optional[str] = ""
#     Unit: Optional[str] = ""
#     date: datetime

# # Convert ObjectId thành string
# def donation_serializer(donation) -> dict:
#     return {
#         "id": str(donation["_id"]),
#         "Bank_Account_Number": donation["Bank_Account_Number"],
#         "Bank_Name": donation["Bank_Name"],
#         "Campaign_Name": donation["Campaign_Name"],
#         "Contact_Information": donation["Contact_Information"],
#         "Donation_Amount": donation["Donation_Amount"],
#         "Donation_Type": donation["Donation_Type"],
#         "Name": donation["Name"],
#         "Note": donation.get("Note", ""),
#         "Quantity_of_Goods": donation["Quantity_of_Goods"],
#         "Status": donation["Status"],
#         "Type_of_Goods": donation.get("Type_of_Goods", ""),
#         "Unit": donation.get("Unit", ""),
#         "date": donation["date"],
#     }

# # Route GET - Trang chủ (check xem ứng dụng có hoạt động không)
# @app.get("/")
# async def root():
#     return {"message": "Welcome to the Donation API!"}

# # Route POST - Tạo quyên góp mới
# @app.post("/donations/")
# async def create_donation(donation: Donation):
#     donation_dict = donation.dict(exclude_unset=True)
#     result = await donation_collection.insert_one(donation_dict)
#     created_donation = await donation_collection.find_one({"_id": result.inserted_id})
#     return {"message": "Donation created", "donation": donation_serializer(created_donation)}

# # Route GET - Lấy danh sách tất cả quyên góp
# @app.get("/donations/", response_model=List[Donation])
# async def get_donations():
#     donations = []
#     async for donation in donation_collection.find():
#         donations.append(donation_serializer(donation))
#     return donations

# # Route GET - Lấy chi tiết quyên góp theo ID
# @app.get("/donations/{donation_id}", response_model=Donation)
# async def get_donation(donation_id: str):
#     donation = await donation_collection.find_one({"_id": ObjectId(donation_id)})
#     if donation is None:
#         raise HTTPException(status_code=404, detail="Donation not found")
#     return donation_serializer(donation)

# # Route PUT - Sửa quyên góp theo ID
# @app.put("/donations/{donation_id}")
# async def update_donation(donation_id: str, donation: Donation):
#     donation_dict = donation.dict(exclude_unset=True)
#     result = await donation_collection.update_one(
#         {"_id": ObjectId(donation_id)}, {"$set": donation_dict}
#     )
    
#     if result.matched_count == 0:
#         raise HTTPException(status_code=404, detail="Donation not found")
    
#     updated_donation = await donation_collection.find_one({"_id": ObjectId(donation_id)})
#     return {"message": "Donation updated", "donation": donation_serializer(updated_donation)}

# # Route DELETE - Xóa quyên góp theo ID
# @app.delete("/donations/{donation_id}")
# async def delete_donation(donation_id: str):
#     result = await donation_collection.delete_one({"_id": ObjectId(donation_id)})
    
#     if result.deleted_count == 0:
#         raise HTTPException(status_code=404, detail="Donation not found")
    
#     return {"message": "Donation deleted"}

# # Route GET - Tìm kiếm quyên góp theo tên
# @app.get("/donations/search/")
# async def search_donations(name: str):
#     donations = []
#     async for donation in donation_collection.find({"Name": {"$regex": name, "$options": "i"}}):
#         donations.append(donation_serializer(donation))
#     return donations















from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

# Khởi tạo FastAPI
app = FastAPI()

# Kết nối MongoDB (Motor)
client = AsyncIOMotorClient("mongodb+srv://admin:N.anh1992003@cluster0.a77gm.mongodb.net/final")
db = client["final"]  # Tên database
donation_collection = db["Quyengops"]  # Tên collection

# Mô hình Donation
class Donation(BaseModel):
    _id: Optional[str]
    Bank_Account_Number: str
    Bank_Name: str
    Campaign_Name: str
    Contact_Information: str
    Donation_Amount: int
    Donation_Type: str
    Name: str
    Note: Optional[str] = None
    Quantity_of_Goods: int
    Status: str
    Type_of_Goods: Optional[str] = ""
    Unit: Optional[str] = ""
    date: datetime

    # Validator để chuyển ObjectId thành string khi xuất ra
    @classmethod
    def from_mongo(cls, donation):
        """Chuyển ObjectId thành string khi nhận từ MongoDB"""
        donation["_id"] = str(donation["_id"])  # Chuyển ObjectId thành string
        return cls(**donation)

    # Chuyển ObjectId thành chuỗi khi trả về API
    @classmethod
    def to_mongo(cls, donation):
        """Chuyển chuỗi thành ObjectId khi lưu vào MongoDB"""
        if "_id" in donation:
            donation["_id"] = ObjectId(donation["_id"])  # Chuyển chuỗi thành ObjectId
        return donation


# Convert ObjectId thành string cho tất cả dữ liệu
def donation_serializer(donation) -> dict:
    donation["_id"] = str(donation["_id"])  # Chuyển ObjectId thành string
    return {
        "id": donation["_id"],
        "Bank_Account_Number": donation["Bank_Account_Number"],
        "Bank_Name": donation["Bank_Name"],
        "Campaign_Name": donation["Campaign_Name"],
        "Contact_Information": donation["Contact_Information"],
        "Donation_Amount": donation["Donation_Amount"],
        "Donation_Type": donation["Donation_Type"],
        "Name": donation["Name"],
        "Note": donation.get("Note", ""),
        "Quantity_of_Goods": donation["Quantity_of_Goods"],
        "Status": donation["Status"],
        "Type_of_Goods": donation.get("Type_of_Goods", ""),
        "Unit": donation.get("Unit", ""),
        "date": donation["date"],
    }

# Route GET - Trang chủ (check xem ứng dụng có hoạt động không)
@app.get("/")
async def root():
    return {"message": "Welcome to the Donation API!"}

# Route POST - Tạo quyên góp mới
@app.post("/donations/")
async def create_donation(donation: Donation):
    donation_dict = donation.dict(exclude_unset=True)
    donation_dict = Donation.to_mongo(donation_dict)  # Chuyển dữ liệu thành ObjectId khi lưu vào MongoDB
    result = await donation_collection.insert_one(donation_dict)
    created_donation = await donation_collection.find_one({"_id": result.inserted_id})
    return {"message": "Donation created", "donation": donation_serializer(created_donation)}

# Route GET - Lấy danh sách tất cả quyên góp
@app.get("/donations/", response_model=List[Donation])
async def get_donations():
    donations = []
    async for donation in donation_collection.find():
        donations.append(Donation.from_mongo(donation))  # Chuyển ObjectId thành string khi nhận dữ liệu
    return donations

# Route GET - Lấy chi tiết quyên góp theo ID
@app.get("/donations/{donation_id}", response_model=Donation)
async def get_donation(donation_id: str):
    donation = await donation_collection.find_one({"_id": ObjectId(donation_id)})
    if donation is None:
        raise HTTPException(status_code=404, detail="Donation not found")
    return Donation.from_mongo(donation)  # Chuyển ObjectId thành string khi trả về

# Route PUT - Sửa quyên góp theo ID
@app.put("/donations/{donation_id}")
async def update_donation(donation_id: str, donation: Donation):
    donation_dict = donation.dict(exclude_unset=True)
    donation_dict = Donation.to_mongo(donation_dict)  # Chuyển ObjectId thành string khi lưu vào MongoDB
    result = await donation_collection.update_one(
        {"_id": ObjectId(donation_id)}, {"$set": donation_dict}
    )
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Donation not found")
    
    updated_donation = await donation_collection.find_one({"_id": ObjectId(donation_id)})
    return {"message": "Donation updated", "donation": donation_serializer(updated_donation)}

# Route DELETE - Xóa quyên góp theo ID
@app.delete("/donations/{donation_id}")
async def delete_donation(donation_id: str):
    result = await donation_collection.delete_one({"_id": ObjectId(donation_id)})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Donation not found")
    
    return {"message": "Donation deleted"}

# Route GET - Tìm kiếm quyên góp theo tên
@app.get("/donations/search/")
async def search_donations(name: str):
    donations = []
    async for donation in donation_collection.find({"Name": {"$regex": name, "$options": "i"}}):
        donations.append(donation_serializer(donation))
    return donations






















