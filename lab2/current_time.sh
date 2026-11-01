#!/bin/bash
# Shows current time and time left until the work day ends
# Usage: current_time.sh [end_hour]   (default 18)
END_HOUR=${1:-18}
END_MIN=0

now_h=$(date +%H)
now_m=$(date +%M)
now_total=$((10#$now_h * 60 + 10#$now_m))
end_total=$((END_HOUR * 60 + END_MIN))

echo "Current time: $now_h:$now_m."
if [ $now_total -ge $end_total ]; then
    echo "Work day is already over."
else
    left=$((end_total - now_total))
    echo "Work day ends after $((left / 60)) hours and $((left % 60)) minutes."
fi
