from datetime import timedelta, datetime

from fastapi import APIRouter, HTTPException
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.user import user_crud, user_schema
from domain.user.user_crud import pwd_context

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

SECRET_KEY = "6a7628cc57e6782f41f2b44654c92f870fc788fdff0a81d2a256f0e90a3e4d86"

ALGORITHM = "HS256"


router = APIRouter(
    prefix="/api/user",
)

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def user_create(_user_create: user_schema.UserCreate, db: Session = Depends(get_db)):
    user = user_crud.get_existing_user(db, user_create=_user_create)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="이미 존재하는 사용자입니다.")
    user_crud.create_user(db=db, user_create=_user_create)

@router.post("/login", status_code=status.HTTP_202_ACCEPTED)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                           db: Session = Depends(get_db)
):

    # -----------------------------------------------
    # 1. 사용자 아이디와 비밀번호 확인
    # -----------------------------------------------

    # OAuth2PasswordRequestForm:
    # 로그인 요청으로 전달된 username과 password를 가져온다.
    # 입력 데이터는 JSON이 아닌 form 데이터 형식이다.

    # 입력받은 username으로 DB에서 사용자 정보 조회
    user = user_crud.get_user(db,form_data.username)
    # 사용자가 존재하지 않거나 비밀번호가 일치하지 않으면 인증실패
    # pwd_context.verify(입력 비밀번호, DB에 저장된 해시 비밀번호)
    # 입력 비밀번호를 저장된 해시 방식으로 검증하여 일치 여부 판단
    # pwd_context.vertify()는 단순히 두 문자열을 비교하는 함수가 아니라,
    # 입력한 비밀번호와 데이터베이스에 저장된 헤시 비밀번호가 일치하는지 검증하는 함수
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    # JWT 엑세스 토큰에 저장할 데이터 생성

    # JSON 형식으로 사용자 정보 등을 담아 전달하는 토큰
    # Claim(클레임)은 JWT에 저장되는 정보의 항목을 의미한다.
    # sub (Subject): 토큰의 주체, 여기서는 사용자 아이디
    # exp (Expiration Time): 토큰의 만료 시간
    date = {
        "sub" : user.username,
        "exp" : datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    }
    # 3. JWT 엑세스 토큰 생성

    #jwt.encode(데이터, 비밀키, 서명 알고리즘)
    #data에 담긴 사용자 정보와 만료 시간을 이용해 JWT 생성
    #SECRET_KEY와 HS256 알고리즘으로 디지털 서명한다.
    #JWT는 기본적으로 암호화가 아닌 인코딩과 서명을 사용한다.
    #jwt.encnode()는 사용자 정보를 암호화해 숨기는 함수가 아니라,
    #JWT를 생성하고 서명하여 위변조를 검증할 수 있도록 만드는 함수
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    #access_token: 생성된 JWT 토큰
    #token_type: 인증 방식
    #username: 로그인한 사용자 아이디
    return {"access_token": jwt.encode, "token_type": "bearer","username": user.username}