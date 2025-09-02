from sqlalchemy import UUID, Column, DateTime, ForeignKey, MetaData, String, Table

meta_data = MetaData()

user_table = Table(
    "users",
    meta_data,
    Column("id", UUID(as_uuid=False), nullable=False, primary_key=True),
    Column("created_at", DateTime(timezone=True), nullable=False),
)

mesh_account_table = Table(
    "mesh_accounts",
    meta_data,
    Column("id", UUID(as_uuid=False), nullable=False, primary_key=True),
    Column("user_id", UUID(as_uuid=False), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, primary_key=True),
    Column("access_token", String(), nullable=False),
    Column("created_at", DateTime(timezone=True), nullable=False),
)
