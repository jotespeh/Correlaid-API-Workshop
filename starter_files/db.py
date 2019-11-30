import config
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine


Base = automap_base()

engine = create_engine(f'mysql+pymysql://{config.user}:{config.password}@mysql01.manitu.net/{config.database}')

Base.prepare(engine, reflect = True)

Item = Base.classes.todo_items

session = scoped_session(sessionmaker(bind = engine))

