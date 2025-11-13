"""Tests for round-trip conversion (JSON -> TOON -> JSON)."""

from __future__ import annotations

from json2toon import json_to_toon, toon_to_json


class TestRoundTrip:
    """Test round-trip conversion."""

    def test_simple_object_roundtrip(self) -> None:
        """Test simple object round-trip."""
        original = {"id": 123, "name": "Ada"}
        toon = json_to_toon(original)
        result = toon_to_json(toon)
        assert result == original

    def test_nested_object_roundtrip(self) -> None:
        """Test nested object round-trip."""
        original = {"user": {"id": 1, "name": "Bob", "active": True}}
        toon = json_to_toon(original)
        result = toon_to_json(toon)
        assert result == original

    def test_primitive_array_roundtrip(self) -> None:
        """Test primitive array round-trip."""
        original = {"tags": ["admin", "ops", "dev"]}
        toon = json_to_toon(original)
        result = toon_to_json(toon)
        assert result == original

    def test_tabular_array_roundtrip(self) -> None:
        """Test tabular array round-trip."""
        original = {
            "users": [
                {"id": 1, "name": "Alice", "role": "admin"},
                {"id": 2, "name": "Bob", "role": "user"},
                {"id": 3, "name": "Carol", "role": "guest"},
            ]
        }
        toon = json_to_toon(original)
        result = toon_to_json(toon)
        assert result == original

    def test_mixed_array_roundtrip(self) -> None:
        """Test mixed array round-trip."""
        original = {"data": [1, {"a": "test"}, "text", True, None]}
        toon = json_to_toon(original)
        result = toon_to_json(toon)
        assert result == original

    def test_complex_structure_roundtrip(self) -> None:
        """Test complex structure round-trip."""
        original = {
            "users": [
                {"id": 1, "name": "Alice", "active": True},
                {"id": 2, "name": "Bob", "active": False},
            ],
            "meta": {
                "count": 2,
                "version": "1.0",
                "settings": {"debug": False, "timeout": 30},
            },
            "tags": ["production", "api", "v1"],
        }
        toon = json_to_toon(original)
        result = toon_to_json(toon)
        assert result == original

    def test_empty_containers_roundtrip(self) -> None:
        """Test empty containers round-trip."""
        original = {"empty_array": [], "data": {"nested": {}}}
        toon = json_to_toon(original)
        result = toon_to_json(toon)
        # Empty object becomes missing key
        assert result["empty_array"] == []

    def test_special_values_roundtrip(self) -> None:
        """Test special values round-trip."""
        original = {
            "null_val": None,
            "true_val": True,
            "false_val": False,
            "zero": 0,
            "empty_str": "",
        }
        toon = json_to_toon(original)
        result = toon_to_json(toon)
        assert result == original

    def test_numeric_strings_roundtrip(self) -> None:
        """Test numeric-looking strings round-trip."""
        original = {
            "code": "123",
            "version": "1.0",
            "bool_str": "true",
            "null_str": "null",
        }
        toon = json_to_toon(original)
        result = toon_to_json(toon)
        assert result == original

    def test_unicode_roundtrip(self) -> None:
        """Test unicode strings round-trip."""
        original = {
            "name": "José García",
            "emoji": "🎉🎊",
            "chinese": "你好",
            "arabic": "مرحبا",
        }
        toon = json_to_toon(original)
        result = toon_to_json(toon)
        assert result == original

    def test_numbers_roundtrip(self) -> None:
        """Test various number types round-trip."""
        original = {
            "int": 42,
            "negative": -17,
            "float": 3.14159,
            "zero": 0,
            "large": 1000000,
        }
        toon = json_to_toon(original)
        result = toon_to_json(toon)
        assert result == original

    def test_nested_arrays_roundtrip(self) -> None:
        """Test nested arrays round-trip."""
        original = {"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}
        toon = json_to_toon(original)
        result = toon_to_json(toon)
        assert result == original

    def test_root_array_roundtrip(self) -> None:
        """Test root array round-trip."""
        original = [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
        ]
        toon = json_to_toon(original)
        result = toon_to_json(toon)
        assert result == original

    def test_deeply_nested_roundtrip(self) -> None:
        """Test deeply nested structure round-trip."""
        original = {"a": {"b": {"c": {"d": {"e": {"f": {"g": 1}}}}}}}
        toon = json_to_toon(original)
        result = toon_to_json(toon)
        assert result == original

    def test_mixed_types_object_roundtrip(self) -> None:
        """Test object with mixed value types round-trip."""
        original = {
            "string": "hello",
            "number": 42,
            "float": 3.14,
            "bool": True,
            "null": None,
            "array": [1, 2, 3],
            "object": {"nested": "value"},
        }
        toon = json_to_toon(original)
        result = toon_to_json(toon)
        assert result == original

    def test_special_characters_roundtrip(self) -> None:
        """Test strings with special characters round-trip."""
        original = {
            "url": "http://example.com:8080",
            "path": "/path/to/file.txt",
            "with_quotes": 'He said "hello"',
            "with_newline": "line1\nline2",
            "with_tab": "col1\tcol2",
        }
        toon = json_to_toon(original)
        result = toon_to_json(toon)
        assert result == original
