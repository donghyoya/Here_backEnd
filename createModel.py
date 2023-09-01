'''
from sqlalchemy import create_engine, MetaData
from sqlalchemy_schemadisplay import create_schema_graph
from sqlalchemy.ext.declarative import declarative_base
import os

DATABASE_URL = "postgresql://postgres:0814@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)
metadata = MetaData()
metadata.reflect(bind=engine)


Base = declarative_base(metadata=metadata)

def generate_model_for_table(table_name, directory):
    columns = metadata.tables[table_name].columns
    class_definition = f"class {table_name}(Base):\n"
    class_definition += f"    __table__ = metadata.tables['{table_name}']\n"

    with open(os.path.join(directory, "model.py"), "w") as f:
        f.write(class_definition)

    for column in columns:
        col_type = str(column.type)
        class_definition += f"    {column.name} = Column({col_type})\n"

table_directory_mapping = {
    "User": "domain/user",
    "Map": "domain/map",
    "Image": "domain/image"
}

for table_name, directory in table_directory_mapping.items():
    generate_model_for_table(table_name, directory)
'''

from sqlalchemy.ext.automap import automap_base, name_for_scalar_relationship
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:0814@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)

# Reflect the tables
Base = automap_base()

# Custom naming function for scalar relationships
def custom_name_for_scalar_relationship(base, local_cls, referred_cls, constraint):
    return name_for_scalar_relationship(base, local_cls, referred_cls, constraint) + "_ref"

Base.prepare(engine, reflect=True, name_for_scalar_relationship=custom_name_for_scalar_relationship)

# Mapped classes are now created with names by default
# matching that of the table name.
User = Base.classes.User


User = Base.classes.User

# User 모델의 속성들을 출력
for column in User.__table__.columns:
    print(column)
