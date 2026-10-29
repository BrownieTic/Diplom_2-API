class Url:
    MAIN_PAGE_URL = 'https://qa-stellarburgers.education-services.ru/'

class API:
    creating_user_api = f'{Url.MAIN_PAGE_URL}api/auth/register'
    delete_user_api = f'{Url.MAIN_PAGE_URL}api/auth/user'
    login_api = f'{Url.MAIN_PAGE_URL}api/auth/login'

    create_order_api = f'{Url.MAIN_PAGE_URL}api/orders'