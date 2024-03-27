from sqlalchemy import MetaData, Table, Column, Text
from sqlalchemy import create_engine, insert


conn = create_engine("sqlite:///cryptid.db")
meta = MetaData()
explorer_table = Table(
    "explorer",
    meta,
    Column("name", Text, primary_key=True),
    Column("country", Text),
    Column("description", Text),
)
insert(explorer_table).values(
    name="Beau Buffette",
    country="US",
    description="...",
)
