import json
import pytest
from src.q3_memory import q3_memory

def create_test_file(tmp_path, data):
    file_path = tmp_path / "test_data.json"
    with open(file_path, 'w') as f:
        for item in data:
            f.write(json.dumps(item) + '\n')
    return str(file_path)

@pytest.mark.parametrize("test_input,expected_output,test_id", [
    # Happy path tests
    ([{"mentionedUsers": [{"username": "user1"}]}, {"mentionedUsers": [{"username": "user1"}, {"username": "user2"}]}], [("user1", 2), ("user2", 1)], "happy_path_basic"),
    ([{"mentionedUsers": [{"username": "user1"}] * 5}, {"mentionedUsers": [{"username": "user2"}] * 3}], [("user1", 5), ("user2", 3)], "happy_path_multiple_mentions"),
    ([{"mentionedUsers": [{"username": "user1"}] * 10}, {"mentionedUsers": [{"username": "user2"}] * 8}]+[{"mentionedUsers": [{"username": f"user{i}"}]} for i in range(3, 11)], [("user1", 10), ("user2", 8), ("user3", 1), ("user4", 1), ("user5", 1), ("user6", 1), ("user7", 1), ("user8", 1), ("user9", 1), ("user10", 1)], "happy_path_top_ten"),
    
    # Edge cases
    ([], [], "edge_case_empty_file"),
    ([{"mentionedUsers": None}], [], "edge_case_no_mentions"),
    ([{"mentionedUsers": [{"username": None}]}], [], "edge_case_null_username"),
    ([{"notMentionedUsers": [{"username": "user1"}]}], [], "edge_case_wrong_key"),
    
    # Error cases
    ([{"mentionedUsers": "not_a_dict"}], [], "error_case_not_a_dict"),
    ([{"mentionedUsers": [{"not_username": "user1"}]}], [], "error_case_missing_username_key"),
    
    # Additional test cases
    ([{"mentionedUsers": [{"username": "user1"}]}], [("user1", 1)], "additional_test_case_single_mention"),
    ([{"mentionedUsers": [{"username": "user1"}] * 100}], [("user1", 100)], "additional_test_case_large_mention_count"),
    ([{"mentionedUsers": [{"username": "user1"}] * 1000}, {"mentionedUsers": [{"username": "user2"}] * 500}], [("user1", 1000), ("user2", 500)], "additional_test_case_multiple_mentions"),
])
def test_q3_memory(tmp_path, test_input, expected_output, test_id):
    # Arrange
    file_path = create_test_file(tmp_path, test_input)

    # Act
    result = q3_memory(file_path)

    # Assert
    assert sorted(result, key=lambda x: (int(x[0].replace('user', '')))) == expected_output, f"Failed test_id: {test_id}"
