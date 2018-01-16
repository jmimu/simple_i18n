#!/usr/bin/python
import re
import sys

if len(sys.argv)<3 :
  print "Usage :\n./prep_translation.py file.js la\nWhere 'la' is the language."
  exit(0)

filename=sys.argv[1]

datafile = open(filename)

language=sys.argv[2]
existing_keys={}

inside_translation=False
#get all existing keys
for line in datafile:
  if re.compile('translation_'+language+'={').search(line):
    #print "hop!"
    inside_translation=True
    continue
  if inside_translation and re.compile('}').search(line):
    #print "bof."
    inside_translation=False
    break
  if inside_translation :
    if (re.match(' *"(.*)": *"(.*)"', line)) :
      key=re.match(' *"(.*)": *"(.*)"', line).group(1)
      val=re.match(' *"(.*)": *"(.*)"', line).group(2)
      #print '  key found: "'+key+'": "'+val+'",'
      existing_keys[key]=val

#print "existing_keys: "
#print existing_keys
#get new keys
datafile.seek(0)
all_keys=[]
for line in datafile:
  if (re.match('.*_\( *["]([^"]+)["] *\).*', line)) :
    all_keys+=re.findall('_\( *["]([^"]+)["] *\)', line)
  if (re.match('.*_\( *[\']([^\']+)[\'] *\).*', line)) :
    all_keys+=re.findall('_\( *[\']([^\']+)[\'] *\)', line)
all_keys_unique=[]
[all_keys_unique.append(x) for x in all_keys if x not in all_keys_unique]

#print len(all_keys),len(all_keys_unique)
#print all_keys

#write transltation mixing existing and new keys
print "var translation_"+language+"={"
for key in all_keys_unique :
  if (key in existing_keys) :
    print '  "'+key+'": "'+existing_keys[key]+'",'
  else :
    print '  "'+key+'": "~'+key+'~",'
print "}"

datafile.close()
