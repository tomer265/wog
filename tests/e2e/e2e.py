import sys

from selenium.webdriver.common.by import By
import helpers


def test_scores_service(url: str) -> bool:
    drivers = helpers.get_drivers_for_existing_browsers()
    for driver in drivers:
        try:
            print(f'Testing driver {driver}')
            driver.get(url)
            element = driver.find_element(By.ID, 'score')
            if element is None:
                print('No score element was found on page.')
                return False
            parsed_value = int(element.text)
            if 0 < parsed_value < 1001:
                print(f'Result {parsed_value} is valid: the value is in range between 1 and 1000.')
                driver.close()
            else:
                print(f'Result {parsed_value} is not valid. The value is not in range between 1 and 1000.')
                driver.close()
                return False
        except Exception as ex:
            print(f'A fatal error has occurred during the test with driver {driver}: {ex}')
            return False
    return True


def main_function():
    if test_scores_service('http://127.0.0.1:8777'):
        sys.exit(0)
    else:
        sys.exit(1)


main_function()