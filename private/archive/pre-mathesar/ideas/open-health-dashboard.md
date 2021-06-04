---
title: Open Health Dashboard
description: 
published: true
date: 2021-04-19T21:13:49.016Z
tags: 
editor: markdown
dateCreated: 2021-04-19T20:18:59.303Z
---

Related to [Decentralize the internet](../goals/decentralize-internet)

## Problem
Everyone needs to take care of their health. There is data available to people about their own health, but there aren't a lot of tools that help people see all of the data in one place and see the big picture. There are some existing solutions that focus on just aggregation (e.g. Apple Health) or on a subset of health (e.g. MyFitnessPal), but they are proprietary, and there's no way to be in control of your own health data.

## Solution
A health dashboard that can retrieve and combine data from your hospital's health records, connected fitness devices (such as trackers and scales), smartphone apps, and manual data entry.

The software should support:
- different modules for different types of health events you want to track, e.g.
  - physical activity (steps, flights climbed, walking distance, running, cycling, etc.)
  - diet (allow scanning of food and automatic calculation of nutriets)
  - exercise (allow tracking of exercises performed)
  - sleep
  - menstrual cycle
  - sexual activity
  - weight and body measurements
  - mindfulness
  - events related to specific medical conditions such as: 
    - migraines
  - modules for non-medical data that might be related to medical conditions such as:
    - weather
    - pollen
    - flu prevalence
- importing health records from your doctors/hospitals
- prescription tracking
- setting health goals and automatically tracking progress based on entered data
- providing automatic recommendations and insights based on data

### UI Mockups
Here are some very rough UI mockups to illustrate the idea behind the project.

**Homepage**: This shows recent activity, insights gained from recent activity, and all the different modules you can add or track.

![Homepage](homepage.png)

**Physical Activity**: This shows the homepage for the "physical activity" module. It shows you the different types of activity tracked there (steps, walking, cycling, etc.), the data tracked for each one (including graphs), and allows you to manage and connect different data sources for the data. It also allows you to set goals for the activity, so that you can track if you're meeting your health goals.

![Physical Activity](physical-activity.png)

## Feasability

The basic product does not have a lot of technical challenges, we'd just need to build connectors to a variety of data sources and display them. We do need to solve a few problems, though:
- We'd need to figure out a standard format and set of requirements for each module so that the community can build out modules that fits their needs and can be interoperable.
- We'd need to figure out a simple UX that doesn't overwhelm the user but provides a lot of functionality.
- We'd need to figure out a good algorithm for making recommendations for advice.
	- We need to have some way to map how different conditions or data will affect each other in order to come up with advice.
	- We might need to allow users who self-host the software to update this database of advice without actually updating the software.

### Potential Roadmap
- Start by creating a few core modules and releasing publicly. Public release should also include documentation on how to create new modules so that we can take advantage of community involvement.
- Continue to build out new modules after launch.
- Build iOS and Android apps that take data from Google Fit and Apple HealthKit and also allow users to enter data from their smartphone (also allows features like "take a photo of your meal and we'll estimate calories")

### Potential Users
- We can market to users who need the first core modules we build (e.g. if we build a migraine module, migraineurs would be a good first audience)
- Market to the "quantified self" movement

### Potential Data Sources
- [https://1up.health/](https://1up.health/)

### CCI Integrations
It's possible this could integrate with [BayesDB](http://probcomp.csail.mit.edu/software/bayesdb/):
- We could try to help people understand their health from a statistical model perspective.
- We could help people understand which modifications of their behavior would be most effective at improving their health.
- Depending on data collection, we could help practitioners give sound advice based on the health data of their patient(s).

## Sustainability
- We could offer a paid centralized version so that people wouldn't need to self-host.
- We could offer paid support for the self-hosted version.
- Partner with medical service providers to offer this to clients?

## Challenges
- We need people with medical knowledge to vet what we're doing.
- Proprietary companies may not want to part with their data (e.g. using the Fitbit API to build a similar service to their health tracking is against their terms of service)
- Offering a hosted version of this runs into lots of regulations about medical data.

### Competitors
There isn't a direct competitor here, there's no web-based software that tracks all of this, and most software that tracks subsets of health data is proprietary.

- Google Fit (smartphone app, proprietary)
- Apple Health (smartphone app, proprietary)
- Dashboards for various wearables (e.g. FitBit)
- Targeted apps for specific health needs:
  - [MyFitnessPal](https://www.myfitnesspal.com/), [Fat Secret](https://www.fatsecret.com/), etc. for calorie tracking (proprietary)
- Tracking, analysis, goal setting:
  - [Gyroscope](https://gyrosco.pe/) (proprietary)
  - [Exist](https://exist.io/) (proprietary)

See also [awesome-quantified-self](https://github.com/woop/awesome-quantified-self#applications-and-platforms) list.

## Additional Thoughts
- These folks are looking to make medical data interoperable, and would be good to talk to: https://www.openmhealth.org/
- An integration with BayesDB could prove to be an advantage that would result in our app being better than the proprietary competition.
- We should try to think of ways that the open-source, non-proprietary nature of our app would result in a better product for the user who might not care much about data security, etc.
