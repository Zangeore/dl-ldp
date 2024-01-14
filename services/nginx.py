from utils.executor import execute


def resolve(domain_port_map: dict[str, int]):
    config = ''
    for domain, port in domain_port_map.items():
        config += f'   server {{\n'
        config += f'       listen 80;\n'
        config += f'       server_name {domain};\n'
        config += f'       location / {{\n'
        config += f'           proxy_pass http://localhost:{port};\n'
        config += f'           proxy_set_header Host $host;\n'
        config += f'           proxy_set_header X-Real-IP $remote_addr;\n'
        config += f'           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;\n'
        config += f'           proxy_set_header X-Forwarded-Proto $scheme;\n'
        config += f'       }}\n'
        config += f'   }}\n'
        config += f'\n'
    with open('/etc/nginx/sites-available/pd_proxy.conf', 'w+') as f:
        f.write(config)
        f.close()
    execute('ln -s /etc/nginx/sites-available/pd_proxy.conf /etc/nginx/sites-enabled/pd_proxy.conf')
    execute('systemctl restart nginx')
