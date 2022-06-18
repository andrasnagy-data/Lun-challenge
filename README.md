# LUN BACK-END CHALLENGE
The project folder contains:
- demo_database.py
- demo_app.py
- model.py
- test_demo_database.py
- CONSTANTS folder
    - GENERAL.py
    - SQL_COMMANDS.py
    - TEST.py
- requirements.txt
- .gitignore
- docs folder


# Run demo
First create demo_database by running the command below.

```bash
user@user-pc:~/project_folder$ python3 demo_database.py
```

Then run the following commands.

```bash
user@user-pc:~/project_folder$ export FLASK_APP=demo_app.py
user@user-pc:~/project_folder$ export FLASK_ENVIRONMENT=development
user@user-pc:~/project_folder$ flask run
```

Then below links will work.
- http://127.0.0.1:5000/users/1/followers
- http://127.0.0.1:5000/users/2/followers
- http://127.0.0.1:5000/users/3/followers


# Follow up questions
1. What are potential pitfalls when expanding on your solution?

One pitfall that I can see, is the way I dealt with "id" in "users" table. As of now, I inserted the "id" -primary key- manually into "users" and did not set an auto increment. Furthermore, I manually added the relationships into the "relationships" table. One way to scale the current solution would be to get the largest "id" (assuming, one increments ids by 1) before adding a user by "SELECT max(id) FROM users", then assign the returned value + 1 as the "id" of user. Following, one would have to run queries to get the ids of the followers, and followees of user. Finally, it is possible to insert all the relationships of the user into "relationships". A better way would be to use auto increment, and to add (multiple) rows into "users" and "relationships" in a for loop and use the cursor object's "lastrowid" property, query information about the followers and folowee of user, then add this information to the tables.

2. How big would your solution scale to, and what would you do at that point?

I think the database schema is correct, and can scale, however I am aware that the API implementation is rather simplistic. One could use "flask resources" and other more advanced technologies, however my knowledge here is limited currently. Another constraining factor could be my choice of data structure -dataclass- into which i "save" the queried follower information.

3. How would you modify your implementation to support other types of followers than just Users?

Currently I use 2 tables to support the API. My solution relies on a one-to-many relationship between ("users" and "relationships").
To allow for brands to follow, I would extend my solution with another table called "brands", and set up a "many-to-many" relationship between users and brands through a one-to-many between "users and "relationships", and another one-to-many between "brands" and "relationship".
