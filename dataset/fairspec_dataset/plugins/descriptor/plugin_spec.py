from unittest.mock import MagicMock, patch

from fairspec_dataset.models.dataset import SaveDatasetOptions

from .plugin import DescriptorPlugin


class TestLoadDataset:
    def setup_method(self):
        self.plugin = DescriptorPlugin()

    @patch("fairspec_dataset.plugins.descriptor.plugin.load_dataset_descriptor")
    def test_loads_from_local_datapackage_json(self, mock_load: MagicMock):
        mock_dataset = MagicMock()
        mock_dataset.model_dump.return_value = {"resources": [{"name": "test", "data": []}]}
        mock_load.return_value = mock_dataset

        result = self.plugin.load_dataset("./datapackage.json")

        mock_load.assert_called_once_with("./datapackage.json")
        assert result == {"resources": [{"name": "test", "data": []}]}

    @patch("fairspec_dataset.plugins.descriptor.plugin.load_dataset_descriptor")
    def test_loads_from_local_json(self, mock_load: MagicMock):
        mock_dataset = MagicMock()
        mock_dataset.model_dump.return_value = {"resources": [{"name": "test", "data": []}]}
        mock_load.return_value = mock_dataset

        result = self.plugin.load_dataset("./dataset.json")

        mock_load.assert_called_once_with("./dataset.json")
        assert result == {"resources": [{"name": "test", "data": []}]}

    @patch("fairspec_dataset.plugins.descriptor.plugin.load_dataset_descriptor")
    def test_loads_from_absolute_path(self, mock_load: MagicMock):
        mock_dataset = MagicMock()
        mock_dataset.model_dump.return_value = {"resources": [{"name": "test", "data": []}]}
        mock_load.return_value = mock_dataset

        result = self.plugin.load_dataset("/absolute/path/datapackage.json")

        mock_load.assert_called_once_with("/absolute/path/datapackage.json")
        assert result == {"resources": [{"name": "test", "data": []}]}

    @patch("fairspec_dataset.plugins.descriptor.plugin.load_dataset_descriptor")
    def test_returns_none_for_csv(self, mock_load: MagicMock):
        result = self.plugin.load_dataset("./data.csv")

        mock_load.assert_not_called()
        assert result is None

    @patch("fairspec_dataset.plugins.descriptor.plugin.load_dataset_descriptor")
    def test_returns_none_for_xlsx(self, mock_load: MagicMock):
        result = self.plugin.load_dataset("./data.xlsx")

        mock_load.assert_not_called()
        assert result is None

    @patch("fairspec_dataset.plugins.descriptor.plugin.load_dataset_descriptor")
    def test_returns_none_for_parquet(self, mock_load: MagicMock):
        result = self.plugin.load_dataset("./data.parquet")

        mock_load.assert_not_called()
        assert result is None

    @patch("fairspec_dataset.plugins.descriptor.plugin.load_dataset_descriptor")
    def test_returns_none_for_zenodo_url(self, mock_load: MagicMock):
        result = self.plugin.load_dataset("https://zenodo.org/record/123")

        mock_load.assert_not_called()
        assert result is None


class TestSaveDataset:
    def setup_method(self):
        self.plugin = DescriptorPlugin()
        self.dataset: dict = {"resources": [{"name": "test", "data": []}]}

    @patch("fairspec_dataset.plugins.descriptor.plugin.save_dataset_descriptor")
    def test_saves_to_local_datapackage_json(self, mock_save: MagicMock):
        options = SaveDatasetOptions(target="./datapackage.json")

        result = self.plugin.save_dataset(self.dataset, options)

        mock_save.assert_called_once_with(self.dataset, path="./datapackage.json")
        assert result is not None
        assert result.path == "./datapackage.json"

    @patch("fairspec_dataset.plugins.descriptor.plugin.save_dataset_descriptor")
    def test_saves_with_absolute_path(self, mock_save: MagicMock):
        options = SaveDatasetOptions(target="/absolute/path/datapackage.json")

        result = self.plugin.save_dataset(self.dataset, options)

        mock_save.assert_called_once_with(self.dataset, path="/absolute/path/datapackage.json")
        assert result is not None
        assert result.path == "/absolute/path/datapackage.json"

    @patch("fairspec_dataset.plugins.descriptor.plugin.save_dataset_descriptor")
    def test_returns_none_for_remote_https(self, mock_save: MagicMock):
        options = SaveDatasetOptions(target="https://example.com/datapackage.json")

        result = self.plugin.save_dataset(self.dataset, options)

        mock_save.assert_not_called()
        assert result is None

    @patch("fairspec_dataset.plugins.descriptor.plugin.save_dataset_descriptor")
    def test_returns_none_for_remote_http(self, mock_save: MagicMock):
        options = SaveDatasetOptions(target="http://example.com/datapackage.json")

        result = self.plugin.save_dataset(self.dataset, options)

        mock_save.assert_not_called()
        assert result is None

    @patch("fairspec_dataset.plugins.descriptor.plugin.save_dataset_descriptor")
    def test_returns_none_for_non_datapackage_json(self, mock_save: MagicMock):
        options = SaveDatasetOptions(target="./dataset.json")

        result = self.plugin.save_dataset(self.dataset, options)

        mock_save.assert_not_called()
        assert result is None

    @patch("fairspec_dataset.plugins.descriptor.plugin.save_dataset_descriptor")
    def test_returns_none_for_csv(self, mock_save: MagicMock):
        options = SaveDatasetOptions(target="./data.csv")

        result = self.plugin.save_dataset(self.dataset, options)

        mock_save.assert_not_called()
        assert result is None

    @patch("fairspec_dataset.plugins.descriptor.plugin.save_dataset_descriptor")
    def test_returns_none_for_xlsx(self, mock_save: MagicMock):
        options = SaveDatasetOptions(target="./data.xlsx")

        result = self.plugin.save_dataset(self.dataset, options)

        mock_save.assert_not_called()
        assert result is None

    @patch("fairspec_dataset.plugins.descriptor.plugin.save_dataset_descriptor")
    def test_returns_none_for_directory(self, mock_save: MagicMock):
        options = SaveDatasetOptions(target="./data")

        result = self.plugin.save_dataset(self.dataset, options)

        mock_save.assert_not_called()
        assert result is None

    @patch("fairspec_dataset.plugins.descriptor.plugin.save_dataset_descriptor")
    def test_ignores_with_remote_option(self, mock_save: MagicMock):
        options = SaveDatasetOptions(target="./datapackage.json", with_remote=True)

        result = self.plugin.save_dataset(self.dataset, options)

        mock_save.assert_called_once_with(self.dataset, path="./datapackage.json")
        assert result is not None
        assert result.path == "./datapackage.json"
