import nox


@nox.session
@nox.parametrize("version", ["functional", "broken"])
def build(session: nox.Session, version: str):
    session.install(
        "-r", f"requirements-{version}.in", "-c", f"requirements-{version}.txt"
    )
    session.run("mkdocs", "build", "-d", f"site-{version}")
