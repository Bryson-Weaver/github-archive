# GitHub Archive MongoDB Project

## Description

This project is a Python application that uses MongoDB to store and manage data from the GitHub Archive dataset. The program connects to a local MongoDB database and allows the user to create, read, update, and delete commit information.

The GitHub Archive data is imported into MongoDB Compass before running the Python program.

## Requirements

* Python 3
* MongoDB
* MongoDB Compass
* PyMongo

## Installing PyMongo

Open the Terminal on a Mac and run:

```bash
python3 -m pip install pymongo
```

## MongoDB Setup

Open MongoDB Compass and connect to:

```text
mongodb://localhost:27017
```

Create a database named:

```text
GitHubArchive
```

Create a collection named:

```text
Commits
```

The `Commits.json` file from the GitHub Archive dataset should be imported into the `Commits` collection.

The database should look like this:

```text
GitHubArchive
└── Commits
```

## Running the Program

Make sure MongoDB is running.

Open Terminal and go to the folder containing the Python file.

Run:

```bash
python3 github_archive_app.py
```

The program will display a menu with different options.

## Program Features

### CRUD Operations

**Create**
Allows the user to add a new commit to the MongoDB database.

**Read**
Allows the user to search for a commit using its commit ID.

**Update**
Allows the user to change the message of an existing commit.

**Delete**
Allows the user to delete a commit using its commit ID.

### Additional Features

**Search Repository**
Allows the user to search for commits from a specific repository.

**Longest Repository Names**
Displays some of the longest repository names found in the GitHub Archive data.

**Most Common Words**
Counts words used in commit messages and displays the most common words.

## Technologies Used

* Python
* MongoDB
* MongoDB Compass
* PyMongo

## Database Information

The Python program connects to MongoDB using:

```python
client = pymongo.MongoClient("mongodb://localhost:27017/")
```

It then uses:

```python
db = client["GitHubArchive"]
collection = db["Commits"]
```

The program works with the data that was imported into MongoDB Compass.

## Project Files

```text
github_archive_app.py
README.md
Commits.json
```

`github_archive_app.py` contains the Python application.

`README.md` contains the project instructions.

`Commits.json` contains the GitHub Archive commit data.

## GitHub Commit Messages

Some example commit messages used while developing the project are:

```text
Add MongoDB connection
Add CRUD operations
Add repository search
Add repository statistics
Add common words feature
Update README
```
