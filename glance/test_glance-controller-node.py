import pytest

@pytest.mark.parametrize("name", [
    # ("openstack-utils"),
    # ("python-glance-store"),
    # ("python-glanceclient"),
    ("openstack-glance"),
    # ("python-glance"),
])
def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed

def test_listening_interfaces(host):
    sckt = host.socket("tcp://0.0.0.0:9292")
    assert sckt.is_listening

@pytest.mark.parametrize("process,enabled", [
    ("openstack-glance-api", True),
    ("openstack-glance-registry", True),
])
def test_services(host, process, enabled):
    svc = host.service(process)
    assert svc.is_running
    if enabled:
        assert svc.is_enabled

@pytest.mark.parametrize("service,conf_file", [
    ("glance", "glance-api.conf"),
    ("glance", "glance-cache.conf"),
    ("glance", "glance-registry.conf"),
    ("glance", "glance-scrubber.conf"),
    ("glance", "schema-image.json"),
    #("glance", "policy.json"),
])
def test_main_services_files(host, service, conf_file):
    _file = host.file("/etc/" + service + "/" + conf_file)
    assert _file.exists
