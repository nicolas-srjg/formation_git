import os
import logging

def maine():

    logging.info("The script is now working in the directory: " + os.getcwd())

if __name__ == "__main__":
    print("Hello world!")

    maine()

