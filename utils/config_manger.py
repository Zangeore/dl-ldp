import os.path
import pathlib

from models.config import Config

__instance: Config | None = None
__config_path: str = '/etc/pd_proxy/config.json'


def config_instance() -> Config:
    global __instance
    if __instance is None:
        __instance = __load_config_from_file(__config_path)
    return __instance


def update_config() -> None:
    __save_config(config_instance(), __config_path)


def __load_config_from_file(path: str) -> Config:
    """Load the config from the file."""
    try:
        with open(path, 'r') as f:
            config = Config.from_json(f.read())
            f.close()
            return config
    except FileNotFoundError:
        return __create_default_config(path)


def __create_default_config(path: str) -> Config:
    print('Config file not found, creating a new one...')
    service_name = input('Please input the services name[apache/nginx]: ')
    if service_name not in ['apache', 'nginx']:
        raise Exception('Invalid services name')
    domain_port_map = {}
    while True:
        domain = input('Please input the domain name(empty to stop): ')
        port = input('Please input the port number(empty to stop): ')
        if domain == '' or port == '':
            break
        domain_port_map[domain] = int(port)
    config = __load_config(service_name, domain_port_map)
    __save_config(config, path)
    print('Config file created successfully.')
    return config


def __save_config(config: Config, path: str) -> None:
    """Save the config to the file."""
    pathlib.Path(os.path.dirname(path)).mkdir(exist_ok=True, parents=True)
    with open(path, 'w+') as f:
        f.write(config.to_json())
        f.close()


def __load_config(service: str, domain_port_map: dict[str, int]) -> Config:
    config = Config()
    config.set_service_name(service)
    config.set_domain_port_map(domain_port_map)
    return config
