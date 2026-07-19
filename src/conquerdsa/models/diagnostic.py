from dataclasses import dataclass


@dataclass
class DiagnosticResult:
    name: str
    passed: bool
    message: str