#!/bin/bash

#Get servers list
set -f
ssh ec2-user@$DEPLOY_SERVER "sudo yum install -y git &&\
                             sudo yum install -y docker &&\
                             sudo service docker start  &&\
                             sudo usermod -a -G docker ec2-user &&\
                             cd app/2020_tp_correction &&\
                             git fetch &&\
                             git checkout docker &&\
                             git pull &&\
                             docker build -t yotta .
                             docker run -d yotta
                             "

