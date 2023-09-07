import os

# sqlacodegen으로부터 생성된 모델 정의
models_definition = """
PS C:\Users\dongw\Documents\Here_backEnd> sqlacodegen postgresql://postgres:0814@localhost:5432/postgres
from sqlalchemy import BigInteger, Boolean, CheckConstraint, Column, DateTime, Float, ForeignKeyConstraint, Identity, Index, Integer, PrimaryKeyConstraint, SmallInteger, String, Text, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Image(Base):
    __tablename__ = 'Image'
    __table_args__ = (
        PrimaryKeyConstraint('imageId', name='Image_pkey'),
    )

    imageId = Column(BigInteger, primary_key=True)
    Key = Column(BigInteger, nullable=False)
    imageName = Column(Text)
    imageUrl = Column(Text)
    imageSize = Column(Text)
    fileType = Column(Text)
    uploader_id = Column(BigInteger)
    createTime = Column(DateTime)
    tag = Column(Text)
    views = Column(Integer)

    Map = relationship('Map', back_populates='Image_')
    NFT = relationship('NFT', back_populates='Image_')


class Transaction(Base):
    __tablename__ = 'Transaction'
    __table_args__ = (
        PrimaryKeyConstraint('Key', name='Transaction_pkey'),
    )

    Key = Column(Text, primary_key=True)
    Key2 = Column(Text, nullable=False)
    imageId = Column(BigInteger, nullable=False)
    sellerId = Column(Text)
    buyerId = Column(Text)
    nftId = Column(Text)
    price = Column(Integer)
    transactionDate = Column(Text)
    status = Column(Text)


class User(Base):
    __tablename__ = 'User'
    __table_args__ = (
        PrimaryKeyConstraint('Key', name='User_pkey'),
    )

    Key = Column(BigInteger, primary_key=True)
    loginId = Column(Text)
    password = Column(Text)
    nickName = Column(Text)
    email = Column(Text)
    wallet_address = Column(Text)
    profileImage = Column(Text)


class AuthGroup(Base):
    __tablename__ = 'auth_group'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='auth_group_pkey'),
        UniqueConstraint('name', name='auth_group_name_key'),
        Index('auth_group_name_a6ea08ec_like', 'name')
    )

    id = Column(Integer, Identity(start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    name = Column(String(150), nullable=False)

    auth_user_groups = relationship('AuthUserGroups', back_populates='group')
    auth_group_permissions = relationship('AuthGroupPermissions', back_populates='group')


class AuthUser(Base):
    __tablename__ = 'auth_user'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='auth_user_pkey'),
        UniqueConstraint('username', name='auth_user_username_key'),
        Index('auth_user_username_6821ab7c_like', 'username')
    )

    id = Column(Integer, Identity(start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    password = Column(String(128), nullable=False)
    is_superuser = Column(Boolean, nullable=False)
    username = Column(String(150), nullable=False)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(254), nullable=False)
    is_staff = Column(Boolean, nullable=False)
    is_active = Column(Boolean, nullable=False)
    date_joined = Column(DateTime(True), nullable=False)
    last_login = Column(DateTime(True))

    auth_user_groups = relationship('AuthUserGroups', back_populates='user')
    django_admin_log = relationship('DjangoAdminLog', back_populates='user')
    auth_user_user_permissions = relationship('AuthUserUserPermissions', back_populates='user')


class DjangoContentType(Base):
    __tablename__ = 'django_content_type'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='django_content_type_pkey'),
        UniqueConstraint('app_label', 'model', name='django_content_type_app_label_model_76bd3d3b_uniq')
    )

    id = Column(Integer, Identity(start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    app_label = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)

    auth_permission = relationship('AuthPermission', back_populates='content_type')
    django_admin_log = relationship('DjangoAdminLog', back_populates='content_type')


class DjangoMigrations(Base):
    __tablename__ = 'django_migrations'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='django_migrations_pkey'),
    )

    id = Column(BigInteger, Identity(start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    app = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    applied = Column(DateTime(True), nullable=False)


class DjangoSession(Base):
    __tablename__ = 'django_session'
    __table_args__ = (
        PrimaryKeyConstraint('session_key', name='django_session_pkey'),
        Index('django_session_expire_date_a5c62663', 'expire_date'),
        Index('django_session_session_key_c0390e0f_like', 'session_key')
    )

    session_key = Column(String(40), primary_key=True)
    session_data = Column(Text, nullable=False)
    expire_date = Column(DateTime(True), nullable=False)


class Map(Base):
    __tablename__ = 'Map'
    __table_args__ = (
        ForeignKeyConstraint(['imageId'], ['Image.imageId'], name='FK_Image_TO_Map_1'),
        PrimaryKeyConstraint('mapid', 'imageId', name='PK_MAP')
    )

    mapid = Column(BigInteger, primary_key=True, nullable=False)
    imageId = Column(BigInteger, primary_key=True, nullable=False)
    longitude = Column(Float(53))
    latitude = Column(Float(53))
    Region = Column(Text)
    Country = Column(Text)
    City = Column(Text)
    State = Column(Text)
    Area = Column(Text)

    Image_ = relationship('Image', back_populates='Map')


class NFT(Base):
    __tablename__ = 'NFT'
    __table_args__ = (
        ForeignKeyConstraint(['imageId'], ['Image.imageId'], name='FK_Image_TO_NFT_1'),
        PrimaryKeyConstraint('Key', 'imageId', name='PK_NFT')
    )

    Key = Column(Text, primary_key=True, nullable=False)
    imageId = Column(BigInteger, primary_key=True, nullable=False)
    name = Column(Text)
    description = Column(Text)
    image = Column(Text)
    createDate = Column(Text)
    owner = Column(Text)
    bfOwner = Column(Text)
    Field = Column(Text)

    Image_ = relationship('Image', back_populates='NFT')


class AuthPermission(Base):
    __tablename__ = 'auth_permission'
    __table_args__ = (
        ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], deferrable=True, initially='DEFERRED', name='auth_permission_content_type_id_2f476e4b_fk_django_co'),      
        PrimaryKeyConstraint('id', name='auth_permission_pkey'),
        UniqueConstraint('content_type_id', 'codename', name='auth_permission_content_type_id_codename_01ab375a_uniq'),
        Index('auth_permission_content_type_id_2f476e4b', 'content_type_id')
    )

    id = Column(Integer, Identity(start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    name = Column(String(255), nullable=False)
    content_type_id = Column(Integer, nullable=False)
    codename = Column(String(100), nullable=False)

    content_type = relationship('DjangoContentType', back_populates='auth_permission')
    auth_group_permissions = relationship('AuthGroupPermissions', back_populates='permission')
    auth_user_user_permissions = relationship('AuthUserUserPermissions', back_populates='permission')


class AuthUserGroups(Base):
    __tablename__ = 'auth_user_groups'
    __table_args__ = (
        ForeignKeyConstraint(['group_id'], ['auth_group.id'], deferrable=True, initially='DEFERRED', name='auth_user_groups_group_id_97559544_fk_auth_group_id'),
        ForeignKeyConstraint(['user_id'], ['auth_user.id'], deferrable=True, initially='DEFERRED', name='auth_user_groups_user_id_6a12ed8b_fk_auth_user_id'),
        PrimaryKeyConstraint('id', name='auth_user_groups_pkey'),
        UniqueConstraint('user_id', 'group_id', name='auth_user_groups_user_id_group_id_94350c0c_uniq'),
        Index('auth_user_groups_group_id_97559544', 'group_id'),
        Index('auth_user_groups_user_id_6a12ed8b', 'user_id')
    )

    id = Column(BigInteger, Identity(start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    user_id = Column(Integer, nullable=False)
    group_id = Column(Integer, nullable=False)

    group = relationship('AuthGroup', back_populates='auth_user_groups')
    user = relationship('AuthUser', back_populates='auth_user_groups')


class DjangoAdminLog(Base):
    __tablename__ = 'django_admin_log'
    __table_args__ = (
        CheckConstraint('action_flag >= 0', name='django_admin_log_action_flag_check'),
        ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], deferrable=True, initially='DEFERRED', name='django_admin_log_content_type_id_c4bce8eb_fk_django_co'),     
        ForeignKeyConstraint(['user_id'], ['auth_user.id'], deferrable=True, initially='DEFERRED', name='django_admin_log_user_id_c564eba6_fk_auth_user_id'),
        PrimaryKeyConstraint('id', name='django_admin_log_pkey'),
        Index('django_admin_log_content_type_id_c4bce8eb', 'content_type_id'),
        Index('django_admin_log_user_id_c564eba6', 'user_id')
    )

    id = Column(Integer, Identity(start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    action_time = Column(DateTime(True), nullable=False)
    object_repr = Column(String(200), nullable=False)
    action_flag = Column(SmallInteger, nullable=False)
    change_message = Column(Text, nullable=False)
    user_id = Column(Integer, nullable=False)
    object_id = Column(Text)
    content_type_id = Column(Integer)

    content_type = relationship('DjangoContentType', back_populates='django_admin_log')
    user = relationship('AuthUser', back_populates='django_admin_log')


class AuthGroupPermissions(Base):
    __tablename__ = 'auth_group_permissions'
    __table_args__ = (
        ForeignKeyConstraint(['group_id'], ['auth_group.id'], deferrable=True, initially='DEFERRED', name='auth_group_permissions_group_id_b120cbf9_fk_auth_group_id'),
        ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], deferrable=True, initially='DEFERRED', name='auth_group_permissio_permission_id_84c5c92e_fk_auth_perm'),
        PrimaryKeyConstraint('id', name='auth_group_permissions_pkey'),
        UniqueConstraint('group_id', 'permission_id', name='auth_group_permissions_group_id_permission_id_0cd325b0_uniq'),
        Index('auth_group_permissions_group_id_b120cbf9', 'group_id'),
        Index('auth_group_permissions_permission_id_84c5c92e', 'permission_id')
    )

    id = Column(BigInteger, Identity(start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    group_id = Column(Integer, nullable=False)
    permission_id = Column(Integer, nullable=False)

    group = relationship('AuthGroup', back_populates='auth_group_permissions')
    permission = relationship('AuthPermission', back_populates='auth_group_permissions')


class AuthUserUserPermissions(Base):
    __tablename__ = 'auth_user_user_permissions'
    __table_args__ = (
        ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], deferrable=True, initially='DEFERRED', name='auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm'),
        ForeignKeyConstraint(['user_id'], ['auth_user.id'], deferrable=True, initially='DEFERRED', name='auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id'),
        PrimaryKeyConstraint('id', name='auth_user_user_permissions_pkey'),
        UniqueConstraint('user_id', 'permission_id', name='auth_user_user_permissions_user_id_permission_id_14a6b632_uniq'),
        Index('auth_user_user_permissions_permission_id_1fbb5f2c', 'permission_id'),
        Index('auth_user_user_permissions_user_id_a95ead1b', 'user_id')
    )

    id = Column(BigInteger, Identity(start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    user_id = Column(Integer, nullable=False)
    permission_id = Column(Integer, nullable=False)

    permission = relationship('AuthPermission', back_populates='auth_user_user_permissions')
    user = relationship('AuthUser', back_populates='auth_user_user_permissions')
"""

# 주어진 코드를 기반으로 각 테이블에 대한 모델 파일 생성
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
print(models_definition)
DATABASE_URL = "postgresql://postgres:0814@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)
metadata = MetaData()
metadata.reflect(bind=engine)


Base = declarative_base(metadata=metadata)

def generate_model_for_table(table_name, directory):
    columns = metadata.tables[table_name].columns
    class_definition = f"class {table_name}(Base):\n"
    class_definition += f"    __table__ = metadata.tables['{table_name}']\n"

    for column in columns:
        col_type = str(column.type)
        class_definition += f"    {column.name} = Column({col_type})\n"

    with open(os.path.join(directory, f"{table_name.lower()}.py"), "w") as f:
        f.write(class_definition)

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
'''