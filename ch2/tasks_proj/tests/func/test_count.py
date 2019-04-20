import tasks
import pytest

@pytest.mark.count
def test_return_type():
    """tasks.count() should return int"""
    task = tasks.Task('do something')
    tasks.add(task)
    count = tasks.count()
    assert isinstance(count, int)

@pytest.mark.count
def test_after_add():
    """tasks's count should add 1 after tasks.add()"""
    count_before = tasks.count()
    task = tasks.Task('do something')
    tasks.add(task)
    count_after = tasks.count()
    assert count_after == count_before + 1

@pytest.mark.count
def test_after_del():
    """tasks'count should sub 1 after tasks.del()"""
    task_id = tasks.add(tasks.Task('something'))
    count_before = tasks.count()
    tasks.delete(task_id)
    count_after = tasks.count()
    assert count_after == count_before - 1

@pytest.mark.count
def test_after_del_all():
    """tasks's count should be 0 after tasks.delete_all()"""
    task_id = tasks.add(tasks.Task('something'))
    tasks.delete_all()
    count_after = tasks.count()
    assert count_after == 0

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()