import pytest

@pytest.mark.parametrize("name", [
    ("openstack-heat-api.noarch"),
    ("openstack-heat-api-cfn.noarch"),
    ("openstack-heat-common.noarch"),
    ("openstack-heat-engine.noarch"),
    ("openstack-heat-ui.noarch"),
    ("openstack-heat-agents.noarch"),
    ("openstack-heat-monolith.noarch"),
])
def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed

@pytest.mark.parametrize("name,port", [
    ("heat-api","8004"),
    ("heat-cfn","8000"),
    ("heat-watch","8003"),
])
def test_listening_interfaces(host, name, port):
    sckt = host.socket("tcp://0.0.0.0:" + port)
    assert sckt.is_listening

@pytest.mark.parametrize("process,enabled", [
    ("chronyd", True),
    ("openstack-heat-api-cfn", True),
    #("openstack-heat-api-cloudwatch", True),
    ("openstack-heat-api", True),
    ("openstack-heat-engine", True),
])
def test_services(host, process, enabled):
    svc = host.service(process)
    assert svc.is_running
    if enabled:
        assert svc.is_enabled

@pytest.mark.parametrize("service,conf_file", [
    ("heat", "heat.conf"),
    #("heat", "policy.json"),
])
def test_main_services_files(host, service, conf_file):
    _file = host.file("/etc/" + service + "/" + conf_file)
    assert _file.exists
