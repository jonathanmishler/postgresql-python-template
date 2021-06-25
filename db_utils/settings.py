from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    db_host: str
    db_port: int    
    db_username: str
    db_password: str
    db_name: str
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        secrets_dir = './secrets'