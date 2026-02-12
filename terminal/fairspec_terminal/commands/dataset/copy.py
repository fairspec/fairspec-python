from fairspec_library import load_dataset, save_dataset

from fairspec_terminal.params import Debug, Json, RequiredPath, Silent, ToPathRequired
from fairspec_terminal.program import dataset_program
from fairspec_terminal.session import Session


@dataset_program.command()
def copy(
    path: RequiredPath,
    to_path: ToPathRequired,
    silent: Silent = False,
    debug: Debug = False,
    json: Json = False,
) -> None:
    """Copy a local or remote dataset to a local folder."""
    session = Session(silent=silent, debug=debug, json=json)

    def _copy() -> None:
        dataset = load_dataset(path)
        save_dataset(dataset, target=to_path)  # type: ignore[arg-type]

    session.task("Copy dataset", _copy)

    session.render_text_result(
        f"Copied dataset from [bold]{path}[/bold] to [bold]{to_path}[/bold]",
        status="success",
    )
