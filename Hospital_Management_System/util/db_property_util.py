def get_property_string(file_path):
    props = {}
    with open(file_path, 'r') as f:
        for line in f:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                props[key] = value

    conn_str = f"mysql+pymysql://{props['username']}:{props['password']}@{props['host']}:{props['port']}/{props['database']}"
    return conn_str
