from __future__ import annotations

from unittest.mock import MagicMock, patch

import polars as pl
from fairspec_metadata import OdsFileDialect, Resource, XlsxFileDialect
from fairspec_table.models.table import LoadTableOptions, SaveTableOptions

from .plugin import XlsxPlugin


class TestXlsxPluginLoadTable:
    def setup_method(self):
        self.plugin = XlsxPlugin()

    @patch("fairspec_table.plugins.xlsx.plugin.load_xlsx_table")
    def test_should_load_table_from_xlsx_file(self, mock_load: MagicMock):
        resource = Resource(data="test.xlsx")
        mock_table = pl.DataFrame().lazy()
        mock_load.return_value = mock_table

        result = self.plugin.load_table(resource)

        assert result is mock_table

    @patch("fairspec_table.plugins.xlsx.plugin.load_xlsx_table")
    def test_should_handle_explicit_xlsx_format(self, mock_load: MagicMock):
        resource = Resource(data="test.txt", fileDialect=XlsxFileDialect())
        mock_table = pl.DataFrame().lazy()
        mock_load.return_value = mock_table

        result = self.plugin.load_table(resource)

        assert result is mock_table

    @patch("fairspec_table.plugins.xlsx.plugin.load_xlsx_table")
    def test_should_pass_through_load_options(self, mock_load: MagicMock):
        resource = Resource(data="test.xlsx")
        options = LoadTableOptions(denormalized=True)
        mock_load.return_value = pl.DataFrame().lazy()

        self.plugin.load_table(resource, options)

        mock_load.assert_called_once()

    @patch("fairspec_table.plugins.xlsx.plugin.load_xlsx_table")
    def test_should_handle_paths_with_directories(self, mock_load: MagicMock):
        resource = Resource(data="/path/to/data.xlsx")
        mock_load.return_value = pl.DataFrame().lazy()

        self.plugin.load_table(resource)

        mock_load.assert_called_once()

    @patch("fairspec_table.plugins.xlsx.plugin.load_xlsx_table")
    def test_should_load_table_from_ods_file(self, mock_load: MagicMock):
        resource = Resource(data="test.ods")
        mock_table = pl.DataFrame().lazy()
        mock_load.return_value = mock_table

        result = self.plugin.load_table(resource)

        assert result is mock_table

    @patch("fairspec_table.plugins.xlsx.plugin.load_xlsx_table")
    def test_should_handle_explicit_ods_format(self, mock_load: MagicMock):
        resource = Resource(data="test.txt", fileDialect=OdsFileDialect())
        mock_table = pl.DataFrame().lazy()
        mock_load.return_value = mock_table

        result = self.plugin.load_table(resource)

        assert result is mock_table

    @patch("fairspec_table.plugins.xlsx.plugin.load_xlsx_table")
    def test_should_pass_through_ods_load_options(self, mock_load: MagicMock):
        resource = Resource(data="test.ods")
        options = LoadTableOptions(denormalized=True)
        mock_load.return_value = pl.DataFrame().lazy()

        self.plugin.load_table(resource, options)

        mock_load.assert_called_once()

    @patch("fairspec_table.plugins.xlsx.plugin.load_xlsx_table")
    def test_should_handle_ods_paths_with_directories(self, mock_load: MagicMock):
        resource = Resource(data="/path/to/data.ods")
        mock_load.return_value = pl.DataFrame().lazy()

        self.plugin.load_table(resource)

        mock_load.assert_called_once()

    @patch("fairspec_table.plugins.xlsx.plugin.load_xlsx_table")
    def test_should_return_none_for_non_xlsx_ods_files(self, mock_load: MagicMock):
        resource = Resource(data="test.csv")

        result = self.plugin.load_table(resource)

        mock_load.assert_not_called()
        assert result is None

    @patch("fairspec_table.plugins.xlsx.plugin.load_xlsx_table")
    def test_should_return_none_for_json_files(self, mock_load: MagicMock):
        resource = Resource(data="test.json")

        result = self.plugin.load_table(resource)

        mock_load.assert_not_called()
        assert result is None


