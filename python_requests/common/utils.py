# coding:utf-8
import yaml


def get_data_from_yaml(file):
    with open(file, 'r', encoding="utf-8") as f:
        content = yaml.load(f, Loader=yaml.FullLoader)
    return content


def set_data_to_yaml(file, content):
    with open(file, 'w+', encoding="utf-8") as f:
        yaml.dump(content, f, Dumper=yaml.Dumper)


def set_env(file, argv):
    content = get_data_from_yaml(file)
    env = "TEST"
    if argv.lower() == "live":
        env = "LIVE"
    content['env'] = env
    set_data_to_yaml(file, content)


def get_env():
    file = "../testdatas/config"
    content = get_data_from_yaml(file)
    env = "TEST"
    if content["env"] == "LIVE":
        env = "LIVE"
    return env


def get_url():
    base_url = ""
    env = get_env().lower()
    # 处理url
    url = ""
    return url
