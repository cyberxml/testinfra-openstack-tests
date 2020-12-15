import pytest

@pytest.mark.parametrize("name", [
    ("openstack-nova-api.noarch"),
    ("openstack-nova-common.noarch"),
    ("openstack-nova-compute.noarch"),
    ("openstack-nova-conductor.noarch"),
    ("openstack-nova-migration.noarch"),
    ("openstack-nova-novncproxy.noarch"),
    ("openstack-nova-scheduler.noarch"),
    ("puppet-nova.noarch"),
    ("python3-nova.noarch"),
    ("python3-novaclient.noarch"),
])
def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed

def test_listening_interfaces(host):
    sckt = host.socket("tcp://0.0.0.0:8774")
    assert sckt.is_listening

@pytest.mark.parametrize("process,enabled", [
    #("openstack-nova-api", True),
    ("openstack-nova-scheduler", True),
    ("openstack-nova-conductor", True),
    ("openstack-nova-novncproxy", True),
])
def test_services(host, process, enabled):
    svc = host.service(process)
    assert svc.is_running
    if enabled:
        assert svc.is_enabled

@pytest.mark.parametrize("service,conf_file", [
    ("nova", "nova.conf"),
    ("nova", "api-paste.ini"),
    ("nova", "policy.json"),
])
def test_main_services_files(host, service, conf_file):
    _file = host.file("/etc/" + service + "/" + conf_file)
    assert _file.exists
