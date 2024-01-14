from utils.executor import execute


def resolve(domain_port_map: dict[str, int]):
    execute('a2enmod proxy')
    execute('a2enmod proxy_http')
    config = ''
    for domain, port in domain_port_map.items():
        config += f'<VirtualHost *:80>\n'
        config += f'    ServerName {domain}\n'
        config += f'    ProxyPass / http://localhost:{port}/\n'
        config += f'    ProxyPassReverse / http://localhost:{port}/\n'
        config += f'</VirtualHost>\n'
        config += '\n'
    with open('/etc/apache2/sites-available/pg_proxy.conf', 'w+') as f:
        f.write(config)
        f.close()
    execute('a2ensite pg_proxy')
    execute('systemctl restart apache2')
