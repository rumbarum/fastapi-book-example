from sqlalchemy import MetaData, Table, Column, Text
from sqlalchemy import create_engine, select, Row

engine = create_engine("sqlite:///db/cryptid.db")
conn = engine.connect()
meta = MetaData()
explorer_table = Table(
    "explorer",
    meta,
    Column("name", Text, primary_key=True),
    Column("country", Text),
    Column("description", Text),
)

def get_one(name: str) -> Row | None:
    stmt = select(explorer_table).where(explorer_table.c.name==name)
    result = conn.execute(stmt)
    return result.fetchone()

print(get_one("yeti"))
