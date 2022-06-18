from typing import Any, Dict, List, Tuple, Union

TEST_DATABASE_NAME: str = 'test.db'

CREATE_TEST_DB: str = '''
CREATE TABLE IF NOT EXISTS test (
    id INTEGER PRIMARY_KEY AUTO INCREMENT,
    test_num INTEGER NOT NULL
)
'''
INSERT_A_ROW_INTO_TEST: str = 'INSERT INTO test VALUES (?, ?)'

TEST_VALUES: Tuple[int] = (1, 3)

TEST_COMMAND_AND_PARAMS: Dict[str, Union[None, Tuple[int]]] = {
    CREATE_TEST_DB: None,
    INSERT_A_ROW_INTO_TEST: TEST_VALUES
}

EXPECTED_FOLLOWER_VALUES: List[Any] = ['Mate', 'Nagy', 3, 'Mate Nagy']