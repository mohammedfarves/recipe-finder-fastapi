from database import Base, engine
from models import Recipe # Import your Recipe model to ensure Base knows about it

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Tables created.")
