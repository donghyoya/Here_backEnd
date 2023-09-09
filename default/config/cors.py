from main import app
from fastapi.middleware.cors import CORSMiddleware

origins = [
   "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # 허용할 자격증명 (예: 쿠키, OAuth 토큰) 설정
    allow_methods=["*"],  # 허용할 HTTP 메서드 설정
    allow_headers=["*"],  # 허용할 HTTP 헤더 설정
)