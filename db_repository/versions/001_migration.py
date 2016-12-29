from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
tag__attrs = Table('tag__attrs', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('attr_1_name', String(length=120)),
    Column('attr_1_value', String(length=250)),
    Column('attr_2_name', String(length=120)),
    Column('attr_2_value', String(length=250)),
    Column('attr_3_name', String(length=120)),
    Column('attr_3_value', String(length=250)),
    Column('attr_4_name', String(length=120)),
    Column('attr_4_value', String(length=250)),
    Column('attr_5_name', String(length=120)),
    Column('attr_5_value', String(length=250)),
    Column('tag_id', Integer),
)

tags = Table('tags', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('tag_name', String(length=250)),
    Column('tag_type', String(length=250)),
    Column('section_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tag__attrs'].columns['tag_id'].create()
    post_meta.tables['tags'].columns['section_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tag__attrs'].columns['tag_id'].drop()
    post_meta.tables['tags'].columns['section_id'].drop()
