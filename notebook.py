import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pytest

    return


app._unparsable_cell(
    r"""
    # Defining the signature function
    def fibonacci(n):

    """,
    name="_"
)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
