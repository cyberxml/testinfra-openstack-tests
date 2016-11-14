## Generated tests for compute IaaS node @Produban
## This role and tests could not be executed by themselves, must exists a previous OSP Region installed
## Then this role could be executed on OSP version described on the folder's name.
import pytest

@pytest.mark.parametrize("name,version", [
    ("openstack-ceilometer-common"),
    ("openstack-ceilometer-compute"),
    ("openstack-utils"),
    ("openstack-selinux"),
    ("openstack-utils"),
])
def test_packages(Package, name):
    assert Package(name).is_installed

@pytest.mark.parametrize("process,enabled", [
    ("openstack-ceilometer-compute", True),
])
def test_services(Service, process, enabled):
    service = Service(process)
    assert service.is_running
    if enabled:
        assert service.is_enabled

@pytest.mark.parametrize("service,conf_file", [
    ("ceilometer", "ceilometer.conf"),
    ("ceilometer", "pipeline.yaml"),
    ("ceilometer", "event_pipeline.yaml"),
    ("ceilometer", "policy.json"),
])
def test_main_services_files(File, service, conf_file):
    _file = File("/etc/" + service + "/" + conf_file)
    assert _file.exists
    assert _file.is_file
    assert _file.user == "root"
    assert _file.group == "root"
    assert _file.mode == '0644'

@pytest.mark.parametrize("service,conf_file", [
    ("ceilometer", "ceilometer.conf"),
])
def test_main_services_deprecation_warnings(File, service, conf_file):
    _file = File("/etc/" + service + "/" + conf_file)
    assert not _file.contains('api_workers')
    assert not _file.contains('notification_workers')
    assert not _file.contains('database_connection')
    assert not _file.contains('collector_workers')
    assert not _file.contains('rpc_thread_pool_size')
    assert not _file.contains('log_format')
    assert not _file.contains('use_syslog')
