import yaml
import argparse

def main(username, password, cfgfile):
    work1_cfg = open(cfgfile)
    wario_cfg = yaml.load(work1_cfg)

    print(wario_cfg)

def get_cmd_args():
    parser = argparse.ArgumentParser(description="Process github repos for COE11 class")
    parser.add_argument("--username", help="Github username")
    parser.add_argument("--password", help="Github password")
    parser.add_argument("--cfg", help="Yaml config for wario")
    args = parser.parse_args()
    return args.username, args.password, args.cfg

if __name__ == "__main__":
    username, password, cfgfile = get_cmd_args()
    main(username, password, cfgfile)