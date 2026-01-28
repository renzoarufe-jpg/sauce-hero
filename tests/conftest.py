import pytest
import os
from datetime import datetime

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, page):
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        print("\n📸 ¡Queso! El test falló, sacando evidencia...")
        
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        
        timestamp = datetime.now().strftime("%H-%M-%S")
        file_name = f"screenshots/{request.node.name}_{timestamp}.png"
        
        page.screenshot(path=file_name, full_page=True)