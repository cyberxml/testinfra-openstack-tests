import pytest

@pytest.mark.parametrize("name", [
    ("openstack-selinux"),
    ("chrony"),
    ("python3-mod_wsgi"),
])
def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed

@pytest.mark.parametrize("process,enabled", [
    ("chronyd", True),
    #("selinux", True),
])
def test_services(host, process, enabled):
    svc = host.service(process)
    assert svc.is_running
    if enabled:
        assert svc.is_enabled

@pytest.mark.parametrize("service,conf_file", [
    ("selinux", "config"),
    ("", "chrony.conf"),
])
def test_main_services_files(host, service, conf_file):
    _file = host.file("/etc/" + service + "/" + conf_file)
    assert _file.exists
