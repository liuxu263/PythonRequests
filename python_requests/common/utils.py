import yaml
import os


def load_yaml(file):
    with open(file, 'r', encoding="utf-8") as f:
        content = yaml.load(f, Loader=yaml.FullLoader)
    return content


def set_yaml(file, content):
    with open(file, 'w', encoding="utf-8") as f:
        yaml.dump(content, f, Dumper=yaml.Dumper)


def set_env(file, argv):
    content = load_yaml(file)
    env = "TEST"
    if argv[0].lower() == "live":
        env = "LIVE"
    content['env'] = env
    set_yaml(file, content)
    os.system("pwd")


def get_env(argv):
    env = "TEST"
    if argv[0] == "LIVE":
        env = "LIVE"
    return env


def get_url():
    pass


if __name__ == '__main__':
    print(load_yaml("/Users/xuliu/workspace/Python_Requests/Python_Requests/common/config"))