class TestXlsxPluginSaveTable:
    def setup_method(self):
        self.plugin = XlsxPlugin()

    @patch("fairspec_table.plugins.xlsx.plugin.save_xlsx_table")
    def test_should_save_table_to_xlsx_file(self, mock_save: MagicMock):
        table = pl.DataFrame().lazy()
        options = SaveTableOptions(path="output.xlsx")
        mock_save.return_value = "output.xlsx"

        result = self.plugin.save_table(table, options)

        mock_save.assert_called_once_with(table, options)
        assert result == "output.xlsx"

    @patch("fairspec_table.plugins.xlsx.plugin.save_xlsx_table")
    def test_should_handle_explicit_xlsx_format(self, mock_save: MagicMock):
        table = pl.DataFrame().lazy()
        options = SaveTableOptions(path="output.txt", fileDialect=XlsxFileDialect())
        mock_save.return_value = "output.txt"

        result = self.plugin.save_table(table, options)

        mock_save.assert_called_once_with(table, options)
        assert result == "output.txt"

    @patch("fairspec_table.plugins.xlsx.plugin.save_xlsx_table")
    def test_should_handle_paths_with_directories(self, mock_save: MagicMock):
        table = pl.DataFrame().lazy()
        options = SaveTableOptions(path="/path/to/output.xlsx")
        mock_save.return_value = "/path/to/output.xlsx"

        self.plugin.save_table(table, options)

        mock_save.assert_called_once_with(table, options)

    @patch("fairspec_table.plugins.xlsx.plugin.save_xlsx_table")
    def test_should_save_table_to_ods_file(self, mock_save: MagicMock):
        table = pl.DataFrame().lazy()
        options = SaveTableOptions(path="output.ods")
        mock_save.return_value = "output.ods"

        result = self.plugin.save_table(table, options)

        mock_save.assert_called_once_with(table, options)
        assert result == "output.ods"

    @patch("fairspec_table.plugins.xlsx.plugin.save_xlsx_table")
    def test_should_handle_explicit_ods_format(self, mock_save: MagicMock):
        table = pl.DataFrame().lazy()
        options = SaveTableOptions(path="output.txt", fileDialect=OdsFileDialect())
        mock_save.return_value = "output.txt"

        result = self.plugin.save_table(table, options)

        mock_save.assert_called_once_with(table, options)
        assert result == "output.txt"

    @patch("fairspec_table.plugins.xlsx.plugin.save_xlsx_table")
    def test_should_handle_ods_paths_with_directories(self, mock_save: MagicMock):
        table = pl.DataFrame().lazy()
        options = SaveTableOptions(path="/path/to/output.ods")
        mock_save.return_value = "/path/to/output.ods"

        self.plugin.save_table(table, options)

        mock_save.assert_called_once_with(table, options)

    @patch("fairspec_table.plugins.xlsx.plugin.save_xlsx_table")
    def test_should_return_none_for_non_xlsx_ods_files(self, mock_save: MagicMock):
        table = pl.DataFrame().lazy()
        options = SaveTableOptions(path="output.csv")

        result = self.plugin.save_table(table, options)

        mock_save.assert_not_called()
        assert result is None

    @patch("fairspec_table.plugins.xlsx.plugin.save_xlsx_table")
    def test_should_return_none_for_files_without_extension(self, mock_save: MagicMock):
        table = pl.DataFrame().lazy()
        options = SaveTableOptions(path="output")

        result = self.plugin.save_table(table, options)

        mock_save.assert_not_called()
        assert result is None

    @patch("fairspec_table.plugins.xlsx.plugin.save_xlsx_table")
    def test_should_return_none_for_json_files(self, mock_save: MagicMock):
        table = pl.DataFrame().lazy()
        options = SaveTableOptions(path="output.json")

        result = self.plugin.save_table(table, options)

        mock_save.assert_not_called()
        assert result is None
