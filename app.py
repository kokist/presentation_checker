from utils.sidebar_setup import setup_sidebar
from utils.metainfo_setup import metainfo_setup
from pages.home import home

def main():
    setup_sidebar()
    home()

if __name__ == "__main__":
    metainfo_setup()
    main()
