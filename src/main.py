import typer
from src.algo.factorial import factorial, factorial_recursive
from src.algo.fibo import fibo, fibo_recursive
from src.structs.stack import Stack
from src.const import ALGO_MAP\

app = typer.Typer()




@app.command()
def stack(operations: str):
    """
    Execute a sequence of stack operations.
    Supported ops: push <int>, pop, peek
    """
    ops = operations.strip().split()
    s = Stack()
    i = 0
    output_lines = []

    while i < len(ops):
        op = ops[i]
        if op == "push":
            if i + 1 >= len(ops):
                typer.echo("Error: 'push'", err=True)
                raise typer.Exit(1)
            try:
                val = int(ops[i + 1])
                s.push(val)
                i += 2
            except ValueError:
                typer.echo(f"Error: invalid integer '{ops[i + 1]}'", err=True)
                raise typer.Exit(1)
        elif op == "pop":
            try:
                val = s.pop()
                output_lines.append(f"pop: {val}")
                i += 1
            except IndexError as e:
                output_lines.append(f"pop: ERROR: {e}")
                i += 1
        elif op == "peek":
            try:
                val = s.peek()
                output_lines.append(f"peek: {val}")
                i += 1
            except IndexError as e:
                output_lines.append(f"peek: ERROR: {e}")
                i += 1
        else:
            typer.echo(f"Unknown operation: '{op}'", err=True)
            raise typer.Exit(1)

    if output_lines:
        for line in output_lines:
            typer.echo(line)

@app.command()
def factorial_cmd(n: int, recursive: bool = typer.Option(False, "-r")):
    """Compute factorial of n, -r for recursive."""
    try:
        func = factorial_recursive if recursive else factorial
        result = func(n)
        method = "recursive" if recursive else "iterative"
        typer.echo(f"{n}! = {result} ({method})")
    except ValueError as e:
        typer.echo(f"Error: {e}", err=True)

@app.command()
def fibo_cmd(n: int, recursive: bool = typer.Option(False, "-r")):
    """Compute n Fibonacci number, -r for recursive."""
    try:
        func = fibo_recursive if recursive else fibo
        result = func(n)
        method = "recursive" if recursive else "iterative"
        typer.echo(f"F({n}) = {result} ({method})")
    except ValueError as e:
        typer.echo(f"Error: {e}", err=True)

@app.command()
def sort_cmd(numbers: str, algo: str = typer.Option(help="Sorting algorithm")):
    """Sort a space-separated list of integers."""
    try:
        arr = list(map(int, numbers.split()))
    except ValueError:
        typer.echo("Error: Please provide integers separated by spaces.", err=True)
        raise typer.Exit(code=1)

    if algo not in ALGO_MAP:
        typer.echo(f"Unknown algorithm: {algo}. Available: {', '.join(ALGO_MAP.keys())}", err=True)
        raise typer.Exit(code=1)

    result = ALGO_MAP[algo](arr)
    typer.echo(" ".join(map(str, result)))


@app.command()
def interactive():
    in_stack = Stack()
    typer.echo("Algorithm in interactive mode")
    typer.echo("Available commands:")
    typer.echo("  factorial <n>        - iterative factorial")
    typer.echo("  factorial -r <n>    - recursive factorial")
    typer.echo("  fibo <n>             - iterative Fibonacci")
    typer.echo("  fibo -r <n>         - recursive Fibonacci")
    typer.echo(f"  sort <algo> <nums>   - sort numbers (algorithms: {', '.join(ALGO_MAP.keys())})")
    typer.echo("  stack push <x>       - push to stack")
    typer.echo("  stack pop            - pop from stack")
    typer.echo("  stack peek           - peek top")
    typer.echo("  q                    - exit\n")

    while True:
        try:
            user_input = typer.prompt("lab3> ").strip()
        except typer.Abort:
            typer.echo("\nBye!")
            break

        if not user_input:
            continue

        if user_input.lower() == "q":
            typer.echo("Bye!")
            break

        parts = user_input.split()
        cmd = parts[0].lower()
        if cmd == "factorial":
            if len(parts) == 2:
                n = int(parts[1])
                res = factorial(n)
                typer.echo(f"{n}! = {res} (iterative)")
            elif len(parts) == 3 and parts[1].lower() == "-r":
                n = int(parts[2])
                res = factorial_recursive(n)
                typer.echo(f"{n}! = {res} (recursive)")
            else:
                typer.echo("Usage: factorial <n>  OR  factorial -r <n>")

        elif cmd == "fibo":
            if len(parts) == 2:
                n = int(parts[1])
                res = fibo(n)
                typer.echo(f"F({n}) = {res} (iterative)")
            elif len(parts) == 3 and parts[1].lower() == "-r":
                n = int(parts[2])
                res = fibo_recursive(n)
                typer.echo(f"F({n}) = {res} (recursive)")
            else:
                typer.echo("Usage: fibo <n>  OR  fibo -r <n>")
        elif cmd == "sort":
            if len(parts) < 3:
                typer.echo("Usage: sort <algorithm> <num1> <num2> ...")
                typer.echo(f"Available algorithms: {', '.join(ALGO_MAP.keys())}")
                continue

            algo_name = parts[1]
            if algo_name not in ALGO_MAP:
                typer.echo(f"Unknown algorithm '{algo_name}'. Available: {', '.join(ALGO_MAP.keys())}")
                continue

            try:
                if algo_name == "bucket":
                    nums = [float(x) for x in parts[2:]]
                else:
                    nums = [int(x) for x in parts[2:]]

                result = ALGO_MAP[algo_name](nums)
                typer.echo(" → " + " ".join(map(str, result)))
            except Exception as e:
                typer.echo(f"Error during sorting: {e}")

        elif cmd == "stack":
            if len(parts) < 2:
                typer.echo("Usage: stack push <x> | stack pop | stack peek")
                continue
            subcmd = parts[1].lower()
            try:
                if subcmd == "push":
                    if len(parts) < 3:
                        typer.echo("Usage: stack push <integer>")
                        continue
                    x = int(parts[2])
                    in_stack.push(x)
                    typer.echo(f"Pushed {x}")
                elif subcmd == "pop":
                    val = in_stack.pop()
                    typer.echo(f"Popped: {val}")
                elif subcmd == "peek":
                    val = in_stack.peek()
                    typer.echo(f"Top: {val}")
                else:
                    typer.echo("Unknown stack command. Use: push, pop, peek")
            except (IndexError, ValueError) as e:
                typer.echo(f"Stack error: {e}")

        else:
            typer.echo(f"Unknown command: {cmd}")


if __name__ == "__main__":
    app()
