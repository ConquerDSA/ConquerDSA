import typer
from rich.console import Console

from conquerdsa.config.manager import ConfigManager

console = Console()


def init() -> None:
    """Initialize ConquerDSA."""

    console.print("\n[bold green]🚀 Welcome to ConquerDSA![/bold green]")
    console.print("Let's configure your intelligent DSA companion.\n")

    github_username = typer.prompt("GitHub Username")
    leetcode_username = typer.prompt("LeetCode Username")

    config = {
        "version": "1",
        "github": {
            "username": github_username,
        },
        "leetcode": {
            "username": leetcode_username,
        },
        "preferences": {
            "theme": "dark",
        },
    }

    ConfigManager.save(config)

    console.print("\n[bold green]✓ Configuration saved successfully![/bold green]")
    console.print("[cyan]Happy Coding 🚀[/cyan]")