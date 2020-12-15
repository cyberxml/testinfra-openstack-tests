import pytest

@pytest.mark.parametrize("name", [
    ("openstack-swift-object"),
    ("openstack-swift-account"),
    ("openstack-swift-proxy"),
    ("openstack-swift-container"),
    ("puppet-swift.noarch"),
    ("python3-swift.noarch"),
    ("python3-swiftclient.noarch"),

])
def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed

@pytest.mark.parametrize("name,port", [
    ("swift-object-server", "6000"),
    ("swift-container-server", "6001"),
    ("swift-account-server", "6002"),
])
def test_listening_interfaces(host, name, port):
    sckt = host.socket("tcp://10.10.10.24:" + port)
    assert sckt.is_listening

@pytest.mark.parametrize("process,enabled", [
    ("openstack-swift-account-auditor", True),
    ("openstack-swift-account-reaper", True),
    ("openstack-swift-account-replicator", True),
    ("openstack-swift-account", True),
    ("openstack-swift-container-auditor", True),
    ("openstack-swift-container-replicator", True),
    ("openstack-swift-container-updater", True),
    ("openstack-swift-container", True),
    ("openstack-swift-object-auditor", True),
    ("openstack-swift-object-expirer", True),
    ("openstack-swift-object-replicator", True),
    ("openstack-swift-object-updater", True),
    ("openstack-swift-object", True),
    ("openstack-swift-proxy", True),
])
def test_services(host, process, enabled):
    svc = host.service(process)
    assert svc.is_running
    if enabled:
        assert svc.is_enabled

@pytest.mark.parametrize("srv,conf_file", [
    ("swift", "account-server.conf"),
    ("swift", "container-reconciler.conf"),
    ("swift", "container-server.conf"),
    ("swift", "object-expirer.conf"),
    ("swift", "object-server.conf"),
    ("swift", "proxy-server.conf"),
    ("swift", "swift.conf"),
])
def test_main_services_files(host, srv, conf_file):
    _file = host.file("/etc/" + srv + '/' + conf_file)
    assert _file.exists
