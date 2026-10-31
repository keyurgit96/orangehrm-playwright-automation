from dotenv import load_dotenv
from datetime import datetime
from typing import Optional
import os


class selectEnv:
    def __init__(self, envName=None):
        self.envName = envName.lower() if envName else None

    def load(self):
        if self.envName == "custom":
            load_dotenv(os.path.join(os.path.dirname(__file__), "../../.custom.env"))
        else:
            load_dotenv(os.path.join(os.path.dirname(__file__), "../../.env"))
        if not os.getenv("AUTH"):
            os.environ["AUTH"] = (
                "./test_data/authCustom.json"
                if self.envName == "custom"
                else "./test_data/auth.json"
            )
        if not os.getenv("DATA_BASE"):
            os.environ["DATA_BASE"] = (
                "./test_data/data_custom.json"
                if self.envName == "custom"
                else "./test_data/data.json"
            )


class logger:
    def __init__(self, page, screenshot=True, snapshot=True, source=True):
        self.page = page
        self.screenshot = screenshot
        self.snapshot = snapshot
        self.source = source

    def startLogging(self):
        self.page.context.tracing.start(
            screenshots=self.screenshot, snapshots=self.snapshot, sources=self.source
        )

    def stopLogging(self, fileName=None):
        if fileName:
            os.makedirs('./logs', exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = './logs/' + timestamp + '_' + fileName + '.zip'
            self.page.context.tracing.stop(path=path)
        else:
            raise AttributeError(
                "Please provide name while stopping logger.(logger().stopLogging(FILENAME))"
            )


class Waits:
    @staticmethod
    def for_url(page, url: str, timeout: int = 30000) -> None:
        """Wait until the page URL matches the given URL exactly."""
        page.wait_for_url(url, timeout=timeout)

    @staticmethod
    def for_url_contains(page, url_fragment: str, timeout: int = 30000) -> None:
        """Wait until the page URL contains the given fragment (glob pattern)."""
        page.wait_for_url(f"**{url_fragment}**", timeout=timeout)

    @staticmethod
    def for_load_state(page, state: str = "domcontentloaded", timeout: int = 30000) -> None:
        """
        Wait for a specific page load state.
        States: 'load' | 'domcontentloaded' | 'networkidle'
        """
        page.wait_for_load_state(state, timeout=timeout)

    @staticmethod
    def for_network_idle(page, timeout: int = 30000) -> None:
        """Wait until there are no network connections for at least 500ms."""
        page.wait_for_load_state("networkidle", timeout=timeout)

    @staticmethod
    def for_navigation(page, timeout: int = 30000) -> None:
        """Wait for a navigation event (page load after a click/form submit)."""
        with page.expect_navigation(timeout=timeout):
            pass

    @staticmethod
    def for_timeout(page, ms: int) -> None:
        """
        Fixed-time wait (use sparingly — prefer event-based waits above).
        Useful only for animations or third-party iframes with no DOM signal.
        """
        page.wait_for_timeout(ms)

    @staticmethod
    def for_visible(locator, timeout: int = 30000) -> None:
        """Wait until the element is visible in the DOM."""
        locator.wait_for(state="visible", timeout=timeout)

    @staticmethod
    def for_hidden(locator, timeout: int = 30000) -> None:
        """Wait until the element is hidden or detached from the DOM."""
        locator.wait_for(state="hidden", timeout=timeout)

    @staticmethod
    def for_attached(locator, timeout: int = 30000) -> None:
        """Wait until the element exists in the DOM (even if not visible)."""
        locator.wait_for(state="attached", timeout=timeout)

    @staticmethod
    def for_enabled(locator, timeout: int = 30000) -> None:
        """Wait until the element is enabled (not disabled)."""
        locator.wait_for(state="visible", timeout=timeout)
        locator.is_enabled()

    @staticmethod
    def for_text(locator, text: str, timeout: int = 30000) -> None:
        """Wait until the element contains the specified text."""
        from playwright.sync_api import expect
        expect(locator).to_contain_text(text, timeout=timeout)


    @staticmethod
    def for_response(page, url_fragment: str, timeout: int = 30000):
        """
        Wait for a network response whose URL contains the given fragment.
        Returns the response object for further assertions.

        Example:
            response = Waits.for_response(page, "/api/v2/admin/users")
            assert response.status == 200
        """
        with page.expect_response(
            lambda r: url_fragment in r.url, timeout=timeout
        ) as response_info:
            pass
        return response_info.value

    @staticmethod
    def for_request(page, url_fragment: str, timeout: int = 30000):
        """
        Wait for an outgoing network request whose URL contains the given fragment.
        Returns the request object.
        """
        with page.expect_request(
            lambda r: url_fragment in r.url, timeout=timeout
        ) as request_info:
            pass
        return request_info.value

    @staticmethod
    def for_dialog(page, action: str = "accept", timeout: int = 30000) -> None:
        """
        Wait for and handle a browser dialog (alert/confirm/prompt).
        action: 'accept' | 'dismiss'
        """
        def handle(dialog):
            if action == "accept":
                dialog.accept()
            else:
                dialog.dismiss()
        page.once("dialog", handle)

    @staticmethod
    def for_download(page, timeout: int = 30000):
        """
        Wait for a file download to start and return the Download object.

        Example:
            download = Waits.for_download(page)
            download.save_as("./downloads/file.pdf")
        """
        with page.expect_download(timeout=timeout) as download_info:
            pass
        return download_info.value

    @staticmethod
    def for_popup(page, timeout: int = 30000):
        """
        Wait for a new popup/tab to open and return the new Page object.

        Example:
            popup = Waits.for_popup(page)
            popup.wait_for_load_state()
        """
        with page.expect_popup(timeout=timeout) as popup_info:
            pass
        return popup_info.value
