# Read from the file words.txt and output the word frequency list to stdout.
# Word Frequency https://leetcode.com/submissions/detail/36808885/
# Note : 
# 1. tr -s ' ' matches "one or more spaces" 
# 2. sort -k2 means sort value by second field
# 3. -r -n should be at the same level 
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | awk '{print $2" "$1}' | sort -k2 -rn