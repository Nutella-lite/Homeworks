from main import get_cat_pic
def test_get_cat_pic_success(mocker):
    mock_success = mocker.patch('main.requests.get')
    mock_success.return_value.status_code = 200
    mock_success.return_value.json.return_value = [{
        "id": "dj7",
        "url": "https://cdn2.thecatapi.com/images/dj7.jpg",
        "width": 640,
        "height": 480
    }]
    assert get_cat_pic() == ('https://cdn2.thecatapi.com/images/dj7.jpg', 640, 480)

def test_get_cat_pic_fail(mocker):
    mock_fail = mocker.patch('main.requests.get')
    mock_fail.return_value.status_code = 500
    assert get_cat_pic() == None