import logging
import os

import yaml
cur_dir = os.path.dirname(__file__)
yaml_dir = os.path.join(cur_dir, '..', 'testdata')


def ReadYaml(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = yaml.load(stream=file, Loader=yaml.FullLoader)
        return data


def PathCfg(file_name='app_cfg.yaml'):
    cfg_path = os.path.join(yaml_dir, file_name)
    logging.info(f'当前数据配置路径为{cfg_path}')
    return cfg_path


if __name__ == '__main__':
    yaml_path = PathCfg()
    data = ReadYaml(yaml_path)
    print(type(data), data)
    print(yaml_path)
