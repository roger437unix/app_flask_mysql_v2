import os, sys

USER     = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST     = os.getenv('HOST')

if USER is not None and PASSWORD is not None and HOST is not None:
  db_config = {
    'host': HOST,
    'user': USER,
    'password': PASSWORD,
    'database': 'db_users'
  }
else:
  print(f'\n*** The enviroment variables "USER", "PASSWORD" and "HOST" are empty ***\n')
  print(f'Execute no terminal:\n')
  print(f'export USER     = "<DATABASE_USER>"')
  print(f'export PASSWORD = "<DATABASE_USER_PASSWORD>"')
  print(f'export HOST     = "<DATABASE_ADDRESS>"\n')
  sys.exit()
