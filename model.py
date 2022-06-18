from dataclasses import dataclass



@dataclass
class UserInfo:
    '''
    Class to hold user information.
    '''
    id: int
    first_name: str
    last_name: str
    full_name: str