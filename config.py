class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://dvwa:p@ssw0rd@localhost:3306/dvwa"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False