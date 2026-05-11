from typing import Literal, Optional

from pydantic import Field

from app.schemas.base import ApiBaseModel


class UserSyncRequest(ApiBaseModel):
    uid: str
    email: str
    nickname: str
    provider: str
    profile_image: Optional[str] = None


class UserSyncBody(ApiBaseModel):
    nickname: Optional[str] = None


AgeGroup = Literal["10대", "20대", "30대", "40대", "50대", "60대 이상"]
JobType = Literal["대학생", "직장인", "자영업자", "주부", "기타"]


class UserDetailsRequest(ApiBaseModel):
    name: str = Field(min_length=1, max_length=50)
    ageGroup: AgeGroup
    job: JobType
    mainBank: str = Field(min_length=1, max_length=30)
    residence: str = Field(min_length=1, max_length=100)


class UserDetailsData(ApiBaseModel):
    id: int
    name: str
    ageGroup: str
    job: str
    mainBank: str
    residence: str
    updatedAt: str


class UserDetailsResponse(ApiBaseModel):
    status: str = "success"
    message: str = "사용자 상세 정보가 성공적으로 저장되었습니다."
    data: UserDetailsData


class UserSyncItem(ApiBaseModel):
    id: int
    firebaseUid: str
    email: str
    provider: str
    nickname: str
    isNewUser: bool


class UserSyncResponse(ApiBaseModel):
    status: str = "success"
    user: UserSyncItem


class UserMeItem(ApiBaseModel):
    id: int
    firebaseUid: str
    email: str
    provider: str
    nickname: str
    ageGroup: Optional[str] = None
    job: Optional[str] = None
    mainBank: Optional[str] = None
    residence: Optional[str] = None
    emailVerified: bool
    profileImageUrl: Optional[str] = None
    isNewUser: bool
    createdAt: str
    updatedAt: str


class UserMeResponse(ApiBaseModel):
    status: str = "success"
    user: UserMeItem


class UserMeUpdateRequest(ApiBaseModel):
    nickname: Optional[str] = None
    profileImageDataUrl: Optional[str] = None
    profileImageBase64: Optional[str] = None
    profileImageUrl: Optional[str] = None
