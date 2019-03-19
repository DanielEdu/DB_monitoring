import os

from db_monitoring import app



if __name__ == '__main__':
    app.debug = True
    app.run()