# Quote of the Hour

Background colors
```
cp brand-colors.latest.txt color.txt
# Keep hex color #HHHHHH
sed -i 's/.*#\([0-9,a-f,A-F]\{6\}\).*/\1/' color.txt
# Delete the first 8 lines
sed -i 1,8d color.txt
# Remove duplicate
uniq color.txt > colors.txt
```