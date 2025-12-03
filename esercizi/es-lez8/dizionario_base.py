config: dict[str, str ] = {

    "host": "192.168.1.1",
    "port": 8080,
    "ssl": True,
    "timeout": 30
}
config["port"] = 443
config["protocol1"] = "https"

print(f"host: {config['host']}")
print(config)