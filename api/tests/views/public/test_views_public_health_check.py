def test_health_check(tst):
    ret = tst.client.get("/health_check/")
    assert ret.status_code == 200
    assert ret.json == {"message": "Hello World"}
