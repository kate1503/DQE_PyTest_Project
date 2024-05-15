DRIVER_NAME = 'SQL Server'
SERVER_HOST = 'localhost'
PORT = '53350'
DATABASE = 'AdventureWorks2012'
User_ID = 'abc'
PASS = '1111'

CONNECTION_ROW = f'mssql+pymssql://{User_ID}:{PASS}@{SERVER_HOST}:{PORT}/{DATABASE}'
