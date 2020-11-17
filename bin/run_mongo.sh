#!/bin/sh

#start mongo
mongod --bind_ip 0.0.0.0 --auth &
MONGO_ID=$!

#wait for mongo to start
./setup/wait_for.sh 127.0.0.1:27017

#admin user vars
ADMIN_USER="${MONGO_ADMIN_USER:-admin}"
ADMIN_PASSWORD="${MONGO_ADMIN_PASSWORD:-password}"

#db user vars
DB_USER="${MONGO_USER:-admin}"
DB_PASSWORD="${MONGO_PASSWORD:-password}"
DB="${MONGO_DB:-tonydb}"

#create admin user
cat > /setup/create_admin_user.js << EOF

db.createUser({ user: "$ADMIN_USER", pwd: "$ADMIN_PASSWORD", roles: [{ role: "userAdminAnyDatabase", db: "admin" }] })
EOF
mongo admin /setup/create_admin_user.js
rm /setup/create_admin_user.js

#create db user
cat > /setup/create_user.js << EOF

db.createUser({ user: "$DB_USER", pwd: "$DB_PASSWORD", roles: [{ role: "dbOwner", db: "$DB" }] })
EOF
mongo $DB /setup/create_user.js -u$ADMIN_USER -p$ADMIN_PASSWORD --authenticationDatabase "admin"
rm /setup/create_user.js


#create test db user
#cat > /setup/create_test_user.js << EOF
#
#db.createUser({ user: "test", pwd: "test", roles: [{ role: "dbOwner", db: "test" }] })
#EOF
#mongo test /setup/create_test_user.js -u$ADMIN_USER -p$ADMIN_PASSWORD --authenticationDatabase "admin"
#rm /setup/create_test_user.js
# rejoin mongo
wait $MONGO_ID
