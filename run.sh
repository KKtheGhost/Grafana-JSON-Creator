source function.sh
export -f process_log local_path
echo "服务器输入/具体项目输入 功能后续开发，暂时仍需修改上级文件夹内文件。当前版本支持时间输入查询."
read -p "需要查询日志的时间为(format YYYMMDD):" startdate
read -p "需要查询日志起始时间(24H制,format YYYYMMDD):" starthour
read -p "需要查询日志结束时间(大于起始时间,format YYYYMMDD):" endhour
for logname in $(<../log.txt);do
    if [[ $1 == "go" ]];then
       list_all_logs $logname $startdate $starthour $endhour| xargs -n 1 -P 4 bash -c 'process_log "$@"' _
    else 
       list_all_logs $logname $startdate $starthour $endhour
    fi
done
