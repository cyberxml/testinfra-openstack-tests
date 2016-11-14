import pytest

@pytest.mark.parametrize("name", [
    ("openstack-selinux"),
    ("openstack-utils"),
    ("ntpd"),
])
def test_packages(Package, name):
    assert Package(name).is_installed

@pytest.mark.parametrize("process,enabled", [
    ("ntpd", True),
    ("selinux", True),
])
def test_services(Service, process, enabled):
    service = Service(process)
    assert service.is_running
    if enabled:
        assert service.is_enabled

@pytest.mark.parametrize("service,conf_file", [
    ("", "ntp.conf"),
    ("sysconfig", "selinux"),
])
def test_main_services_files(File, service, conf_file):
    _file = File("/etc/" + service + "/" + conf_file)
    assert _file.exists
