import pytest

@pytest.mark.parametrize("name", [
    ("openstack-nova-api"),
    ("openstack-nova-cert"),
    ("openstack-nova-conductor"),
    ("openstack-nova-console"),
    ("openstack-nova-novncproxy"),
    ("openstack-nova-scheduler"),
    ("python-novaclient"),
    ("openstack-utils"),
    ("openstack-selinux"),
])
def test_packages(Package, name, version):
    assert Package(name).is_installed

def test_listening_interfaces(Socket):
    socket = Socket("tcp://0.0.0.0:8774")
    assert socket.is_listening

@pytest.mark.parametrize("process,enabled", [
    ("openstack-nova-api", True),
    ("openstack-nova-cert", True),
    ("openstack-nova-consoleauth", True),
    ("openstack-nova-scheduler", True),
    ("openstack-nova-conductor", True),
    ("openstack-nova-novncproxy", True),
])
def test_services(Service, process, enabled):
    service = Service(process)
    assert service.is_running
    if enabled:
        assert service.is_enabled

@pytest.mark.parametrize("service,conf_file", [
    ("nova", "nova.conf"),
    ("nova", "api-paste.ini"),
    ("nova", "policy.json"),
])
def test_main_services_files(File, service, conf_file):
    _file = File("/etc/" + service + "/" + conf_file)
    assert _file.exists
