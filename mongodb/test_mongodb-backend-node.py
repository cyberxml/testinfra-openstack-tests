import pytest

@pytest.mark.parametrize("name", [
    ("mariadb"),
    ("mariadb-server"),
    ("python2-PyMySQL"),
])
def test_packages(Package, name):
    assert Package(name).is_installed

@pytest.mark.parametrize("name,port", [
    ("mongod","27017"),
])
def test_listening_interfaces(Socket, name, port):
    socket = Socket("tcp://" + port)
    assert socket.is_listening

@pytest.mark.parametrize("process,enabled", [
    ("mariadb", True),
])
def test_services(Service, process, enabled):
    service = Service(process)
    assert service.is_running
    if enabled:
        assert service.is_enabled

@pytest.mark.parametrize("service,conf_file", [
    ("keystone", "keystone.conf"),
    ("keystone", "policy.json"),
    ("keystone", "keystone-paste.ini"),
    ("keystone", "logging.conf"),
])
def test_main_services_files(File, service, conf_file):
    _file = File("/etc/" + service + "/" + conf_file)
    assert _file.exists
