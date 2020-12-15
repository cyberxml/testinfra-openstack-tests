## Generated tests for compute IaaS node @Produban
## This role and tests could not be executed by themselves, must exists a previous OSP Region installed
## Then this role could be executed on OSP version described on the folder's name.
import pytest

@pytest.mark.parametrize("name", [
    ("openstack-nova-common"),
    ("openstack-nova-compute"),
    # ("openstack-utils"),
    ("openstack-selinux"),
    # ("openstack-utils"),
])
def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed

@pytest.mark.parametrize("process,enabled", [
    ("openstack-nova-compute", True),
])
def test_services(host, process, enabled):
    svc = host.service(process)
    assert svc.is_running
    if enabled:
        assert svc.is_enabled
