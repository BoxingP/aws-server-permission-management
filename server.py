from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Server(Base):
    __tablename__ = 'aws_ec2_instances'
    id = Column('id', Integer, primary_key=True)
    account = Column('aws_account', String)
    environment = Column('environment', String)
    hostname = Column('instance_displayname', String)
    ip = Column('instance_public_ip', String)
    region = Column('instance_region', String)
    state = Column('instance_state', String)
