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
    


@app.cell
def _():
    import marimo as mo

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

    


@app.cell
def _(mo):
    n = mo.ui.number(
            start=0,
            stop=50,
            step=1,
            value=5,
            label="Choose n:"
        )
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
    


@app.cell
def _():
    # Test for large values
    def test_fibonacci_100():
        assert fibonacci(100) == 354224848179261915075

    def test_fibonacci_1000():
        assert fibonacci(1000) == (
            43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
        )

    


@app.function
# using the fast doubling method to optimize fibonacci for large numbers
def fibonacci_large_numbers(n):
    n1 = 0
    n2 = 1

    for bit in bin(n)[2:]:
        n3 = n1 * (2 * n2 - n1)
        n4 = n1 * n1 + n2 * n2

        if bit == "0":
            n1 = n3
            n2 = n4
        else:
            n1 = n4
            n2 = n3 + n4

    return n1


@app.cell
def _():
    # Test for large values
    def test_fibonacci_100_v2():
        assert fibonacci_large_numbers(100) == 354224848179261915075

    def test_fibonacci_1000_v2():
        assert fibonacci_large_numbers(1000) == (
            43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
        )


if __name__ == "__main__":
    app.run()
