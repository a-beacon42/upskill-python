from dataclasses import dataclass, field
from typing import Optional


class TaskError(Exception):
    pass


@dataclass
class Task:
    title: str
    priority: int
    owner: str
    tags: list[str] = field(default_factory=list)
    done: bool = False

    def __post_init__(self):
        if self.title == "":
            raise TaskError("bad title")
        if self.priority < 1 or self.priority > 5:
            raise TaskError("bad priority")
        if self.owner == "":
            raise TaskError("bad owner")


class TaskManager:
    def __init__(self):
        self.data: list[Task] = []

    def make_task(
        self,
        title: str,
        priority: int,
        owner: str,
        tags: list[str] = [],
        done: bool = False,
    ) -> Task:
        task = Task(title=title, priority=priority, done=done, owner=owner, tags=tags)
        return task

    def add(
        self,
        title: str,
        priority: int,
        owner: str,
        tags: list[str] = [],
        done: bool = False,
    ):
        for task in self.data:
            if task.title == title and task.owner == owner:
                raise TaskError("dup")
        task = self.make_task(title, priority, owner, tags, done)
        self.data.append(task)

    def get_tasks(
        self, owner: str | None = None, done: bool | None = None, tag: str | None = None
    ) -> list[Task]:
        filtered = [
            task
            for task in self.data
            if (not owner or task.owner == owner)
            and (not done or task.done == done)
            and (not tag or tag in task.tags)
        ]
        return filtered

    def complete(self, title: str, owner: str) -> Task | None:
        for task in self.data:
            if task.title == title and task.owner == owner:
                task.done = True
                return task
        return None

    def remove(self, title: str, owner: str) -> Task | None:
        new = []
        removed = None
        for task in self.data:
            if task.title == title and task.owner == owner:
                removed = task
            else:
                new.append(task)
        self.data = new
        return removed

    def summary(self) -> dict:
        total = len(self.data)
        done_count = sum([1 for task in self.data if task.done])
        return {"total": total, "done": done_count, "pending": total - done_count}
