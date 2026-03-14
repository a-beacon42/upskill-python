from refactor_tasks import TaskManager, TaskError


def main():
    tm = TaskManager()

    # Add tasks
    tm.add(title="Write docs", priority=2, owner="alice", tags=["docs"])
    tm.add(title="Fix bug #42", priority=4, owner="bob", tags=["bugfix", "urgent"])
    tm.add(title="Code review", priority=3, owner="alice", tags=["review"])
    tm.add(title="Deploy v2", priority=5, owner="charlie", tags=["ops", "urgent"])

    # Filter
    print(tm.get_tasks(owner="alice"))
    # Expected: 2 tasks for alice

    print(tm.get_tasks(tag="urgent"))
    # Expected: Fix bug #42, Deploy v2

    print(tm.get_tasks(done=False))
    # Expected: all 4

    # Complete and check
    tm.complete(title="Write docs", owner="alice")
    print(tm.get_tasks(owner="alice", done=True))
    # Expected: just Write docs

    # Remove
    removed = tm.remove(title="Fix bug #42", owner="bob")
    print(f"Removed: {removed}")
    print(tm.summary())
    # Expected: total=3, done=1, pending=2

    # Duplicates
    try:
        tm.add(title="Write docs", priority=2, owner="alice")
        print("BUG: duplicate should have been rejected")
    except TaskError as e:
        print(f"Caught: {e}")

    # Invalid
    for bad in [
        {"title": "", "priority": 3, "owner": "dave"},
        {"title": "Ok task", "priority": 0, "owner": "dave"},
        {"title": "Ok task", "priority": 3, "owner": ""},
    ]:
        try:
            tm.add(**bad)
            print("BUG: should have been rejected")
        except TaskError as e:
            print(f"Caught: {e}")


if __name__ == "__main__":
    main()
