import typer

from conquerdsa.cli.init import init

app = typer.Typer(
    name="conquerdsa",
    help="An intelligent DSA companion for tracking, analyzing, and improving your coding journey.",
)

app.command()(init)


@app.command()
def version() -> None:
    """Display the current ConquerDSA version."""
    typer.echo("ConquerDSA v0.1.0")

from conquerdsa.cli.doctor import doctor
app.command()(doctor)