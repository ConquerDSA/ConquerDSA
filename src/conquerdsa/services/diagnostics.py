from conquerdsa.config.manager import ConfigManager
from conquerdsa.models.diagnostic import DiagnosticResult
from conquerdsa.services.github import GitHubService
from conquerdsa.services.leetcode import LeetCodeService
from conquerdsa.services.system import SystemService


class DiagnosticService:

    @staticmethod
    def run() -> list[DiagnosticResult]:

        results = []

        results.append(
            DiagnosticResult(
                "Python",
                True,
                SystemService.python_version(),
            )
        )

        results.append(
            DiagnosticResult(
                "Git",
                SystemService.git_installed(),
                "Installed" if SystemService.git_installed() else "Not Found",
            )
        )

        if not ConfigManager.exists():
            results.append(
                DiagnosticResult(
                    "Configuration",
                    False,
                    "Missing",
                )
            )
            return results

        config = ConfigManager.load()

        results.append(
            DiagnosticResult(
                "Configuration",
                True,
                "Found",
            )
        )

        github = config["github"]["username"]
        leetcode = config["leetcode"]["username"]

        results.append(
            DiagnosticResult(
                "GitHub",
                GitHubService.validate_username(github),
                github,
            )
        )

        results.append(
            DiagnosticResult(
                "LeetCode",
                LeetCodeService.validate_username(leetcode),
                leetcode,
            )
        )

        return results