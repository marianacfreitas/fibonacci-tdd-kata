import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pytest

    return


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


if __name__ == "__main__":
    app.run()
