import sys

from dataclasses import dataclass

from app.Classes.logger import Logger

# import sqlparse - available if you need it!


logger = Logger('main')

def handleCommand(db_file, command):

    if command == ".dbinfo":
        with open(db_file, "rb") as database_file:
            logger.log(['main'], f'Handling Command : {command}')
            # Uncomment this to pass the first stage
            database_file.seek(16)  # Skip the first 16 bytes of the header
            page_size = int.from_bytes(database_file.read(2), byteorder="big")
            
            database_file.seek(103)
            number_of_tables = int.from_bytes(database_file.read(2), byteorder="big")
            
            # Logging
            logger.log(['main', 'handleCommand'], f"database page size: {page_size}")
            logger.log(['main', 'handleCommand'], f"number of tables: {number_of_tables}")
            
            # Prints
            print(f"database page size: {page_size}")
            print(f"number of tables: {number_of_tables}")
            
    else:
        logger.log(['main', 'handleCommand'], f"Invalid command: {command}")

def main(args):
    database_file_path = args[1]
    command = args[2]

    handleCommand(database_file_path, command)
    


if __name__ == '__main__':
    main(sys.argv)