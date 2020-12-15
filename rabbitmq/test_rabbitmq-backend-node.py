import pytest

@pytest.mark.parametrize("name", [
    ("rabbitmq-server"),
])
def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed

@pytest.mark.parametrize("name,port", [
    ("rabbitmq-server","5672"),
])
def test_listening_interfaces(host, name, port):
    sckt = host.socket("tcp://" + port)
    assert sckt.is_listening

@pytest.mark.parametrize("process,enabled", [
    ("rabbitmq-server", True),
])
def test_services(host, process, enabled):
    svc = host.service(process)
    assert svc.is_running
    if enabled:
        assert svc.is_enabled

@pytest.mark.parametrize("service,conf_file", [
    ("rabbitmq", "rabbitmq.config"),
    ("rabbitmq", "rabbitmq-env.conf"),
])
def test_main_services_files(host, service, conf_file):
    _file = host.file("/etc/" + service + "/" + conf_file)
    assert _file.exists
