import hvplot.pandas
import pandas as pd
import panel as pn


def _get_chart_data() -> pd.DataFrame:
    """## Chart Data

    Returns:
        pd.DataFrame -- A DataFrame with dummy data and columns=["Day", "Orders"]
    """

    chart_data = {
        "Day": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",],
        "Orders": [15539, 21345, 18483, 24003, 23489, 24092, 12034],
    }
    return pd.DataFrame(chart_data)


def _holoviews_chart():
    """## Dashboard Orders Chart generated by HoloViews"""
    data = _get_chart_data()
    line_plot = data.hvplot.line(
        x="Day", y="Orders", width=None, height=500, line_color="#007BFF", line_width=6,
    )
    scatter_plot = data.hvplot.scatter(x="Day", y="Orders", height=300).opts(
        marker="o", size=10, color="#007BFF"
    )
    fig = line_plot * scatter_plot
    gridstyle = {"grid_line_color": "black", "grid_line_width": 0.1}
    fig = fig.opts(
        responsive=True,
        toolbar=None,
        yticks=list(range(12000, 26000, 2000)),
        ylim=(12000, 26000),
        gridstyle=gridstyle,
        show_grid=True,
    )
    return fig


chart = _holoviews_chart()
chart_panel = pn.panel(chart, css_classes=["holo-chart"])
app = pn.Column(chart_panel, width=500)
app.servable("no css_classes")
