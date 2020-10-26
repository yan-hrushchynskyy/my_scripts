#---------------------------------------------------------------------------
# This script will set definited CloudWatch Alarms for all ELBs in the region 
# Requires the AWS CLI and jq and you must setup your ALARMACTION
#
# v 1.0
#
# Modified by Yan Hrushchynskyi 2020
#---------------------------------------------------------------------------

#!/usr/bin/env bash
# AWS Region
Region="needed_region"
# SNS topic
ALARMACTION='arn:aws:sns:my_topic'

# Functions

# Completed
function completed(){
	echo
	separator
	tput setaf 2; echo "Completed!"
	separator
	echo
}

# Fail
function fail(){
	tput setaf 1; echo "Failure: $*"
	exit 1
}

# separator
function separator(){
	echo "============================================================"
}

# Get list of all Classic EC2 ELBs in one region
function ListELBs(){
	ELBs=$(aws elb describe-load-balancers --region $Region --output=json 2>&1)
	if [ $? -ne 0 ]; then
		fail "$ELBs"
	else
		ParseELBs=$(echo "$ELBs" | jq '.LoadBalancerDescriptions | .[] | .LoadBalancerName' | cut -d '"' -f2 | sed '/dummy\|standby\|alpha/d')
	fi
	if [ -z "$ParseELBs" ]; then
		echo "No ELBs found in $Region."
		TotalELBs="0"
	else
		TotalELBs=$(echo "$ParseELBs" | wc -l | cut -d " " -f1)
	fi
}

