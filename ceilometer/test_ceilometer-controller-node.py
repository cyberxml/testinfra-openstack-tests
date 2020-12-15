import pytest

@pytest.mark.parametrize("name", [
    #("openstack-ceilometer-central.noarch"),
    ("openstack-ceilometer-common.noarch"),
    ("openstack-ceilometer-ipmi.noarch"),
    ("openstack-ceilometer-notification.noarch"),
    ("openstack-ceilometer-polling.noarch"),
])
def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed

def test_listening_interfaces(host):
    sckt = host.socket("tcp://8777")
    assert sckt.is_listening

@pytest.mark.parametrize("process,enabled", [
    #("openstack-ceilometer-api", True),
    #("openstack-ceilometer-notification", True),
    #("openstack-ceilometer-central", True),
    #("openstack-ceilometer-collector", True),
    #("openstack-ceilometer-alarm-evaluator", True),
    #("openstack-ceilometer-alarm-notifier", True),
    #("openstack-ceilometer-ipmi.service", True),
    ("openstack-ceilometer-notification.service", True),
    ("openstack-ceilometer-polling.service", True),

])
def test_services(host, process, enabled):
    svc = host.service(process)
    assert svc.is_running
    if enabled:
        assert svc.is_enabled

@pytest.mark.parametrize("service,conf_file", [
    ("ceilometer", "ceilometer.conf"),
    ("ceilometer", "pipeline.yaml"),
    ("ceilometer", "event_pipeline.yaml"),
    #("ceilometer", "policy.json"),
])
def test_main_services_files(host, service, conf_file):
    _file = host.file("/etc/" + service + "/" + conf_file)
    assert _file.exists
