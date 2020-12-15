import pytest

@pytest.mark.parametrize("name", [
    ("openstack-cinder"),
    #("python-cinderclient"),
    ("openstack-selinux"),
    # ("openstack-utils")
])
def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed

@pytest.mark.parametrize("process,enabled", [
    ("openstack-cinder-volume", True),
    ("openstack-cinder-backup", True),
])
def test_services(host, process, enabled):
    svc = host.service(process)
    assert svc.is_running
    if enabled:
        assert svc.is_enabled

@pytest.mark.parametrize("service,conf_file", [
    ("cinder", "cinder.conf"),
    ("cinder", "api-paste.ini"),
    ("cinder", "rootwrap.conf"),
    #("cinder", "policy.json"),
])
def test_main_services_files(host, service, conf_file):
    _file = host.file("/etc/" + service + "/" + conf_file)
    assert _file.exists
