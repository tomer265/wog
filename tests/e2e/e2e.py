from selenium.webdriver.common.by import By
import helpers


def test_scores_service(url: str) -> bool:
    drivers = helpers.get_drivers_for_existing_browsers()
    for driver in drivers:
        try:
            driver.get(url)
            element = driver.find_element(By.ID, 'score')
            if element is None:
                print('No score element was found on page.')
                return False
            parsed_value = int(element.text)
            if 0 < parsed_value < 1001:
                pass
            else:
                print('Result value is not in range between 1 and 1000,')
                return False
            driver.close()
        except Exception as ex:
            print(f'A fatal error has occurred during the test with driver {driver}: {ex}')
            return False
    return True


def main_function() -> int:
    if test_scores_service('http://127.0.0.1:8777'):
        return 0
    else:
        return 1


main_function()