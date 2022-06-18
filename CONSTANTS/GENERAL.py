from typing import Any, Dict, List, Tuple, Type, Union

from CONSTANTS.SQL_COMMANDS import (
    CREATE_USERS_TABLE,
    CREATE_RELATIONSHIPS_TABLE,
    INSERT_RELATIONSHIP,
    INSERT_USER
)


LOG_FILE: str = 'error.log'

DATABASE_NAME: str = 'demo_database.db'

JSON = Union[Dict[str, Any], List[Any], int, str, float, bool, Type[None]]

USERS: List[Tuple[Any]] = [
    (1, 'Andras', 'Nagy'),
    (2, 'Sara', 'Horvath'),
    (3, 'Mate', 'Nagy')
]

RELATIONSHIPS: List[Tuple[Any]] = [
    (1, 3),
    (1, 2),
    (2, 3),
    (2, 1),
    (3, 2),
    (3, 1)
]

SET_UP_DB_COMMANDS_AND_PARAMS: Dict[str, Union[Tuple[Any], None]] = {
    CREATE_USERS_TABLE: None,
    CREATE_RELATIONSHIPS_TABLE: None,
    INSERT_USER: USERS,
    INSERT_RELATIONSHIP: RELATIONSHIPS,
}