from sqlalchemy import create_engine, Column, String
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
import bcrypt

class Database:
    __username = ''
    __host = ''
    __database = ''
    __password = ''
    _url = None
    _engin = None
    _session = None
    _Base = declarative_base()

    class User(_Base):
                __tablename__ = "Users"
                Username = Column(String(), primary_key=True)
                Password = Column(String())

    def __init__(self, username, host, database, password):
        self.__username = username
        self.__host = host
        self.__database = database
        self.__password = password
        
    def connect(self):
        url = URL.create(
            drivername= 'postgresql',
            username= self.__username,
            host= self.__host,
            database= self.__database,
            password= self.__password,
        )

        self._url = url
        self._engin = create_engine(url)
        Session = sessionmaker(bind=self._engin)
        self._session = Session()
        
    def showUser(self, username):
        return self._session.query(self.User).filter(self.User.Username == username).first()

    def login(self, username, password):
        try:
            user = self.showUser(username)
            if user:
                stored_hashed_password = user.Password
                # Check if the entered password matches the stored hashed password
                if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            print(f"Error during login: {e}")
            return False

    def signup(self, username, password):
        try:
            existing_user = self.showUser(username)
            if not existing_user:
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                new_user = self.User(Username=username, Password=hashed_password.decode('utf-8'))
                self._session.add(new_user)
                self._session.commit()
                return True
        except Exception as e:
            print(f"Error during signup: {e}")
            return False

