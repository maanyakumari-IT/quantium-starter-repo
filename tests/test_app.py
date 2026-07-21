import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import app


def test_header_present(dash_duo):
    dash_duo.start_server(app)

    dash_duo.wait_for_text_to_equal("h1", "Pink Morsel Sales Visualizer", timeout=10)

    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel Sales Visualizer"


def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)

    dash_duo.wait_for_element("#sales-chart", timeout=10)

    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)

    dash_duo.wait_for_element("#region-filter", timeout=10)

    radio = dash_duo.find_element("#region-filter")
    assert radio is not None