---
title: Dark Mode project idea
description: 
published: true
date: 2023-03-02T00:00:00.000Z
tags: 
editor: markdown
dateCreated: 2022-03-02T00:00:00.000Z
---

## Classification

- **Difficulty**: *Easy*
- **Skills needed**: CSS, HTML, some graphic design, some JavaScript, and some Svelte
- **Length**: *Small (~75 hours)*

## The Problem

- Many users prefer to use apps in "dark mode", where most of the UI shows light text on dark background.

- **Mathesar currently has poor support for dark mode**.

- Some custom browser extensions may be able to display Mathesar in dark mode, but only by making their own guesses as to the best colors to use for UI elements. Beyond usage of such browser extensions, it is not possible to use Mathesar in dark mode.

## Feature Description

- Mathesar should globally adapt its colors in response to the [prefers-color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) media query.

- Mathesar should also have a color scheme switcher, allowing the user to override the browser's color scheme preference. For example:

    ![image](https://user-images.githubusercontent.com/42411/216636539-930238bb-309f-4183-889d-7cd672649c79.png)

    ![image](https://user-images.githubusercontent.com/42411/216637154-22123980-b89e-4f7e-ab43-b5b4f08d7649.png)

- The color scheme switcher should synchronize its state with `localStorage` so that the user's color scheme preference is persisted after page reloads.

## Design Work

- This project also includes the work of choosing the colors to use for each UI element in dark mode.
- We'll need to figure out the appearance and behavior of the theme switcher.

## Tasks

1. Build a theme-switcher component
1. Incorporate the theme switcher into the app so that it toggles a class on the `body` element.
1. Get the theme-switcher to synchronize its state with localStorage 
1. Get one color within the UI to change based the `prefers-color-scheme` media query and the body class.
1. Methodically work your way through all the colors defined for the app, choosing appropriate values for those colors in dark mode.
1. Refactor color values out of CSS declarations and into CSS variables as needed.

## Expected Outcome

Users can easily use Mathesar in dark mode.

## Application Tips

- Demonstrate proficiency with the required skills
- Demonstrate a good sense of visual design and taste

## Out of scope

- Any additional themes, beyond "Light" and "Dark"
- Custom themes

## Mentors

- **Primary Mentor**: Sean Colsen
- **Secondary Mentor(s)**: Pavish Kumar Ramani Gopal

