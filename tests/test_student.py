from app.student import StudentDb
import pytest
import os.path

db = None
data_file = os.path.join("data", "data.json")

def setup_module(module):
    print("---------------------setup-------------------")
    global db
    db = StudentDb();db.connect(data_file)
     
def teardown_module(module):
    print("---------------------teardown--------\
        -----------")
    db.close()

def test_mosheh_data():
    result = db.get_data('Mosheh')
    assert result['name'] == 'Mosheh'
    assert result['id'] == 1, "Should be 1"
    assert result['result'] == 'failed'
