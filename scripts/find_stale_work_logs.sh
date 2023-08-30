#!/usr/bin/env bash

# This script prints the date of the most recent work log for each team member,
# sorted by the oldest date first. It helps the team manager identify team
# members who need to update their work logs.
#
# This is quick and dirty. Please feel free to improve!

dir="`dirname "$(dirname "$0")"`/docs/team/worklogs"
date_pattern='\d\d\d\d-\d\d-\d\d'

for file in "$dir"/*.md; do
  date=`grep -e '^##' $file | grep -Po $date_pattern | sort | uniq | tail -n 1`
  name=`echo $file | grep -Po '(\w+)(?=\.md$)'`
  echo $date $name
done | sort
