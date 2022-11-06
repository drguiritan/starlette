from database import Base,Engine
from models import Student


Base.metadata.create_all(bind=Engine)