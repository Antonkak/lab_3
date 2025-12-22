import pytest
from typer.testing import CliRunner
from src.main import app

runner = CliRunner()

def test_factorial_iterative():
    result = runner.invoke(app, ["factorial-cmd", "5"])
    assert result.exit_code == 0
    assert "120 (iterative)" in result.output

def test_factorial_recursive():
    result = runner.invoke(app, ["factorial-cmd", "5", "-r"])
    assert result.exit_code == 0
    assert "120 (recursive)" in result.output

def test_fibo_iterative():
    result = runner.invoke(app, ["fibo-cmd", "6"])
    assert result.exit_code == 0
    assert "F(6) = 8 (iterative)" in result.output

def test_fibo_recursive():
    result = runner.invoke(app, ["fibo-cmd", "6", "-r"])
    assert result.exit_code == 0
    assert "F(6) = 8 (recursive)" in result.output

def test_sort_bubble():
    result = runner.invoke(app, ["sort-cmd", "3 1 2", "--algo", "bubble"])
    assert result.exit_code == 0
    assert result.output.strip() == "1 2 3"

def test_sort_quick():
    result = runner.invoke(app, ["sort-cmd", "--algo", "quick", "5 2 8 1"])
    assert result.exit_code == 0
    assert result.output.strip() == "1 2 5 8"

def test_stack_operations():
    result = runner.invoke(app, ["stack", "push 10 push 20 pop peek"])
    assert result.exit_code == 0
    assert "pop: 20" in result.output
    assert "peek: 10" in result.output
