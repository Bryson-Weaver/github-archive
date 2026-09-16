import pymongo
from collections import Counter

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["GitHubArchive"]
collection = db["Commits"]


# CREATE
def create():
    print("\nCreate a new commit")

    document = {
        "commit": input("Commit ID: "),
        "repo_name": [input("Repository name: ")],
        "subject": input("Subject: "),
        "message": input("Message: ")
    }

    collection.insert_one(document)

    print("Commit added.")


# READ
def read():
    print("\nFind a commit")

    commit_id = input("Enter commit ID: ")

    result = collection.find_one({"commit": commit_id})

    if result:
        print(result)
    else:
        print("Commit not found.")


# UPDATE
def update():
    print("\nUpdate a commit")

    commit_id = input("Enter commit ID: ")
    new_message = input("Enter new message: ")

    result = collection.update_one(
        {"commit": commit_id},
        {"$set": {"message": new_message}}
    )

    if result.modified_count > 0:
        print("Commit updated.")
    else:
        print("Commit not found.")


# DELETE
def delete():
    print("\nDelete a commit")

    commit_id = input("Enter commit ID: ")

    result = collection.delete_one(
        {"commit": commit_id}
    )

    if result.deleted_count > 0:
        print("Commit deleted.")
    else:
        print("Commit not found.")


# FEATURE 1
# Search for a repository
def search_repository():
    print("\nSearch Repository")

    repo = input("Enter repository name: ")

    results = collection.find(
        {"repo_name": repo}
    ).limit(5)

    for document in results:
        print(document)


# FEATURE 2
# Show the longest repository names
def longest_repositories():
    print("\nLongest Repository Names")

    repositories = collection.distinct("repo_name")

    # repo_name is stored as a list
    names = []

    for repo in repositories:
        if isinstance(repo, list):
            names.extend(repo)

    names.sort(key=len, reverse=True)

    for name in names[:5]:
        print(name)


# FEATURE 3
# Find common words in commit messages
def common_words():
    print("\nMost Common Words")

    words = []

    documents = collection.find(
        {},
        {"message": 1}
    )

    for document in documents:

        message = document.get("message", "")

        for word in message.lower().split():
            words.append(word.strip(".,!?():;"))

    counter = Counter(words)

    for word, count in counter.most_common(10):
        print(word, "-", count)


# MENU
while True:

    print("\n==============================")
    print("GitHub Archive MongoDB Program")
    print("==============================")

    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Search Repository")
    print("6. Longest Repository Names")
    print("7. Most Common Words")
    print("8. Exit")

    choice = input("Choose an option: ")

    match choice:

        case "1":
            create()

        case "2":
            read()

        case "3":
            update()

        case "4":
            delete()

        case "5":
            search_repository()

        case "6":
            longest_repositories()

        case "7":
            common_words()

        case "8":
            print("Goodbye!")
            break

        case _:
            print("Invalid choice.")