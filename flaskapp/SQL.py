import sqlalchemy
from sqlalchemy import URL
from sqlalchemy import Column, Integer, String, UUID

class UserSQL :
    __tablename__ = 'users'
    id = Column(UUID, unique=True, nullable=False)
    name = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True)



class sql:
    conn = sqlalchemy.create_engine()
    def __init__(self, host : str, port: int, user : str, password : str, database : str, protocol : str = "postgresql"):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = database
        self.protocol = protocol

    def create_connection(self):
        self.conn = sqlalchemy.create_engine(URL.create(self.protocol, self.user, self.password, self.host, self.port, self.db))



