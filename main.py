# run func by name: python main.py func_name
import os
import subprocess
import sys
from utils.config_manger import config_instance
from services.hosts import resolve as hosts_resolve


def rebuild():
    config = config_instance()
    if config.get_service_name() == 'nginx':
        from services.nginx import resolve
    elif config.get_service_name() == 'apache':
        from services.apache import resolve
    else:
        raise Exception('Invalid service name')
    resolve(config.get_domain_port_map())
    hosts_resolve(config.get_domain_port_map())
    print('Rebuild successfully.')


def append():
    port = input('Please input the port number: ')
    domain = input('Please input the domain name: ')
    config = config_instance()
    config.get_domain_port_map()[domain] = int(port)
    rebuild()


def remove():
    domain = input('Please input the domain name: ')
    config = config_instance()
    config.get_domain_port_map().pop(domain)
    rebuild()


if __name__ == '__main__':
    if os.getuid() != 0:
        subprocess.call(['sudo', 'python3'] + sys.argv)
        exit(0)
    config_instance()
    if len(sys.argv) != 2:
        print('Usage: python main.py func_name')
        exit(1)
    func_name = sys.argv[1]
    if func_name not in globals():
        print('Invalid func name')
        exit(1)
    globals()[func_name]()
