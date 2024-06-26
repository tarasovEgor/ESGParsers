import re
# from datetime import datetime
from pydantic import BaseModel, validator


class SravniRuBaseScheme(BaseModel):
    sravni_id: str
    sravni_old_id: int | None = None
    alias: str
    bank_name: str
    bank_full_name: str
    bank_official_name: str
    bank_id: int
    # time_created: datetime

    class Config:
        orm_mode = True


class SravniRuBankScheme(SravniRuBaseScheme):
    @validator("bank_id", pre=True)
    def validate_bank_id(cls, v: str) -> int:
        license_id_str = v.split("-")[0]
        return int(license_id_str)


# class SravniRuInsuranceScheme(SravniRuBaseScheme):
#     @validator("bank_id", pre=True)
#     def validate_bank_id(cls, v: str) -> int:
#         if len(v) == 0:
#             return -1
#         return int(re.findall(r"(?:(?<=№)|(?<=№\s))\d+(?:(?=\sот)|(?=-\d+|\s))", v)[0])

class SravniRuInsuranceScheme(SravniRuBaseScheme):
    @validator("bank_id", pre=True)
    def validate_bank_id(cls, v: str) -> int:
        if len(v) == 0:
            return -1
        matches = re.findall(r"(?:(?<=№)|(?<=№\s))\d+(?:(?=\sот)|(?=-\d+|\s))", v)
        if matches:
            return int(matches[0])
        else:
            return -1


class SravniRuMfoScheme(SravniRuBaseScheme):
    bank_ogrn: int
