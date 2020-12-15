import pytest

@pytest.mark.parametrize("name", [
    ("redis"),
    ("python3-redis"),
    ("puppet-redis.noarch"),

])
def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed

@pytest.mark.parametrize("name,port", [
    ("redis", "6379"),
])
def test_listening_interfaces(host, name, port):
    sckt = host.socket("tcp://10.10.10.24:" + port)
    assert sckt.is_listening

@pytest.mark.parametrize("process,enabled", [
    ("redis", True),
])
def test_services(host, process, enabled):
    svc = host.service(process)
    assert svc.is_running
    if enabled:
        assert svc.is_enabled

@pytest.mark.parametrize("conf_file", [
    ("redis.conf"),
])
def test_main_services_files(host, conf_file):
    _file = host.file("/etc/" + conf_file)
    assert _file.exists
