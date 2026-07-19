import typer
from rich.console import Console

from conquerdsa.models.diagnostic import DiagnosticResult
from conquerdsa.services.diagnostics import DiagnosticService

console = Console()


def doctor() -> None:
    """Run system diagnostics."""

    console.print("\n[bold blue]🔎 Running diagnostics...[/bold blue]\n")

    results = DiagnosticService.run()

    all_passed = True

    for result in results:
        if result.passed:
            console.print(
                f"[green]✓ {result.name}[/green] {result.message}"
            )
        else:
            console.print(
                f"[red]✗ {result.name}[/red] {result.message}"
            )
            all_passed = False

    if not all_passed:
        raise typer.Exit(code=1)

    console.print("\n[bold green]System is healthy! 🚀[/bold green]")