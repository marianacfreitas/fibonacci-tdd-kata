import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Fibonacci function
    This code implements the Fibonacci function using Test-Driven Development, the sequence is defined by:
    - F(0) = 0
    - F(1) = 1
    - F(n) = F(n−1) + F(n−2)    for n ≥ 2
    """)
    return


@app.cell
def _():
    import marimo as mo
    import pytest

    return (mo,)


@app.function
# Refactored fibonacci
def fibonacci(n):
    n1 = 0
    n2 = 1
    for i in range(n):
        temp = n1
        n1 = n2
        n2 = temp+n2
    return n1


@app.cell
def _():
    # --- List of tests to pass ----

    def test_fibonacci1():
        assert fibonacci(0) == 0

    def test_fibonacci2():
        assert fibonacci(1) == 1

    def test_fibonacci3():
        assert fibonacci(2) == 1

    def test_fibonacci4():
        assert fibonacci(3) == 2

    return


@app.cell
def _(mo):
    n = mo.ui.number(
            start=0,
            stop=50,
            step=1,
            value=5,
            label="Choose n:"
        )

    n
    return (n,)


@app.cell
def _(mo, n):
    result = fibonacci(n.value)

    
    mo.md(
            f"""
            ## Result

            Fibonacci({n.value}) = **{result}**
            """
        )
    return


if __name__ == "__main__":
    app.run()
