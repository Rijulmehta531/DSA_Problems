def validate_and_sort_configuration(config_string):
    if config_string == "":
        return []
    configs = config_string.split('|')
    config_map = {}
    
    for config in configs:
        if len(config) != 14:
            return ["Invalid configuration"]
        
        ordinal_index = config[:4]
        value = config[4:]
        
        if not ordinal_index.isdigit() or ordinal_index == "0000":
            return ["Invalid configuration"]
        if not value.isalnum() or len(value) != 10:
            return ["Invalid configuration"]
        
        index = int(ordinal_index)
        if index in config_map or value in config_map.values():
            return ["Invalid configuration"]
        
        config_map[index] = value
    
    if set(range(1, len(config_map) + 1)) != set(config_map.keys()):
        return ["Invalid configuration"]
    
    return [config_map[i] for i in sorted(config_map)]

if __name__ == "__main__":
    config_string = "0001abcd123499|0002efgh5678hh|0003ijkl901282"
    output = validate_and_sort_configuration("")
    print(output)
