# FastAPI_Page


## The following app is backend connection made using FastAPI
The app contains CRUD operations for user profiles, post entries,user authentication and voting system.

>Source folder: API_ENDPOINTS_User_Post/

---

The following app branch is hosted on : https://fast-api-votes-system-demo1.onrender.com/
---
**Content**

1. [Installation](#installation)
1. [Endpoints](#endpoints)
1. [Database using SQLAlchemy Alembic Model](#database-model)
1. Dockerization
1. Config Render and AWS Instance


---


## Installation

>Install : pip install -r requirements.txt

requirements.txt file inside Source Folder(API_ENDPOINTS_User_Post)


## Endpoints
### Get
- /posts: Get all Post info (not user info)
- /posts/{id}: Get post by id
- /users/{id}: get user info(after authentication) 

### Post and Put
- /posts: Create post
- /posts/{id}: Update post for particular ID
- /users: Create User

### Delete
- /posts/{id}: Delete Post

>Checkout Docs and redocs for more info on query parameters and structure.


## Database Model

```

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer,primary_key = True , nullable = False)
    title = Column(String,nullable = False )
    content = Column(String , nullable=False)
    published = Column(Boolean , nullable=False , server_default = 'TRUE') 
    created_at = Column(TIMESTAMP(timezone=True),nullable = False , server_default =text("now()"))
    owner_id = Column(Integer , ForeignKey("users.id" , ondelete="CASCADE") , nullable = False)
    owner = relationship("User")#get class


#new sqlalchemy model 
class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key = True  ,nullable = False )
    email = Column(String,nullable = False ,unique=True)
    password = Column(String , nullable = False)
    created_at = Column(TIMESTAMP(timezone=True),nullable = False , server_default =text("now()"))


class Votes(Base):
    __tablename__ = "votes"
    user_id = Column(Integer , ForeignKey("users.id" , ondelete="CASCADE") , primary_key = True)
    post_id = Column(Integer , ForeignKey("post.id" , ondelete="CASCADE") , primary_key = True)
    


```


### Pydantic Schemas

```

class Userout(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True




class PostBase(BaseModel):
    title:str 
    content :str
    published : bool = True 


class PostCreate(PostBase):
    pass

class Post(PostBase):
    id:int
    created_at: datetime
    owner_id: int
    owner: Userout 
    class Config:
        orm_mode = True


#schema for new post after adding votes
class PostOut(BaseModel):
    Post: Post 
    votes: int 
    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email:EmailStr
    password:str 

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str 
    token_type: str 

class TokenData(BaseModel):
    id: Optional[str]=None

class Vote(BaseModel):
    post_id: int 
    dir: conint(le=1)

```

>The above database schema ORM is used in Postgres free instance available on Render



## Dockerization