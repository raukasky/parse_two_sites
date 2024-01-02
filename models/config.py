from alembic import context

from core.config import settings


def get_url() -> str:
    contour = context.get_x_argument(as_dictionary=True).get('ctr')
    if contour not in ['dev', 'prod']:
        raise Exception('''set ctr parameter 
              Example:
              'alembic revision -x ctr=dev --autogenerate -m "tests"''')
    match contour:
        case 'dev':
            server = ''
            port = ''
            db = ''
            user = ''
            password = ''
        case 'prod':
            server = settings.POSTGRES_SERVER
            port = settings.POSTGRES_PORT
            db = settings.POSTGRES_DB
            user = settings.POSTGRES_USER
            password = settings.POSTGRES_PASSWORD
    return f'postgresql://{user}:{password}@{server}:{port}/{db}'  # noqa
