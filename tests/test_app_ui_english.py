from streamlit.testing.v1 import AppTest


def test_app_loads_without_exception():
    at = AppTest.from_file("app.py")
    at.run()
    assert not at.exception


def test_button_is_hidden_before_upload():
    at = AppTest.from_file("app.py")
    at.run()
    assert len(at.button) == 0