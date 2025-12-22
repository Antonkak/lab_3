import pytest
from typer.testing import CliRunner
from src.main import app

runner = CliRunner()

def test_interactive_factorial_and_fibo():
    input_sequence = "\n".join([
        "factorial 4",
        "factorial -r 3",
        "fibo 5",
        "fibo -r 4",
        "q"
    ])
    result = runner.invoke(app, ["interactive"], input=input_sequence)

    assert result.exit_code == 0
    assert "24 (iterative)" in result.output
    assert "6 (recursive)" in result.output
    assert "F(5) = 5 (iterative)" in result.output
    assert "F(4) = 3 (recursive)" in result.output
    assert "Bye!" in result.output

def test_interactive_stack():
    input_sequence = "\n".join([
        "stack push 100",
        "stack push 200",
        "stack peek",
        "stack pop",
        "stack pop",
        "q"
    ])
    result = runner.invoke(app, ["interactive"], input=input_sequence)

    assert result.exit_code == 0
    assert "Pushed 100" in result.output
    assert "Pushed 200" in result.output
    assert "Top: 200" in result.output
    assert "Popped: 200" in result.output
    assert "Popped: 100" in result.output

def test_interactive_sort():
    input_sequence = "\n".join([
        "sort bubble 4 2 1",
        "sort quick 5 3 1 4",
        "q"
    ])
    result = runner.invoke(app, ["interactive"], input=input_sequence)

    assert result.exit_code == 0
    assert "→ 1 2 4" in result.output
    assert "→ 1 3 4 5" in result.output
