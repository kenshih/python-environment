# https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
import boto3
import pprint
# https://pypi.org/project/toml/
import toml
# https://realpython.com/command-line-interfaces-python-argparse/#:~:text=The%20command%20line%20interface%20(also,currently%20the%20Python%20argparse%20library.
import argparse

def read_cfg(rel_path):
  text_file = open(rel_path)
  data = text_file.read()
  text_file.close()
  return toml.loads(data)

def env_file_path():
  parser = argparse.ArgumentParser()
  parser.add_argument('--envfile', action='store', type=str, required=True)
  args = parser.parse_args()
  return args.envfile

fpath = env_file_path()
cfg = read_cfg(fpath)
rds = boto3.client('rds')
dev1 = rds.describe_db_clusters(DBClusterIdentifier=cfg["db_cluster_id"])
pprint.pp(dev1)