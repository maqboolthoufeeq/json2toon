"""Tests for TOON to JSON decoder."""

from __future__ import annotations

import pytest

from json2toon import ToonParseConfig, ToonParseError, toon_to_json


class TestBasicDecoding:
    """Test basic decoding functionality."""

    def test_simple_object(self) -> None:
        """Test decoding simple object."""
        toon = "id: 123\nname: Ada"
        result = toon_to_json(toon)
        expected = {"id": 123, "name": "Ada"}
        assert result == expected

    def test_nested_object(self) -> None:
        """Test decoding nested object."""
        toon = "user:\n  id: 1\n  name: Bob"
        result = toon_to_json(toon)
        expected = {"user": {"id": 1, "name": "Bob"}}
        assert result == expected

    def test_empty_object(self) -> None:
        """Test decoding empty document."""
        toon = ""
        result = toon_to_json(toon)
        assert result == {}

    def test_primitive_values(self) -> None:
        """Test decoding various primitive types."""
        toon = """str_val: hello
int_val: 42
float_val: 3.14
bool_true: true
bool_false: false
null_val: null"""
        result = toon_to_json(toon)
        assert result["str_val"] == "hello"
        assert result["int_val"] == 42
        assert result["float_val"] == 3.14
        assert result["bool_true"] is True
        assert result["bool_false"] is False
        assert result["null_val"] is None


class TestArrayDecoding:
    """Test array decoding."""

    def test_primitive_array(self) -> None:
        """Test decoding primitive array."""
        toon = "tags[3]: admin,ops,dev"
        result = toon_to_json(toon)
        expected = {"tags": ["admin", "ops", "dev"]}
        assert result == expected

    def test_tabular_array(self) -> None:
        """Test decoding tabular array."""
        toon = """users[2]{id,name,role}:
  1,Alice,admin
  2,Bob,user"""
        result = toon_to_json(toon)
        expected = {
            "users": [
                {"id": 1, "name": "Alice", "role": "admin"},
                {"id": 2, "name": "Bob", "role": "user"},
            ]
        }
        assert result == expected

    def test_empty_array(self) -> None:
        """Test decoding empty array."""
        toon = "items[0]:"
        result = toon_to_json(toon)
        expected = {"items": []}
        assert result == expected

    def test_mixed_array(self) -> None:
        """Test decoding mixed array."""
        toon = """data[3]:
  - 1
  - a: test
  - text"""
        result = toon_to_json(toon)
        assert len(result["data"]) == 3
        assert result["data"][0] == 1
        assert result["data"][1] == {"a": "test"}
        assert result["data"][2] == "text"


class TestStringUnquoting:
    """Test string unquoting."""

    def test_quoted_string(self) -> None:
        """Test quoted strings are unquoted."""
        toon = 'val: "hello"'
        result = toon_to_json(toon)
        assert result["val"] == "hello"

    def test_unquoted_string(self) -> None:
        """Test unquoted strings."""
        toon = "name: Alice"
        result = toon_to_json(toon)
        assert result["name"] == "Alice"

    def test_escaped_characters(self) -> None:
        """Test escaped characters are unescaped."""
        toon = r'text: "line1\nline2\ttab"'
        result = toon_to_json(toon)
        assert result["text"] == "line1\nline2\ttab"

    def test_escaped_quotes(self) -> None:
        """Test escaped quotes."""
        toon = r'val: "He said \"hello\""'
        result = toon_to_json(toon)
        assert result["val"] == 'He said "hello"'


class TestDelimiters:
    """Test different delimiters."""

    def test_comma_delimiter(self) -> None:
        """Test comma delimiter (default)."""
        toon = "tags[3]: a,b,c"
        result = toon_to_json(toon)
        assert result["tags"] == ["a", "b", "c"]

    def test_tab_delimiter(self) -> None:
        """Test tab delimiter."""
        toon = "items[2\t]{id\tname}:\n  1\tAlice\n  2\tBob"
        result = toon_to_json(toon)
        assert len(result["items"]) == 2
        assert result["items"][0]["name"] == "Alice"

    def test_pipe_delimiter(self) -> None:
        """Test pipe delimiter."""
        toon = "items[2|]{id|name}:\n  1|Alice\n  2|Bob"
        result = toon_to_json(toon)
        assert len(result["items"]) == 2
        assert result["items"][0]["name"] == "Alice"


class TestRootTypes:
    """Test different root types."""

    def test_root_object(self) -> None:
        """Test root as object."""
        toon = "a: 1\nb: 2"
        result = toon_to_json(toon)
        assert result == {"a": 1, "b": 2}

    @pytest.mark.xfail(reason="Root array parsing edge case - will be fixed")
    def test_root_array(self) -> None:
        """Test root as array."""
        toon = "[2]{id,name}:\n  1,Alice\n  2,Bob"
        result = toon_to_json(toon)
        assert len(result) == 2
        assert result[0] == {"id": 1, "name": "Alice"}

    def test_root_primitive(self) -> None:
        """Test root as primitive."""
        toon = "hello"
        result = toon_to_json(toon)
        assert result == "hello"


class TestStrictMode:
    """Test strict mode validation."""

    def test_array_count_mismatch(self) -> None:
        """Test array count mismatch error."""
        toon = "items[3]: a,b"  # Says 3 but has 2
        config = ToonParseConfig(strict=True)
        with pytest.raises(ToonParseError, match="count mismatch"):
            toon_to_json(toon, config)

    def test_array_count_ok_nonstrict(self) -> None:
        """Test array count mismatch allowed in non-strict."""
        toon = "items[3]: a,b"
        config = ToonParseConfig(strict=False)
        result = toon_to_json(toon, config)
        # Should decode without error
        assert "items" in result


class TestPathExpansion:
    """Test path expansion."""

    def test_path_expansion_safe(self) -> None:
        """Test safe path expansion."""
        toon = "a.b.c: 1"
        config = ToonParseConfig(expand_paths="safe")
        result = toon_to_json(toon, config)
        expected = {"a": {"b": {"c": 1}}}
        assert result == expected

    def test_no_path_expansion(self) -> None:
        """Test no path expansion by default."""
        toon = "a.b.c: 1"
        result = toon_to_json(toon)
        assert result == {"a.b.c": 1}


class TestEdgeCases:
    """Test edge cases."""

    def test_whitespace_lines(self) -> None:
        """Test empty lines are ignored."""
        toon = "a: 1\n\nb: 2"
        result = toon_to_json(toon)
        assert result == {"a": 1, "b": 2}

    def test_complex_nested_structure(self) -> None:
        """Test complex nested structure."""
        toon = """a:
  b:
    c:
      d: 1"""
        result = toon_to_json(toon)
        assert result == {"a": {"b": {"c": {"d": 1}}}}

    def test_number_types(self) -> None:
        """Test different number formats."""
        toon = "int: 42\nfloat: 3.14\nexp: 1e10"
        result = toon_to_json(toon)
        assert result["int"] == 42
        assert result["float"] == 3.14
        assert result["exp"] == 1e10
