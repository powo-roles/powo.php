import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    php = host.ansible("stat", "path=/usr/bin/php")
    assert php['stat']['exists'] is True
    assert php['stat']['xusr'] is True
