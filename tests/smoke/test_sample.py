import pytest

def test_app_launch(driver):
    """Simple smoke test to verify driver initialization and app launch."""
    assert driver is not None
    print("\n[SUCCESS] Appium session started and app is launched!")