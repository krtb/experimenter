"""Representaion of the Owned Experiments Page."""

from selenium.webdriver.common.by import By

from pages.base import Base


class OwnedExperiments(Base):

    _owned_text_locator = (By.CSS_SELECTOR, ".m-0")
    _page_wait_locator = (
        By.CSS_SELECTOR,
        "body.page-list-view",
    )


    @property
    def count(self):
        """Return the number of owned experiments."""
        num = self.find_element(*self._owned_text_locator).text
        return int(num.split()[0])

    @property
    def title(self):
        return self.find_element(*self._owned_text_locator).text
