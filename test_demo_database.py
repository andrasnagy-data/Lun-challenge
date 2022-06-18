import unittest

from demo_database import (
    execute_create_and_insert_sql_command,
    get_followers,
    create_connection
)
from CONSTANTS.GENERAL import DATABASE_NAME
from CONSTANTS.TEST import (
    TEST_DATABASE_NAME,
    TEST_COMMAND_AND_PARAMS,
    TEST_VALUES,
    EXPECTED_FOLLOWER_VALUES
)


class Test_execute_create_and_insert_sql_command(unittest.TestCase):
    '''
    Class to hold test logic for testing the
    create_db_add_users_and_relationship_tables_and_insert_values
    function.
    '''
    def setUp(self) -> None:
        '''
        Method to set up test environment.
        '''
        self.connection =  create_connection(TEST_DATABASE_NAME)
        execute_create_and_insert_sql_command(
            self.connection,
            TEST_COMMAND_AND_PARAMS
        )

    def tearDown(self) -> None:
        '''
        Method to tear down test environment.
        '''
        pass
    
    def test_execute_create_and_insert_sql_command(self) -> None:
        '''
        Method to test execute_create_and_insert_sql_command function.

        Test procedure:
        Set up toy database, check if "SELECT * FROM toy" gives the
        expected result.
        '''
        self.connection = create_connection(TEST_DATABASE_NAME)
        self.cursor = self.connection.cursor()

        return_values = []
        for row in self.cursor.execute('SELECT * FROM test'):
            return_values.append(row)
        
        self.assertEqual(return_values[0], TEST_VALUES)


class Test_get_followers(unittest.TestCase):
    '''
    Class to hold the logic for testing the get_followers function.
    '''
    def setUp(self) -> None:
        '''
        Method to set up test environment.
        '''
        pass

    def tearDown(self) -> None:
        '''
        Method to tear down test environment.
        '''
        pass

    def test_get_followers(self) -> None:
        '''
        Method to test the get followers function.

        Test procedure:
        Connect to demo_database.db, get the followers of id=1
        and check if it gives expected result.
        '''
        self.connection = create_connection(DATABASE_NAME)
        
        followers_of_id1 = get_followers(1)
        followers_of_id1 = [
            follower.__dict__ for follower in followers_of_id1
        ]
        first_follower = followers_of_id1[0]

        self.assertCountEqual(
            list(first_follower.values()),
            EXPECTED_FOLLOWER_VALUES
        )



if __name__ == '__main__':
    unittest.main()