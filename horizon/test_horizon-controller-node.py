import pytest

@pytest.mark.parametrize("name", [
    ("openstack-dashboard"),
    ("httpd"),
    ("memcached"),
])
def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed

@pytest.mark.parametrize("name,port", [
    ("httpd","80"),
    ("httpd-ssl","443"),
    ("memcached","11211"),
])
def test_listening_interfaces(host, name, port):
    sckt = host.socket("tcp://0.0.0.0:" + port)
    assert sckt.is_listening

@pytest.mark.parametrize("process,enabled", [
    ("httpd", True),
    ("memcached", True),
])
def test_services(host, process, enabled):
    svc = host.service(process)
    assert svc.is_running
    if enabled:
        assert svc.is_enabled

@pytest.mark.parametrize("service,conf_file", [
    ("openstack-dashboard", "local_settings"),
])
def test_main_services_files(host, service, conf_file):
    _file = host.file("/etc/" + service + "/" + conf_file)
    assert _file.exists
