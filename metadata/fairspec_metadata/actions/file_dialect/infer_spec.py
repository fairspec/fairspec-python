from .infer import infer_file_dialect_format


class TestInferFileDialectFormat:
    def test_csv(self):
        assert infer_file_dialect_format({"data": "table.csv"}) == "csv"

    def test_tsv(self):
        assert infer_file_dialect_format({"data": "table.tsv"}) == "tsv"

    def test_json(self):
        assert infer_file_dialect_format({"data": "table.json"}) == "json"

    def test_jsonl(self):
        assert infer_file_dialect_format({"data": "table.jsonl"}) == "jsonl"

    def test_ndjson_maps_to_jsonl(self):
        assert infer_file_dialect_format({"data": "table.ndjson"}) == "jsonl"

    def test_xlsx(self):
        assert infer_file_dialect_format({"data": "table.xlsx"}) == "xlsx"

    def test_ods(self):
        assert infer_file_dialect_format({"data": "table.ods"}) == "ods"

    def test_parquet(self):
        assert infer_file_dialect_format({"data": "table.parquet"}) == "parquet"

    def test_arrow(self):
        assert infer_file_dialect_format({"data": "table.arrow"}) == "arrow"

    def test_feather_maps_to_arrow(self):
        assert infer_file_dialect_format({"data": "table.feather"}) == "arrow"

    def test_sqlite(self):
        assert infer_file_dialect_format({"data": "table.sqlite"}) == "sqlite"

    def test_unknown_extension(self):
        assert infer_file_dialect_format({"data": "table.xyz"}) is None

    def test_no_data(self):
        assert infer_file_dialect_format({}) is None
