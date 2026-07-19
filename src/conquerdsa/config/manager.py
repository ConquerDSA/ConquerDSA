from pathlib import Path

import tomllib
import tomli_w
from platformdirs import user_config_dir
from rich.console import Console

console = Console()


class ConfigManager:
    """Manage ConquerDSA configuration."""

    APP_NAME = "ConquerDSA"

    @classmethod
    def config_dir(cls) -> Path:
        """Return the ConquerDSA configuration directory."""
        config_dir = Path(user_config_dir(cls.APP_NAME))
        config_dir.mkdir(parents=True, exist_ok=True)
        return config_dir

    @classmethod
    def config_file(cls) -> Path:
        """Return the path to config.toml."""
        return cls.config_dir() / "config.toml"

    @staticmethod
    def initialize() -> None:
        """Initialize ConquerDSA configuration."""

        config_file = ConfigManager.config_file()

        if not config_file.exists():
            default_config = {
                "version": "1",
                "github": {
                    "username": ""
                },
                "leetcode": {
                    "username": ""
                },
                "preferences": {
                    "theme": "dark"
                }
            }

            with config_file.open("wb") as f:
                tomli_w.dump(default_config, f)

            console.print("[green]✓ Created config.toml[/green]")
        else:
            console.print("[yellow]✓ config.toml already exists[/yellow]")

        console.print(f"[cyan]{config_file}[/cyan]")

    @staticmethod
    def save(config: dict) -> None:
        """Save configuration to config.toml."""

        config_file = ConfigManager.config_file()

        with config_file.open("wb") as f:
            tomli_w.dump(config, f)

    @staticmethod
    def exists() -> bool:
        """Check whether the configuration file exists."""

        return ConfigManager.config_file().exists()

    @staticmethod
    def load() -> dict:
        """Load configuration from config.toml."""

        with ConfigManager.config_file().open("rb") as f:
            return tomllib.load(f)