import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    queue = PriorityQueue()
    assert len(queue) == 0

    list_elements = [
        {"qtd_linhas": 20, "nome": "file1.txt"},
        {"qtd_linhas": 3, "nome": "file3.txt"},
        {"qtd_linhas": 230, "nome": "file2.txt"},
    ]
    for element in list_elements:
        queue.enqueue(element)
    assert len(queue) == 3
    assert len(queue.high_priority) == 1
    assert len(queue.regular_priority) == 2

    with pytest.raises(IndexError, match='Índice Inválido ou Inexistente'):
        queue.search(5)
    assert queue.search(0) == list_elements[1]
    assert queue.search(1) == list_elements[0]
    assert queue.search(2) == list_elements[2]

    queue.dequeue()
    assert queue.search(0) == list_elements[0]
    queue.dequeue()
    assert queue.search(0) == list_elements[2]
