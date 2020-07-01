from core import *
import platform

osName = platform.system()
app = create_app(osName)

if __name__ == "__main__":
    app.run()
