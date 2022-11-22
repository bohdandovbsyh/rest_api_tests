from factory_method.chrome import Chrome
from factory_method.edge import Edge
from factory_method.firefox import FireFox


def browser_factory(browser):
    if browser == 'chrome':
        return Chrome()
    elif browser == 'edge':
        return Edge()
    elif browser == 'firefox':
        return FireFox()


if __name__ == '__main__':
    browser = browser_factory('chrome')

