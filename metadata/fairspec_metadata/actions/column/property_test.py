from .property import get_base_property_type, get_is_nullable_property_type


class TestGetBasePropertyType:
    def test_returns_type_for_string(self):
        assert get_base_property_type("string") == "string"

    def test_returns_base_type_for_type_null(self):
        assert get_base_property_type(["string", "null"]) == "string"

    def test_returns_base_type_for_null_type(self):
        assert get_base_property_type(["null", "string"]) == "string"

    def test_returns_none_for_none(self):
        assert get_base_property_type(None) is None


class TestGetIsNullablePropertyType:
    def test_returns_false_for_string(self):
        assert get_is_nullable_property_type("string") is False

    def test_returns_true_for_type_null(self):
        assert get_is_nullable_property_type(["string", "null"]) is True

    def test_returns_true_for_null_type(self):
        assert get_is_nullable_property_type(["null", "string"]) is True

    def test_returns_false_for_none(self):
        assert get_is_nullable_property_type(None) is False
