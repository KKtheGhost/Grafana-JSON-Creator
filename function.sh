zone_list() {
    cat ./zones
    }
date_range () {
  FROM=$1
  TO=$(date -d "$1  1 days ago "  "+%Y%m%d")
  MATCH=$(echo $2 | sed 's/,/ /g')
  n=0
  DAY=$FROM
  while [[ $TO -gt $DAY ]]; do
    DAY=$(date -d "${FROM} + ${n} day" +%Y%m%d)
    WEEK_DAY=$(date -d $DAY +%u)
    if [[ $(echo "${MATCH}" | wc -w) -gt 0 ]];then
      for mw in ${MATCH};do
	if [ "x${mw}" == "x${WEEK_DAY}" ];then
	  echo $DAY
	fi
      done
    fi
    n=$(expr $n + 1)
  done
}


list_all_logs () {
  logname=$1
  startdate=$2
  starthour=$3
  endhour=$4
  LOG_TEMPLATE=s3://rogame-sea-vault/log/sea/FIELD_ZONE/FIELD_PROGRESS.log.FIELD_DATE-FIELD_HOUR.gz
  ZONES=$(zone_list)
  PROGRESSES=$(bash -c "echo $logname")
  DATES=$(date_range $startdate 4)
  HOURS=$(bash -c "echo {${starthour}..${endhour}}")
  for z in $ZONES;do
    for p in $PROGRESSES;do
        for d in $DATES;do
	        for h in $HOURS;do
	            LOG_PATH=$(echo $LOG_TEMPLATE | sed "s+FIELD_ZONE+${z}+g" | sed "s+FIELD_PROGRESS+${p}+g" | sed "s+FIELD_DATE+${d}+g" | sed "s+FIELD_HOUR+${h}+g" )
	            echo $LOG_PATH
	        done
        done
    done
  done
}


local_path () {
  LOCAL_ROOT=/xdata/rogame-logs/
  remote=$1
  echo $remote | sed "s+^s3://rogame-sea-vault/log/+${LOCAL_ROOT}+g"
}

process_log () {
  remote=$1
  filter=$2
  content=$3
  locPath=$(local_path $remote)
  outName=$(echo $locPath | sed 's+\.gz$++g')
  mkdir -p $(dirname $outName)
  if [ "$filter" == 'y' ];then
    aws s3 cp $remote - | gunzip | grep  $content > $outName
  else
    aws s3 cp $remote  ${outName}.gz
  fi
}
