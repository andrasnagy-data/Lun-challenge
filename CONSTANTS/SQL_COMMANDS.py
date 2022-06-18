# no autoincrement -> prefered to use what i know
CREATE_USERS_TABLE: str = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY_KEY,
    first_name CHAR(20) NOT NULL,
    last_name CHAR(20) NOT NULL
)
'''

CREATE_RELATIONSHIPS_TABLE: str = '''
CREATE TABLE IF NOT EXISTS relationships (
    follower INTEGER NOT NULL,
    followee INTEGER NOT NULL,
    PRIMARY KEY (follower, followee),
    FOREIGN KEY(follower) REFERENCES users(id),
    FOREIGN KEY(followee) REFERENCES users(id)
)
'''

INSERT_USER: str = 'INSERT INTO users VALUES (?, ?, ?)'

INSERT_RELATIONSHIP: str = 'INSERT INTO relationships VALUES (?, ?)'

GET_FOLLOWERS_COMMAND: str = '''
SELECT users.id, users.first_name, users.last_name
FROM relationships
LEFT JOIN users ON
    users.id = relationships.followee
WHERE relationships.follower = ?
ORDER BY users.first_name ASC, users.last_name ASC
'''