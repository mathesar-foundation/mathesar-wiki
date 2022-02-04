---
title: Example Schema
description: This is an example table structure used in various product specs.
published: true
date: 2022-02-04T03:09:49.072Z
tags: 
editor: markdown
dateCreated: 2022-02-04T02:52:01.932Z
---

This schema is a reference to be used as an example in specs or other sections of the wiki. These tables are meant to simulate what data looks like in real databases.

## Table: `movie`
| id | title | year | language |
|-|-|-|-|
| 13 | Thelma & Louise | 1991 | English |
| 22 | Meet Joe Black | 1998 | English |
| 33 | Crouching Tiger, Hidden Dragon | 2000 | Mandarin |
| 41 | Crazy Rich Asians | 2018 | English |

## Table: `actor`
| id | name |
|-|-|
| 34 | Michelle Yeoh |
| 45 | Brad Pitt |
| 71 | Geena Davis |
| 83 | Zhang Ziyi |

## Table: `movie_actor_map`
| id | movie_id | actor_id |
|-|-|-|
| 67 | 13 | 45 |
| 68 | 22 | 45 |
| 69 | 33 | 34 | 
| 70 | 41 | 34 |
| 89 | 13 | 71 |
| 97 | 33 | 83 | 

## Table: `movie_watch`
| id | movie_id | date |
|-|-|-|
| 91 | 13 | 2021-10-13 |
| 100 | 22 | 2021-10-01 |
| 104 | 33 | 2021-09-23 | 
| 190 | 41 | 2021-08-12 |
| 203 | 13 | 2019-01-20 |
