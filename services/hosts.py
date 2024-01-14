from utils.array_substring_search import array_substring_search


def resolve(domain_port_map: dict[str, int]):
    current_config = ''
    with open('/etc/hosts', 'r') as f:
        current_config = f.read()
        f.close()
    current_config = current_config.split('\n')
    for domain, port in domain_port_map.items():
        existsLine = array_substring_search(current_config, f' {domain}')
        if domain not in current_config:
            current_config.append(f'127.0.0.1 {domain}\n')
        else:
            current_config[existsLine] = f'127.0.0.1 {domain}\n'
    with open('/etc/hosts', 'w') as f:
        f.write('\n'.join(current_config))
        f.close()

