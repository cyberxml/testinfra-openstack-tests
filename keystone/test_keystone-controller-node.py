import pytest

@pytest.mark.parametrize("name", [
    ("openstack-keystone.noarch"),
    ("puppet-keystone.noarch"),
    ("python3-keystone.noarch"),
    ("python3-keystoneauth1.noarch"),
    ("python3-keystoneclient.noarch"),
    ("python3-keystonemiddleware.noarch"),
])

def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed

@pytest.mark.parametrize("name,port", [
    ("keystone_user","5000"),
])
def test_listening_interfaces(host, name, port):
    sckt = host.socket("tcp://" + port)
    assert sckt.is_listening

@pytest.mark.parametrize("service,conf_file", [
    ("keystone", "keystone.conf"),
    ("keystone", "policy.json"),
    ("keystone", "logging.conf"),
])
def test_main_services_files(host, service, conf_file):
    _file = host.file("/etc/" + service + "/" + conf_file)
    assert _file.exists
