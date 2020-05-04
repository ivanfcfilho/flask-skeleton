def test_error_400(tst):
    ret = tst.client.get("/robots/")
    assert ret.status_code == 404
    assert ret.json == {"message": "The URL requested doesn't exist"}
