import sqlite3
from pathlib import Path

from conquerdsa.config.manager import ConfigManager


class DatabaseManager:
    DATABASE_NAME = "conquerdsa.db"

    @classmethod
    def database_path(cls) -> Path:
        return ConfigManager.config_dir() / cls.DATABASE_NAME

    @classmethod
    def connect(cls) -> sqlite3.Connection:
        connection = sqlite3.connect(cls.database_path())

        connection.row_factory = sqlite3.Row

        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("PRAGMA journal_mode = WAL")

        return connection