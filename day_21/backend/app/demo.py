# wit cursor database connection
# from random import randrange

# import psycopg2
# @app.get('/')
# def root():
#     return {"message" : "hello world"}

# @app.get('/posts')
# def get_posts():
#     posts = cursor.execute(""" SELECT * FROM posts """)
#     posts = cursor.fetchall()
    
#     return {"post" : posts}

# @app.post('/posts' , status_code=status.HTTP_201_CREATED)
# def create_post(data : CreatePost):
   
#    cursor.execute(""" insert into posts (title , content , published ) values(%s,%s,%s) returning *"""
#                   ,(data.title , data.content , data.published))
#    new_post = cursor.fetchone()
#    conn.commit()
#    return {"data" : new_post}


# @app.get('/posts/{id}')
# def get_one_post(id:int):
#     cursor.execute(""" select * from posts where id = %s""" , (str(id),))
#     test_post = cursor.fetchone()
#     print(test_post)

    
#     if not test_post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="id not found")
#     return {"post" : test_post}



# @app.delete('/posts/{id}' , status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id : int):
#     cursor.execute(""" delete from posts where id = %s returning *""" , (str(id),))
#     deleted_post = cursor.fetchone()
#     conn.commit()
    
#     if deleted_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="post not found with this id")
    
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put('/posts/{id}')
# def update_post(id:int , post : CreatePost):

#     cursor.execute("""update posts set title = %s, content =%s , published = %s where id = %s returning*""" , (post.title,
#     post.content , post.published , str(id)) )
#     updated_post = cursor.fetchone()
#     conn.commit()
#     if updated_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="id not found")

#     return {'message' : updated_post}

# try:
#     conn = psycopg2.connect(host='localhost' ,
#     database='fastapi' , user='postgres' , password='password',cursor_factory=RealDictCursor)
#     cursor = conn.cursor()
#     print("Database connect was successfull!")
# except Exception as error:
#     print("Connecting to database failed" )
#     print("Error" , error)