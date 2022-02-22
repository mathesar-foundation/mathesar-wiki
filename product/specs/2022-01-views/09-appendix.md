---
title: 08. Appendix
description: 
published: true
date: 2022-02-22T00:10:06.955Z
tags: 
editor: markdown
dateCreated: 2022-02-20T18:31:12.526Z
---

# Appendix A: Movie Tables & Views

These tables and views are used to illustrate concepts in other parts of this spec.

## Tables
### Movie
| ID | Title | Release Year | Primary Language |
|-|-|-|-|
| 13 | Thelma & Louise | 1991 | English |
| 22 | Meet Joe Black | 1998 | English |
| 33 | Crouching Tiger, Hidden Dragon | 2000 | Mandarin |
| 41 | Crazy Rich Asians | 2018 | English |

### Person
| ID | Name | Role |
|-|-|-|
| 34 | Michelle Yeoh | Actor |
| 45 | Brad Pitt | Actor |
| 71 | Geena Davis | Actor |
| 83 | Zhang Ziyi | Actor |
| 84 | Ang Lee | Director |

### Movie Person Map
| ID | Movie ID | Person ID |
|-|-|-|
| 67 | 13 | 45 |
| 68 | 22 | 45 |
| 69 | 33 | 34 | 
| 70 | 41 | 34 |
| 89 | 13 | 71 |
| 97 | 33 | 83 | 
| 99 | 33 | 84 |

## Views
### Movie Actors
| Title | Release Year | Primary Language | Actors |
|-|-|-|-|
| Thelma & Louise | 1991 | English | Brad Pitt, Geena Davis |
| Meet Joe Black | 1998 | English | Brad Pitt |
| Crouching Tiger, Hidden Dragon | 2000 | Mandarin | Michelle Yeoh, Zhang Ziyi |
| Crazy Rich Asians | 2018 | English | Michelle Yeoh |

This view is defined as follows:
- `Title`, `Release Year`, `Primary Language` are directly from **Movie**
- `Actors` is a List aggregation formula applied to **Person**'s `Name` with a filter applied so that only **Person** records with `Role = "Actor"` will show up.
