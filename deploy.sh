#!/bin/bash

cp www/team.md 2019/team.md

cd 2019
./deploy.sh
cd ..

cd www
./deploy.sh
cd ..

cd beta
./deploy.sh
cd ..

