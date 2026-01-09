from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()
engine = create_engine(
    "sqlite:///my_first_django_project/old_userbd.sqlite3",
    echo=True
)

class User(Base):
    __tablename__ = "old_user"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

Base.metadata.create_all(engine)

def delete_old_user():
    with engine.begin()as conn:
        conn.execute(text("DELETE FROM old_user"))

# def last_user():
#     with engine.begin()as conn:
#         user = conn.execute(text('''SELECT *
#                            FROM old_user
#                            WHERE id = (SELECT MAX(id) FROM old_user)'''))
#         for i in user:
#             result = [row for row in i]
#         return result
#     return []

# def new_person_old_user(id_user=0, email_user='', password_user=''):
#     id_user = last_user()[0] + 1
#     with Session(engine) as session:
#         new_user = User(id=id_user, email=email_user, password=password_user)
#         session.add(new_user)
#         session.commit()

# def data_in_data_old():
#     delete_old_user()
#     with open('my_first_django_project/data_old.csv', encoding='utf-8') as fl:
#         data = [i.strip() for i in fl.readlines()]
#         data = data[1:]
#         for i in data:
#             row = i.split(',')
#             new_person_old_user(id_user=int(row[2]), email_user=row[0], password_user=row[1])

# data_in_data_old()  
