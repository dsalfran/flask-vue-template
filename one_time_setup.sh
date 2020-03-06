#!/bin/bash

echo "Installing Vue dependencies"

cd client
npm install -d

echo "Building default App"
npm run build
cd ..

echo "Wipe README file"
echo "" > README.md

echo "Restarting version control"
rm -rf .git
git init
git add .
git commit -a -m "Initial commit"

echo "Deleting this script... Bye!"
rm one_time_setup.sh
