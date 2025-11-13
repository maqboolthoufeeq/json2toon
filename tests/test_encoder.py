"""Tests for JSON to TOON encoder."""

from __future__ import annotations

import pytest

from json2toon import ToonConfig, json_to_toon


class TestBasicEncoding:
    """Test basic encoding functionality."""

    def test_simple_object(self) -> None:
        """Test encoding simple object."""
        data = {"id": 123, "name": "Ada"}
        result = json_to_toon(data)
        expected = "id: 123\nname: Ada"
        assert result == expected

    def test_nested_object(self) -> None:
        """Test encoding nested object."""
        data = {"user": {"id": 1, "name": "Bob"}}
        result = json_to_toon(data)
        expected = "user:\n  id: 1\n  name: Bob"
        assert result == expected

    def test_empty_object(self) -> None:
        """Test encoding empty object."""
        data: dict[str, str] = {}
        result = json_to_toon(data)
        assert result == ""

    def test_primitive_values(self) -> None:
        """Test encoding various primitive types."""
        data = {
            "str_val": "hello",
            "int_val": 42,
            "float_val": 3.14,
            "bool_true": True,
            "bool_false": False,
            "null_val": None,
        }
        result = json_to_toon(data)
        assert "str_val: hello" in result
        assert "int_val: 42" in result
        assert "float_val: 3.14" in result
        assert "bool_true: true" in result
        assert "bool_false: false" in result
        assert "null_val: null" in result


class TestArrayEncoding:
    """Test array encoding."""

    def test_primitive_array(self) -> None:
        """Test encoding primitive array."""
        data = {"tags": ["admin", "ops", "dev"]}
        result = json_to_toon(data)
        expected = "tags[3]: admin,ops,dev"
        assert result == expected

    def test_tabular_array(self) -> None:
        """Test encoding tabular array."""
        data = {
            "users": [
                {"id": 1, "name": "Alice", "role": "admin"},
                {"id": 2, "name": "Bob", "role": "user"},
            ]
        }
        result = json_to_toon(data)
        assert "users[2]{id,name,role}:" in result
        assert "1,Alice,admin" in result
        assert "2,Bob,user" in result

    def test_empty_array(self) -> None:
        """Test encoding empty array."""
        data = {"items": []}
        result = json_to_toon(data)
        expected = "items[0]:"
        assert result == expected

    @pytest.mark.xfail(reason="Mixed array encoding edge case - will be fixed")
    def test_mixed_array(self) -> None:
        """Test encoding mixed array."""
        data = {"data": [1, {"a": "test"}, "text"]}
        result = json_to_toon(data)
        assert "data[3]:" in result
        assert "- 1" in result
        assert "- a: test" in result
        assert "- text" in result

    def test_nested_array(self) -> None:
        """Test encoding array of arrays."""
        data = {"pairs": [[1, 2], [3, 4]]}
        result = json_to_toon(data)
        assert "pairs[2]:" in result


class TestStringQuoting:
    """Test string quoting logic."""

    def test_empty_string(self) -> None:
        """Test empty string is quoted."""
        data = {"empty": ""}
        result = json_to_toon(data)
        assert 'empty: ""' in result

    def test_reserved_words(self) -> None:
        """Test reserved words are quoted."""
        data = {"val1": "true", "val2": "false", "val3": "null"}
        result = json_to_toon(data)
        assert 'val1: "true"' in result
        assert 'val2: "false"' in result
        assert 'val3: "null"' in result

    def test_numeric_strings(self) -> None:
        """Test numeric-like strings are quoted."""
        data = {"val": "123"}
        result = json_to_toon(data)
        assert 'val: "123"' in result

    def test_special_characters(self) -> None:
        """Test strings with special characters are quoted."""
        data = {"url": "http://example.com:8080"}
        result = json_to_toon(data)
        assert '"http://example.com:8080"' in result

    def test_unquoted_safe_string(self) -> None:
        """Test safe strings are not quoted."""
        data = {"name": "Alice"}
        result = json_to_toon(data)
        assert "name: Alice" in result


class TestConfiguration:
    """Test encoder configuration options."""

    def test_custom_indent(self) -> None:
        """Test custom indentation size."""
        data = {"user": {"name": "Bob"}}
        config = ToonConfig(indent_size=4)
        result = json_to_toon(data, config)
        assert "user:\n    name: Bob" in result

    def test_tab_delimiter(self) -> None:
        """Test tab delimiter."""
        data = {"items": [{"id": 1, "name": "Ada"}]}
        config = ToonConfig(delimiter="\t")
        result = json_to_toon(data, config)
        assert "[1\t]{id\tname}:" in result

    def test_pipe_delimiter(self) -> None:
        """Test pipe delimiter."""
        data = {"items": [{"id": 1, "name": "Ada"}]}
        config = ToonConfig(delimiter="|")
        result = json_to_toon(data, config)
        assert "[1|]{id|name}:" in result

    def test_key_folding(self) -> None:
        """Test key folding."""
        data = {"a": {"b": {"c": 1}}}
        config = ToonConfig(key_folding="safe")
        result = json_to_toon(data, config)
        assert "a.b.c: 1" in result


class TestNumberCanonicalization:
    """Test number canonicalization."""

    def test_integer_conversion(self) -> None:
        """Test float that's an integer is converted."""
        data = {"val": 5.0}
        result = json_to_toon(data)
        assert "val: 5" in result

    def test_decimal_format(self) -> None:
        """Test numbers are in decimal format."""
        data = {"val": 1000000}
        result = json_to_toon(data)
        assert "val: 1000000" in result

    def test_nan_to_null(self) -> None:
        """Test NaN is converted to null."""
        data = {"val": float("nan")}
        result = json_to_toon(data)
        assert "val: null" in result

    def test_inf_to_null(self) -> None:
        """Test Infinity is converted to null."""
        data = {"val": float("inf")}
        result = json_to_toon(data)
        assert "val: null" in result


class TestRootTypes:
    """Test different root types."""

    def test_root_object(self) -> None:
        """Test root as object."""
        data = {"a": 1, "b": 2}
        result = json_to_toon(data)
        assert "a: 1" in result
        assert "b: 2" in result

    def test_root_array(self) -> None:
        """Test root as array."""
        data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        result = json_to_toon(data)
        assert "[2]{id,name}:" in result
        assert "1,Alice" in result


class TestEdgeCases:
    """Test edge cases."""

    def test_deeply_nested(self) -> None:
        """Test deeply nested structure."""
        data = {"a": {"b": {"c": {"d": {"e": 1}}}}}
        result = json_to_toon(data)
        assert "e: 1" in result

    def test_complex_structure(self) -> None:
        """Test complex mixed structure."""
        data = {
            "users": [
                {"id": 1, "name": "Alice", "tags": ["admin", "ops"]},
            ],
            "meta": {"count": 1, "version": "1.0"},
        }
        result = json_to_toon(data)
        # Should encode successfully
        assert "users[1]:" in result
        assert "meta:" in result

    def test_unicode_strings(self) -> None:
        """Test unicode strings."""
        data = {"name": "José", "emoji": "🎉"}
        result = json_to_toon(data)
        assert "José" in result
        assert "🎉" in result
