"""
tests
"""
import pytest
from app import cli, do_something

# from pytest_mock import mocker

# From https://realpython.com/python-cli-testing/#mocks

@pytest.fixture(params=['ndict', 'dict'], name='init_transform_fixture')
def generate_initial_transform_parameters(request, mocker):
    """fixture"""
    mocker.patch.object(do_something, 'is_good_is_nice', return_value='nice')

    test_input = {
        'name': 'John Q. Public',
        'street': '123 Main St.',
        'city': 'Anytown',
        'state': 'FL',
        'zip': 99999,
    }
    expected_output = {
        'name': 'John Q. Public',
        'street': '123 Main St.',
        'city': 'Anytown',
        'state': 'FL',
        'zip': 99999,
    }
    if request.param == 'dict':
        test_input['relationships'] = {
            'siblings': ['Michael R. Public', 'Suzy Q. Public'],
            'parents': ['John Q. Public Sr.', 'Mary S. Public'],
        }
        expected_output['siblings'] = ['Michael R. Public', 'Suzy Q. Public']
        expected_output['parents'] = ['John Q. Public Sr.', 'Mary S. Public']

    return test_input, expected_output

def test_initial_transform(init_transform_fixture):
    """Test"""
    test_input = init_transform_fixture[0]
    expected_output = init_transform_fixture[1]
    assert cli.initial_transform(test_input) == expected_output
