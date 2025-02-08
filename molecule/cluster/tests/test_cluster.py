def test_service_is_running(host):
    service = host.service("named")
    assert service.is_running
    assert service.is_enabled
