import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario (Base):

    __tablename__ = 'usuario'    
    id = Column(Integer, primary_key=True)
    user = Column(String(250), nullable= True)
    password = Column(String(250), nullable= True)

class Likes (Base):

    __tablename__ = 'likes'    
    id = Column(Integer, primary_key=True)
    reaccion = Column(String(250), nullable= True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
   
    

class Medias (Base):

    __tablename__ = 'medias'    
    id = Column(Integer, primary_key=True)
    photo = Column(String(250), nullable= True)
    video= Column(String(250), nullable= True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
       

class Comentarios (Base):

    __tablename__ = 'comentarios'    
    id = Column(Integer, primary_key=True)
    parrafo = Column(String(250), nullable= True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
      
    # post_id = Column(Integer, ForeignKey('post.id'))
    # post = relationship()


class Post (Base):
    __tablename__ = 'post' 
    id = Column(Integer, primary_key=True)      
    usuario_id = Column(Integer, ForeignKey('usuario.id'))    
    comentarios_id = Column(Integer, ForeignKey('comentario.id'))
    parrafo = Column(String(250), nullable= True)
    comentarios = relationship(Comentarios)
    medias_id = Column(Integer, ForeignKey('medias.id'))
    photo = Column(String(250), nullable= True)
    video = Column(String(250), nullable= True)
    medias = relationship(Medias)
    likes_id = Column(Integer, ForeignKey('likes.id'))
    reaccion = Column(String(250), nullable= True)
    likes = relationship(Likes)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e