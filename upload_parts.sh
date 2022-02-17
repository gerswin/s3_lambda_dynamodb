file_parts=./ap
parts=0
for file in "file_parts"/*
do
  parts=$((parts+1))
  echo "file"
  aws s3 cp "$file" s3://yourbucketpath
  sleep 15s 
 if [[ "$parts" -gt 5 ]]; then
    parts=0
    sleep 90s
  fi
done