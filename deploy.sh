#!/bin/bash

cp www/team.md 2019/team.md
cp www/gdpr.md 2019/gdpr.md
cp www/impressum.md 2019/impressum.md

cd 2019
./deploy.sh
cd ..

cd www
./deploy.sh
cd ..


