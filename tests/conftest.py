# Import the necessary modules
import pytest
import pytest_html
from _pytest.runner import TestReport

# Define a pytest hook to add extra information to the HTML report
@pytest.hookimpl(tryfirst=True)
def pytest_html_results_table_row(report: TestReport, cells):
    # Check if the report contains extra information
    if hasattr(report, 'extra_info'):
        # Add the extra information as a new column in the report table
        extra_info = str(report.extra_info)
        cells.insert(2, pytest_html.widgets.Html(extra_info))

# Your test case
class MyTest:

    def test_example(self):
        # Perform test steps

        # Add extra information to the test report
        self.report_extra_info("Additional information")

    # Custom method to add extra information to the report
    def report_extra_info(self, extra_info):
        report = self.pytest_report_item  # Get the pytest report item
        setattr(report, 'extra_info', extra_info)

