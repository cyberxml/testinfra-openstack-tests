import pytest

@pytest.mark.parametrize("name", [
    ("openstack-swift-object"),
    ("python-swift"),
    ("openstack-swift-account"),
    ("openstack-swift-proxy"),
    ("openstack-swift-container"),
    ("python2-swiftclient")
])
def test_packages(Package, name):
    assert Package(name).is_installed

@pytest.mark.parametrize("name,port", [
    ("swift-container-server", "6001"),
    ("swift-object-server", "6200"),
    ("swift-proxy-server", "8080"),
    ("swift-object-server", "6000"),
])
def test_listening_interfaces(Socket, name, port):
    socket = Socket("tcp://" + port)
    assert socket.is_listening

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
def test_services(Service, process, enabled):
    service = Service(process)
    assert service.is_running
    if enabled:
        assert service.is_enabled

@pytest.mark.parametrize("conf_file", [
    ("swift", "account-server.conf"),
    ("swift", "container-reconciler.conf"),
    ("swift", "container-server.conf"),
    ("swift", "object-expirer.conf"),
    ("swift", "object-server.conf"),
    ("swift", "proxy-server.conf"),
    ("swift", "swift.conf"),
])
def test_main_services_files(File, conf_file):
    _file = File("/etc/" + conf_file)
    assert _file.exists
