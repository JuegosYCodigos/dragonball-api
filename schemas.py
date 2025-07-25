from database import Base,engine,sessionLocal
from sqlalchemy import Column,String,Integer,Text,BIGINT


try:
    class DragonBall(Base):
        __tablename__ = 'personajess'
        __table_args__ = {'extend_existing': True}


        id = Column(Integer,primary_key=True)
        nombre = Column(String(25))
        descripcion = Column(Text)
        genero = Column(String(25))
        ki = Column(BIGINT)
        max_ki = Column(BIGINT)
        imagen = Column(Text)
        raza = Column(String(25))
        print('conneccion creada conn exito')
except Exception as e:
    print(e)
Base.metadata.create_all(bind=engine)

session = sessionLocal()



#for dato in datos:
    #print(f'id: {dato.id}, nombre: {dato.nombre}, raza: {dato.raza}, genero: {dato.genero}' )
