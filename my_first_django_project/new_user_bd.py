from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()
engine = create_engine(
    "sqlite:///my_first_django_project/new_userbd.sqlite3",
    echo=True
)

class User(Base):
    __tablename__ = "new_user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

Base.metadata.create_all(engine)

def delete_new_user():
    with engine.begin()as conn:
        conn.execute(text("DELETE FROM new_user"))

def last_user():
    with engine.begin()as conn:
        user = conn.execute(text('''SELECT *
                           FROM new_user
                           WHERE id = (SELECT MAX(id) FROM new_user)'''))
        for i in user:
            result = [row for row in i]
        return result

def new_person_new_user(id_user=0, name_user='', email_user='', password_user=''):
    id_user = last_user()[0] + 1
    with Session(engine) as session:
        new_user = User(id=id_user, name=name_user, email=email_user, password=password_user)
        session.add(new_user)
        session.commit()

def data_in_data():
    delete_new_user()
    with open('my_first_django_project/data.csv', encoding='utf-8') as fl:
        data = [i.strip() for i in fl.readlines()]
        data = data[1:]
        for i in data:
            row = i.split(',')
            new_person_new_user(id_user=int(row[3]), name_user=row[0], email_user=row[1], password_user=row[2])
    
last_user()

# def new_person(id_user=0, balanse_user=0):
#     with Session(engine) as session:
#         new_user = User(id=id_user, balanese=balanse_user)
#         session.add(new_user)
#         session.commit()

# def look_bd():
#     with engine.begin()as conn:
#         data = conn.execute(text("SELECT * FROM user"))
#         data = [row for row in data]
#         print(data)
        
# def look_id():
#     with engine.begin()as conn:
#         data = conn.execute(text("SELECT id FROM user"))
#         data = [i for row in data for i in row]
#         print(data)
#     return data

# def replacement_balanse(id_user, flag):
#     balanse_person = -3
#     with Session(engine) as session:
#         user = session.get(User, id_user)

#         if user:
#             if flag == '0':
#                 user.balanese -= 15
#             elif flag == 'x':
#                 user.balanese += 15
#             else:
#                 user.balanese += 0
#             balanse_person = user.balanese
#             session.commit()
#     return balanse_person

# def look_balanse(id_user):
#     balanse_person = -3
#     with Session(engine) as session:
#         user = session.get(User, id_user)
#         if user:
#             balanse_person = user.balanese
#             session.commit()
#         else:
#             new_person(id_user=id_user, balanse_user=100)
#             balanse_person = 100
#     return balanse_person