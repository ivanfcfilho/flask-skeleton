def test_error_400(tst):
    ret = tst.client.get("/robots/")
    assert ret.status_code == 404
    assert ret.json == {
        "message": "404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
    }
