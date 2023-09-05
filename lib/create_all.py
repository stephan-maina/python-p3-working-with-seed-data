from models import Base, engine

# Create the tables defined in your models
Base.metadata.create_all(engine)
