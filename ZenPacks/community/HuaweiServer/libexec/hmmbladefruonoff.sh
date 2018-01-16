#!/bin/bash
###########################################################################
# Author:	kingkong
# Date:		Jan 12th 2018
# Modified:
#
# 
# $1 = ip 
# $2 = zSnmpVer
# $3 = zSnmpCommunity
# $4 = zSnmpSecurityName
# $5 = zSnmpAuthType
# $6 = zSnmpAuthPassword
# $7 = zSnmpPrivType
# $8 = zSnmpPrivPassword
# $9 = intvalue bladeN
# $10 = intvalue
###########################################################################
#set -x


echo "$1" "$2" "$3" "$4" "$5" "$6" "$7" "$8" "$9" "$10"
if [ "$2" = "-v2c" ]; then	snmpset $2 $3 $1 1.3.6.1.4.1.2011.2.82.1.82.4.$9.5.0 s "${10}"
elif [ "$2" = "-v3" ]; then	snmpset $2 $4 -l authPriv $5 $6 $7 $8 $1 1.3.6.1.4.1.2011.2.82.1.82.4.$9.5.0 s "${10}"
fi