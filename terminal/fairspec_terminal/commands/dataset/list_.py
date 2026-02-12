from fairspec_library import load_dataset
from fairspec_metadata import infer_resource_name

from fairspec_terminal.params import Debug, Json, RequiredPath
from fairspec_terminal.program import dataset_program
from fairspec_terminal.session import Session


@dataset_program.command(name="list")
def list_(
    path: RequiredPath,
    json: Json = False,
    debug: Debug = False,
) -> None:
    """List Dataset resources."""
    session = Session(debug=debug, json=json)

    def _load() -> object:
        dataset = load_dataset(path)
        if not dataset:
            raise ValueError("Could not load dataset")
        return dataset

    dataset = session.task("Loading dataset", _load)

    resource_names = [
        resource.name or infer_resource_name(resource)
        for resource in getattr(dataset, "resources", None) or []
    ]

    session.render_data_result(resource_names)
