from .infer import infer_resource_name


class TestInferResourceName:
    def test_infers_name_from_single_path(self):
        assert infer_resource_name({"data": "/data/users.csv"}) == "users"

    def test_infers_name_from_first_path_in_array(self):
        resource = {"data": ["/data/users.csv", "/data/backup.csv"]}
        assert infer_resource_name(resource) == "users"

    def test_infers_name_from_url(self):
        resource = {"data": "https://example.com/data/products.json"}
        assert infer_resource_name(resource) == "products"

    def test_returns_default_name_when_no_path(self):
        assert infer_resource_name({}) == "resource"

    def test_returns_default_name_when_no_filename(self):
        assert infer_resource_name({"data": "/data/folder/"}) == "resource"

    def test_handles_complex_filename(self):
        resource = {"data": "/data/file.backup.csv"}
        assert infer_resource_name(resource) == "file_backup"

    def test_slugifies_filename(self):
        resource = {"data": "/data/My Data File!.csv"}
        assert infer_resource_name(resource) == "my_data_file"

    def test_returns_numbered_default(self):
        assert infer_resource_name({}, resource_number=1) == "resource1"
