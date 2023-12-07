
from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:1@localhost:5432/postgres')

base = declarative_base()

class Client(Base):
    __tablename__ = "clients"
    id = Column("id", Integer, autoincrement=True, primary_key=True)
    fullname = Columna("fullname", VARCHAR(255))
    username = Columna("username", VARCHAR(255), unique = True)
    password= Columna("password", VARCHAR(10), CheckConstraint("length(password)>4"))
    join_at = Columna("fullname", TIMESTAMP(timezone = True , default= current_timestamp))


class Branch_address(Base):
    __tablename__ = "addresses"
    id = Column("id", Integer , autoincrement=True, primary_key = True)
   country = Columna("cities", VARCHAR(100))


clients = select(Client).where(Client.id==2)
clients = session.execute(clients)
for i in clients :
    print(i)