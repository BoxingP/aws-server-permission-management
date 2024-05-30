from contextlib import contextmanager
from urllib.parse import quote

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import config
from server import Server

adapter = config.server_database_adapter
host = config.server_database_host
port = config.server_database_port
database = config.server_database_database
user = config.server_database_user
password = config.server_database_password
engine = create_engine(f'{adapter}://{user}:%s@{host}:{port}/{database}' % quote(password))
Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class DatabaseManager(object):
    def get_server_info(self):
        servers = []
        with session_scope() as session:
            query = session.query(Server).filter_by(account=config.server_aws_account,
                                                    environment=config.server_environment, state=config.server_state)
            query = query.yield_per(100)
            for server in query:
                server_dict = {
                    'hostname': server.hostname,
                    'dns': f'ec2-{server.ip.replace(".", "-")}.{server.region}.compute.amazonaws.com.cn'
                }
                servers.append(server_dict)
        return servers
