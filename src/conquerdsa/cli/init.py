import typer
from rich.console import Console

from conquerdsa.config.manager import ConfigManager
from conquerdsa.exceptions.service import ServiceUnavailableError
from conquerdsa.services.leetcode import LeetCodeService

console = Console()


def init() -> None:
    """Initialize ConquerDSA."""

    console.print("\n[bold green]🚀 Welcome to ConquerDSA![/bold green]")
    console.print("Let's configure your intelligent DSA companion.\n")

    from conquerdsa.services.github import GitHubService
    while True:
     github_username = typer.prompt("GitHub Username")

     try:
        if GitHubService.validate_username(github_username):
            console.print("[green]✓ GitHub username verified[/green]")
            break

        console.print("[red]✗ GitHub username not found.[/red]")

     except ServiceUnavailableError as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(code=1)
    while True:
     leetcode_username = typer.prompt("LeetCode Username")

     try:
        if LeetCodeService.validate_username(leetcode_username):
            console.print("[green]✓ LeetCode username verified[/green]")
            break

        console.print("[red]✗ LeetCode username not found.[/red]")

     except ServiceUnavailableError as e:
        console.print(f"[red]{e}[/red]")
        raise typer.Exit(code=1)

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