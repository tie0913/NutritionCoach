class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://dev:!QAZ2wsx3edc@localhost:3306/nutri_coache"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False