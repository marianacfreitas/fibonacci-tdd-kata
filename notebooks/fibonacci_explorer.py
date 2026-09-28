import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt

    from fibonacci_tdd_kata import fibonacci

    return fibonacci, mo, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Fibonacci Explorer
        Pick a range below and see how fibonacci gives the output for each number in it,
        both as a list and as a chart of the distribution of outputs. This notebook consumes
        the published fibonacci_kata package — it does not reimplement the function.
    """)
    return


@app.cell
def _(mo):
    start = mo.ui.slider(1, 200, value=1, label="Range start")
    end = mo.ui.slider(1, 200, value=100, label="Range end")
    mo.hstack([start, end])
    return end, start


@app.cell
def _(end, fibonacci, start):
    lo, hi = sorted((start.value, end.value))
    inputs = list(range(lo, hi + 1))
    results = [fibonacci(n) for n in range(lo, hi + 1)]
    results
    return (results, inputs)


@app.cell
def _(inputs, plt, results):
    fig, ax = plt.subplots()
    ax.plot(results, inputs, marker="o")
    ax.set_ylabel("Fibonacci output")
    ax.set_xlabel("Input")
    ax.set_title("Fibonacci sequence over the selected range")
    fig
    return


if __name__ == "__main__":
    app.run()
