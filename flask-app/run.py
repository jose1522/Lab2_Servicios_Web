from core import *
import platform

osName = platform.system()
app = create_app('Windows')

if osName == 'Darwin':
    app = create_app('Darwin')

if __name__ == "__main__":
    app.run()
