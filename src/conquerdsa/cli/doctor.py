import typer
from rich.console import Console

from conquerdsa.config.manager import ConfigManager

console = Console()


def doctor() -> None:
    """Run system diagnostics."""

    console.print("\n[bold blue]🔎 Running diagnostics...[/bold blue]\n")

    if ConfigManager.exists():
        console.print("[green]✓ Configuration found[/green]")
    else:
        console.print("[red]✗ Configuration not found[/red]")
        raise typer.Exit(code=1)

    config = ConfigManager.load()

    github_username = config["github"]["username"]
    leetcode_username = config["leetcode"]["username"]

    if github_username:
        console.print(f"[green]✓ GitHub:[/green] {github_username}")
    else:
        console.print("[yellow]! GitHub username not configured[/yellow]")

    if leetcode_username:
        console.print(f"[green]✓ LeetCode:[/green] {leetcode_username}")
    else:
        console.print("[yellow]! LeetCode username not configured[/yellow]")

    console.print("\n[bold green]System looks healthy! 🚀[/bold green]")