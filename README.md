# Phase 3 Lecture 5: Putting It All Together

## Objectives

By the end of today's lecture, you will be able to mock up a many-to-many relationship in OOP.

## Lesson Plan

0. Run `pipenv install` to install the dependencies and `pipenv shell` to enter the virtual environment.
1. Add properties brand and type to Makeup class.
    - Brand must be a string.
    - Type must be a string.
2. Add properties name and age to People class.
    - Name must be a string that cannot be changed after initially being set.
    - Age must be an integer greater than 12.
3. Add properties makeup item, person, and date to Purchase class.
    - Makeup item must be an instance of Makeup class.
    - Person must be an instance of People class.
    - Date must be a string.
4. Keep track of the many-to-many relationship between Makeup and People classes, using Purchase as the SSOT.
5. Add `get_most_popular_brand` to Purchase class to return most common makeup brand.
    - What is necessary to keep track of all purchase instances?

## Looking Ahead

From here on out, we will review OOP in Python.