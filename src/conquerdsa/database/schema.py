from conquerdsa.database.manager import DatabaseManager


class SchemaManager:

    @staticmethod
    def initialize() -> None:

        with DatabaseManager.connect() as connection:

            connection.execute("""
                CREATE TABLE IF NOT EXISTS sync_state (
                    provider TEXT PRIMARY KEY,
                    last_sync TEXT
                )
            """)

            connection.commit()