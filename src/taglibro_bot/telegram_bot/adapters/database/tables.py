from sqlalchemy import UUID, BigInteger, Column, DateTime, ForeignKey, String, Table

from taglibro_bot.common.adapters.database.tables import meta_data

tg_user_table = Table(
    "tg_users",
    meta_data,
    Column("id", UUID(as_uuid=False), nullable=False, primary_key=True),
    Column(
        "user_id", UUID(as_uuid=False), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, primary_key=True
    ),
    Column("full_name", String(), nullable=True),
    Column("tg_user_id", BigInteger(), nullable=True),
    Column("tg_chat_id", BigInteger(), nullable=True),
    Column("created_at", DateTime(timezone=True), nullable=False),
)
