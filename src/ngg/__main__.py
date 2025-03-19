import sys

def entry_ngg():
    from ngg.ngg import main
    main(sys.argv[1:])
    
if __name__ == "__main__":
    entry_ngg()