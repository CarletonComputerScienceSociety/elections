MODE = 'test'

if MODE == 'test':
    print 'Warning! Test mode. Do not use this in prod.'

if MODE == 'test':
    # Use SQLite for our disposable database.
    SQLALCHEMY_URL = 'sqlite:///tmp/test.db'
    DEBUG = True
