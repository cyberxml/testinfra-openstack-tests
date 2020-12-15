## Generated tests for compute IaaS node @Produban
## This role and tests could not be executed by themselves, must exists a previous OSP Region installed
## Then this role could be executed on OSP version described on the folder's name.
import pytest

@pytest.mark.parametrize("name", [
    #("openstack-ceilometer-central.noarch"),
    ("openstack-ceilometer-common.noarch"),
    #("openstack-ceilometer-compute.noarch"),
    ("openstack-ceilometer-ipmi.noarch"),
    ("openstack-ceilometer-notification.noarch"),
    ("openstack-ceilometer-polling.noarch"),
])
def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed

@pytest.mark.parametrize("process,enabled", [
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
    ("ceilometer", "event_definitions.yaml"),
    ("ceilometer", "gnocchi_resources.yaml"),
    ("ceilometer", "polling.yaml"),
    ("ceilometer", "rootwrap.conf"),

])
def test_main_services_files(host, service, conf_file):
    _file = host.file("/etc/" + service + "/" + conf_file)
    assert _file.exists
    assert _file.is_file
    assert _file.user == "root"
    assert _file.group == "ceilometer"
    #assert _file.mode == '0640'

@pytest.mark.parametrize("service,conf_file", [
    ("ceilometer", "ceilometer.conf"),
])
def test_main_services_deprecation_warnings(host, service, conf_file):
    _file = host.file("/etc/" + service + "/" + conf_file)
    assert not _file.contains('api_workers')
    #assert not _file.contains('notification_workers')
    assert not _file.contains('database_connection')
    assert not _file.contains('collector_workers')
    #assert not _file.contains('rpc_thread_pool_size')
    assert not _file.contains('log_format')
    #assert not _file.contains('use_syslog')
