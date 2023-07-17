from contextlib import contextmanager
from urllib.parse import quote

from decouple import config as decouple_config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from server import Server

adapter = decouple_config('SERVER_DATABASE_ADAPTER')
host = decouple_config('SERVER_DATABASE_HOST')
port = decouple_config('SERVER_DATABASE_PORT')
database = decouple_config('SERVER_DATABASE_DATABASE')
user = decouple_config('SERVER_DATABASE_USER')
password = decouple_config('SERVER_DATABASE_PASSWORD')
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
            query = session.query(Server).filter_by(account=decouple_config('SERVER_AWS_ACCOUNT'),
                                                    environment=decouple_config('SERVER_ENVIRONMENT'),
                                                    state=decouple_config('SERVER_STATE'))
            query = query.yield_per(100)
            for server in query:
                server_dict = {
                    'hostname': server.hostname,
                    'dns': f'ec2-{server.ip.replace(".", "-")}.{server.region}.compute.amazonaws.com.cn'
                }
                servers.append(server_dict)
        return servers
