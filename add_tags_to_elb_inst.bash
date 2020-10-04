#!/usr/bin/env bash

ELB=$(aws elb describe-load-balancers --load-balancer-name ConcurrencyProxy-Internal --output=json 2>&1)
ParseELB=$(echo "$ELB" | jq '.LoadBalancerDescriptions[].Instances[].InstanceId' | cut -d \" -f2)
TotalINST=$(echo "$ParseELB" | wc -l | cut -d " " -f1)
if [ "$TotalINST" -gt "0" ]; then
 INSTStart=1
 for (( INSTCount=$INSTStart; INSTCount<=$TotalINST; INSTCount++ ))
 do
  INSTName=$(echo "$ParseELB" | nl | grep -w [^0-9][[:space:]]$INSTCount | cut -f2)
  aws ec2 create-tags --resources $INSTName --tags Key=ELBList,Value=ConcurrencyProxy-Internal
 done
fi