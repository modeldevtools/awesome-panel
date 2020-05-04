"""# Bootstrap Dashboard Page.

Creates a Bootstrap Dashboard Page with a Chart and a Table

- inspired by the [GetBoostrap Dashboard Template]
(https://getbootstrap.com/docs/4.4/examples/dashboard/)
- implemented using the `awesome_panel' Python package and in particular the
`awesome_panel.express.templates.BootstrapDashboardTemplate`
"""
import pathlib

import hvplot.pandas  # pylint: disable=unused-import
import pandas as pd
import panel as pn

import awesome_panel.express as pnx

IMAGE_PATH = (
    pathlib.Path(__file__).parent
    / "assets"
    / "images"
    / "bootstrap_dashboard_template_original.png"
)
TEXT = """\
The purpose of this app is to test that a **multi-page Dashboard Layout** similar to the [bootstrap dashboard template](https://getbootstrap.com/docs/4.3/examples/dashboard/) from [getboostrap.com](https://getbootstrap.com/) can be implemented in [Panel](https://panel.pyviz.org/).

The layout with a header, navigation sidebar and a main area is what powers [awesome-panel.org](https://awesome-panel.org).

You can see how the template is implemented
[here](https://github.com/MarcSkovMadsen/awesome-panel/tree/master/package/awesome_panel/express/templates/bootstrap_dashboard)

The template is generally avaiable in the [awesome_panel](https://pypi.org/project/awesome-panel/)
python package via `awesome_panel.express.templates.BootstrapDashboardTemplate`."""


def view() -> pn.Column:
    """# Bootstrap Dashboard Page.

    Creates a Bootstrap Dashboard Page with a Chart and a Table

    - inspired by the [GetBoostrap Dashboard Template]
    (https://getbootstrap.com/docs/4.4/examples/dashboard/)
    - implemented using the `awesome_panel' Python package and in particular the
    `awesome_panel.express.templates.BootstrapDashboardTemplate`

    Returns:
        pn.Column -- The Orders View
    """
    table = pn.Pane(_get_table_data(), sizing_mode="stretch_width",)
    return pn.Column(
        pn.pane.Markdown(TEXT),
        # pn.pane.PNG(str(IMAGE_PATH), max_width=600, sizing_mode="scale_both"),
        pnx.Title("Dashboard"),
        pn.layout.Divider(),
        _holoviews_chart(),
        pnx.Title("Section Title"),
        pn.layout.Divider(),
        table,
        sizing_mode="stretch_width",
        name="Dashboard",
    )


def _holoviews_chart():
    """## Dashboard Orders Chart generated by HoloViews"""
    data = _get_chart_data()
    line_plot = data.hvplot.line(
        x="Day", y="Orders", width=None, height=500, line_color="#007BFF", line_width=6,
    )
    scatter_plot = data.hvplot.scatter(x="Day", y="Orders", height=300,).opts(
        marker="o", size=10, color="#007BFF",
    )
    fig = line_plot * scatter_plot
    gridstyle = {
        "grid_line_color": "black",
        "grid_line_width": 0.1,
    }
    fig = fig.opts(
        responsive=True,
        toolbar=None,
        yticks=list(range(12000, 26000, 2000,)),
        ylim=(12000, 26000,),
        gridstyle=gridstyle,
        show_grid=True,
    )
    return fig


def _get_chart_data() -> pd.DataFrame:
    """## Chart Data

    Returns:
        pd.DataFrame -- A DataFrame with dummy data and columns=["Day", "Orders"]
    """

    chart_data = {
        "Day": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",],
        "Orders": [15539, 21345, 18483, 24003, 23489, 24092, 12034,],
    }
    return pd.DataFrame(chart_data)


def _get_table_data() -> pd.DataFrame:
    """## Table Data

    Returns:
        pd.DataFrame -- A DataFrame with dummy data and columns=
        ["Header0", "Header1", "Header2", "Header3", "Header4"]
    """

    table_data = [
        (1001, "Lorem", "ipsum", "dolor", "sit",),
        (1002, "amet", "consectetur", "adipiscing", "elit",),
        (1003, "Integer", "nec", "odio", "Praesent",),
        (1003, "libero", "Sed", "cursus", "ante",),
        (1004, "dapibus", "diam", "Sed", "nisi",),
        (1005, "Nulla", "quis", "sem", "at",),
        (1006, "nibh", "elementum", "imperdiet", "Duis",),
        (1007, "sagittis", "ipsum", "Praesent", "mauris",),
        (1008, "Fusce", "nec", "tellus", "sed",),
        (1009, "augue", "semper", "porta", "Mauris",),
        (1010, "massa", "Vestibulum", "lacinia", "arcu",),
        (1011, "eget", "nulla", "Class", "aptent",),
        (1012, "taciti", "sociosqu", "ad", "litora",),
        (1013, "torquent", "per", "conubia", "nostra",),
        (1014, "per", "inceptos", "himenaeos", "Curabitur",),
        (1015, "sodales", "ligula", "in", "libero",),
    ]
    return pd.DataFrame(
        table_data, columns=["Header0", "Header1", "Header2", "Header3", "Header4",],
    ).set_index("Header0")
