# Read from the file words.txt and output the word frequency list to stdout.
# Word Frequency https://leetcode.com/submissions/detail/36808885/
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | awk '{print $2" "$1}' | sort -k2 -n -r