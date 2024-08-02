import sqlalchemy
import yaml

class AWSDBConnector:

    def __init__(self, credentials_path="creds/credential.yaml"):
        self.creds  = self.read_credentials_file(credentials_path)
        self.HOST = self.creds["HOST"]
        self.USER = self.creds["USER"]
        self.PASSWORD = self.creds["PASSWORD"]
        self.DATABASE = self.creds["DATABASE"]
        self.PORT = self.creds["PORT"]

    @staticmethod
    def read_credentials_file(file_name):
        try:
            with open(file_name, 'r') as file:
                cred = yaml.safe_load(file)
                return cred
        except yaml.YAMLError as e:
                    print(f"Error reading YAML file: {e}")
                    return None
        
    def create_db_connector(self):
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
        return engine
