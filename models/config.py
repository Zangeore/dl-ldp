import json
from typing import Any

from meta.singleton import Singleton


class Config(metaclass=Singleton):
    __service_name: str | None = None
    __domain_port_map: dict[str, int] | None = None

    @classmethod
    def get_service_name(cls) -> str:
        return cls.__service_name

    @classmethod
    def get_domain_port_map(cls) -> dict[str, int]:
        return cls.__domain_port_map

    @classmethod
    def set_service_name(cls, service_name: str) -> None:
        cls.__service_name = service_name

    @classmethod
    def set_domain_port_map(cls, domain_port_map: dict[str, int]) -> None:
        cls.__domain_port_map = domain_port_map

    @classmethod
    def to_json(cls) -> str:
        return json.dumps({
            'service_name': cls.__service_name,
            'domain_port_map': cls.__domain_port_map
        }, indent=4)

    @classmethod
    def from_json(cls, json_str: str) -> Any:
        data = json.loads(json_str)
        cls.__service_name = data['service_name']
        cls.__domain_port_map = data['domain_port_map']
        return cls

    def __del__(self):
        from utils.config_manger import update_config
        update_config()
