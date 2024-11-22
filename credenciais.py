import os, sys

USER = os.getenv('USER')
PASS = os.getenv('PASS')
HOST = os.getenv('HOST')

if USER is not None and PASS is not None and HOST is not None:
  db_config = {
    'host': HOST,
    'user': USER,
    'password': PASS,
    'database': 'db_users'
  }
else:
  print(f'\n*** The enviroment variables "USER", "PASS" and "HOST" are empty ***\n')
  print(f'Execute no terminal:\n')
  print(f'export USER="<DATABASE_USER>"')
  print(f'export PASS="<DATABASE_USER_PASSWORD>"')
  print(f'export HOST="<DATABASE_ADDRESS>"\n')
  sys.exit()  
