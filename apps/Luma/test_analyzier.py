# tests/test_analyzer.py
import pytest

from analyzier import analyze_pattern
from enums import PropagationType

@pytest.mark.parametrize(
    "input_str, expected_output, expected_pattern",
    [
        (
            "(expr)*",
            {
                'is_identifier': False,
                'is_group': True,
                'propagation': PropagationType.ONE_TO_MANY,
            },
            "expr"
        ),
        (
            "(expr)*?",
            {
                'is_identifier': False,
                'is_group': True,
                'propagation': PropagationType.ZERO_TO_MANY,
            },
            "expr"
        ),
        (
            "&identifier?",
            {
                'is_identifier': True,
                'is_group': False,
                'propagation': PropagationType.ZERO_TO_ONE,
            },
            "identifier"
        ),
        (
            "&identifier",
            {
                'is_identifier': True,
                'is_group': False,
                'propagation': PropagationType.ONLY_ONE,
            },
            "identifier"
        ),
    ]
)
def test_analyze_pattern_valid_inputs(input_str, expected_output, expected_pattern):
    result, pattern = analyze_pattern(input_str)
    assert result == expected_output, f"Failed for input: {input_str}"
    assert pattern == expected_pattern, f"Pattern mismatch for input: {input_str}"

def test_analyze_pattern_invalid_input():
    with pytest.raises(ValueError) as exc_info:
        analyze_pattern("invalid_pattern")
    assert str(exc_info.value) == "Formato inválido de padrão!"
