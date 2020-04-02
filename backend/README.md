# run command on Heroku
heroku run -a xiaomanager bash
heroku run -a xiaomanager "cd backend && ./manager shell"

# setup postgresql
1. brew services start postgresql  
2. brew services stop  postgresql  
3. To create database  
   3.1 psql postgres  
   3.2 "CREATE ROLE postgres WITH LOGIN;"  
   3.3 "ALTER ROLE postgres CREATEDB;"  
   3.4 psql -c 'create database test_db;" -U posgres  