function SetAlarms(){
	if [ "$TotalELBs" -gt "0" ]; then
		ELBStart=1
		for (( ELBCount=$ELBStart; ELBCount<=$TotalELBs; ELBCount++ ))
		do
			ELBName=$(echo "$ParseELBs" | nl | grep -w [^0-9][[:space:]]$ELBCount | cut -f2)
			echo
			separator
			echo "ELB Name: $ELBName"
			echo "Setting CloudWatch Alarms"
			VerifyAlarm1=$(aws cloudwatch describe-alarms --alarm-names "$ELBName - ELB Unhealthy Hosts" --output=json --region $Region 2>&1)
			AlarmName1=$(echo "$VerifyAlarm1" | jq '.MetricAlarms | .[] | .AlarmName')
			if [ -z "$AlarmName1" ]; then
				SetAlarm1=$(aws cloudwatch put-metric-alarm --alarm-name "$ELBName - ELB Unhealthy Hosts" --alarm-description "There is one or more unhealthy hosts in the LB for more than 15 min" --metric-name UnHealthyHostCount --namespace AWS/ELB --statistic Maximum --dimensions Name=LoadBalancerName,Value="$ELBName" --unit Count --period 300 --evaluation-periods 3 --threshold 1 --comparison-operator GreaterThanOrEqualToThreshold --alarm-actions $ALARMACTION --ok-actions $ALARMACTION --insufficient-data-actions $ALARMACTION --output=json --region $Region 2>&1)
				if [ $? -ne 0 ]; then
					fail "$SetAlarm1"
				fi
				echo "Alarm set: ELB Unhealthy Hosts"
			else
				echo "$AlarmName1 is alredy configured on $ELBName"
			fi
			VerifyAlarm2=$(aws cloudwatch describe-alarms --alarm-names "$ELBName - ELB High Latency" --output=json --region $Region 2>&1)
			AlarmName2=$(echo "$VerifyAlarm2" | jq '.MetricAlarms | .[] | .AlarmName')
			if [ -z "$AlarmName2" ]; then
				SetAlarm2=$(aws cloudwatch put-metric-alarm --alarm-name "$ELBName - ELB High Latency" --alarm-description "High latency is being observed for more than 5 min" --metric-name Latency --namespace AWS/ELB --statistic Average --dimensions Name=LoadBalancerName,Value="$ELBName" --unit Count --period 60 --evaluation-periods 5 --threshold 1 --comparison-operator GreaterThanOrEqualToThreshold --alarm-actions $ALARMACTION --ok-actions $ALARMACTION --insufficient-data $ALARMACTION --output=json --region $Region 2>&1)
				if [ $? -ne 0 ]; then
					fail "$SetAlarm2"
				fi
				echo "Alarm set: ELB High Latency"
			else
				echo "$AlarmName2 is alredy configured on $ELBName"
			fi
			VerifyAlarm3=$(aws cloudwatch describe-alarms --alarm-names "$ELBName - ELB High Number Backend_5XX errors" --output=json --region $Region 2>&1)
			AlarmName3=$(echo "$VerifyAlarm3" | jq '.MetricAlarms | .[] | .AlarmName')
			if [ -z "$AlarmName3" ]; then
				SetAlarm3=$(aws cloudwatch put-metric-alarm --alarm-name "$ELBName - ELB High Number Backend_5XX errors" --alarm-description "More than 100 server errors responses during the last 5 min" --metric-name HTTPCode_Backend_5XX --namespace AWS/ELB --statistic Average --dimensions Name=LoadBalancerName,Value="$ELBName" --unit Count --period 60 --evaluation-periods 5 --threshold 100 --comparison-operator GreaterThanOrEqualToThreshold --alarm-actions $ALARMACTION --ok-actions $ALARMACTION --insufficient-data $ALARMACTION --output=json --region $Region 2>&1)
				if [ $? -ne 0 ]; then
					fail "$SetAlarm3"
				fi
				echo "Alarm set: ELB High Number Backend_5XX errors"
			else
				echo "$AlarmName3 is alredy configured on $ELBName"
			fi
			VerifyAlarm4=$(aws cloudwatch describe-alarms --alarm-names "$ELBName - ELB High Number HTTP_5XX errors" --output=json --region $Region 2>&1)
			AlarmName4=$(echo "$VerifyAlarm4" | jq '.MetricAlarms | .[] | .AlarmName')
			if [ -z "$AlarmName4" ]; then
				SetAlarm4=$(aws cloudwatch put-metric-alarm --alarm-name "$ELBName - ELB High Number HTTP_5XX errors" --alarm-description "More than 100 5xx errors during the last 5 min. Either the load balancer or the registered instance is causing the error or the load balancer is unable to parse the response." --metric-name HTTPCode_ELB_5XX --namespace AWS/ELB --statistic Sum --dimensions Name=LoadBalancerName,Value="$ELBName" --unit Count --period 60 --evaluation-periods 5 --threshold 100 --comparison-operator GreaterThanOrEqualToThreshold --alarm-actions $ALARMACTION --ok-actions $ALARMACTION --insufficient-data $ALARMACTION --output=json --region $Region 2>&1)
				if [ $? -ne 0 ]; then
					fail "$SetAlarm4"
				fi
				echo "Alarm set: ELB High Number HTTP_5XX errors"
			else
				echo "$AlarmName4 is alredy configured on $ELBName"
			fi
			VerifyAlarm5=$(aws cloudwatch describe-alarms --alarm-names "$ELBName - ELB BackendConnectionErrors" --output=json --region $Region 2>&1)
			AlarmName5=$(echo "$VerifyAlarm5" | jq '.MetricAlarms | .[] | .AlarmName')
			if [ -z "$AlarmName5" ]; then
				SetAlarm5=$(aws cloudwatch put-metric-alarm --alarm-name "$ELBName - ELB BackendConnectionErrors" --alarm-description "BackendConnectionErrors are observed for the last 5 min" --metric-name BackendConnectionErrors --namespace AWS/ELB --statistic Sum --dimensions Name=LoadBalancerName,Value="$ELBName" --unit Count --period 60 --evaluation-periods 5 --threshold 1 --comparison-operator GreaterThanOrEqualToThreshold --alarm-actions $ALARMACTION --ok-actions $ALARMACTION --insufficient-data $ALARMACTION --output=json --region $Region 2>&1)
				if [ $? -ne 0 ]; then
					fail "$SetAlarm5"
				fi
				echo "Alarm set: ELB BackendConnectionErrors"
			else
				echo "$AlarmName5 is alredy configured on $ELBName"
			fi
		done
	fi
}

if [ -z "$Region" ]; then
	fail "Region is not specified"
else
	ListELBs
	if [ "$TotalELBs" -gt "0" ]; then
		SetAlarms
	fi
fi

completed