import sqlite3
from typing import Any, Dict, List, Tuple, Union
from datetime import datetime
from contextlib import redirect_stdout

from CONSTANTS.GENERAL import (
    LOG_FILE,
    DATABASE_NAME,
    SET_UP_DB_COMMANDS_AND_PARAMS
)
from CONSTANTS.SQL_COMMANDS import GET_FOLLOWERS_COMMAND
from model import UserInfo




def create_connection(database_name: str) -> sqlite3.Connection:
    '''
    Function to create a connection to <data_base_name>.
    '''
    try:
        connection = sqlite3.connect(database_name)
        return connection
    
    except sqlite3.Error as e:
        with open(LOG_FILE, 'a') as f:
            with redirect_stdout(f):
                (
                    f'\nFailed to establish connection to {database_name}:'
                    f' {e} at {datetime.now()}.'
                )
        raise e


def execute_create_and_insert_sql_command(
    connection: sqlite3.Connection,
    commands_and_parameters: (
        Dict[str, Union[Tuple[Any], List[Tuple[Any]], None]]
    )
) -> None:
    '''
    Function to execute create and insert SQL commands
    along with their (potential) values.
    '''
    try:
        cursor = connection.cursor()

        for command, parameters in commands_and_parameters.items():
            if parameters is None:
                cursor.execute(command)
                connection.commit()
            else:
                if isinstance(parameters, tuple):
                    cursor.execute(command, parameters)
                elif isinstance(parameters, list):
                    cursor.executemany(command, parameters)
        
        connection.commit()
        
    except sqlite3.Error as e:
        with open(LOG_FILE, 'a') as f:
            with redirect_stdout(f):
                (
                    f'\nFailed to execute command:'
                    f' {e} at {datetime.now()}.'
                )
        raise e

    finally:
        connection.close()


def create_db_add_users_and_relationship_tables_and_insert_values() -> None:
    '''
    Function to create database, create users & relationships table,
    then, populate the tables with values.
    '''
    try:
        connection = create_connection(DATABASE_NAME)
        execute_create_and_insert_sql_command(
            connection,
            SET_UP_DB_COMMANDS_AND_PARAMS
        )

    except sqlite3.Error as e:
        with open(LOG_FILE, 'a') as f:
            with redirect_stdout(f):
                (
                    f'\nFailed to create db, tables, and to insert values:'
                    f' {e} at {datetime.now()}.'
                )
        raise e


def get_followers(followee_id: int) -> List[Dict[str, Any]]:
    '''
    Function to get the followers of <followee_id>.
    '''
    try:
        connection = create_connection(DATABASE_NAME)
        cursor = connection.cursor()

        followers = []

        for follower in cursor.execute(
            GET_FOLLOWERS_COMMAND,
            (followee_id,)
        ):
            followers.append(
                UserInfo(
                    follower[0], # id
                    follower[1], # first name
                    follower[2], # last name
                    ' '.join([follower[1], follower[2]])
                )
            )
        
        return followers

    except sqlite3.Error as e:
        with open(LOG_FILE, 'a') as f:
            with redirect_stdout(f):
                (
                    f'\nFailed to get followers for {followee_id}:'
                    f' {e} at {datetime.now()}.'
                )
        raise e

    finally:
        cursor.close()




if __name__ == '__main__':
    create_db_add_users_and_relationship_tables_and_insert_values()
