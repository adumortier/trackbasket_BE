  
<p align="center">
  <img width="500" height="300" src="https://user-images.githubusercontent.com/55954962/83821753-706c4f00-a68c-11ea-9c1b-2a2d24eddd94.jpg">
</p>

<br />
<p align="center">
  <a href="https://trackbasket.herokuapp.com/">
  </a>
  
  <h1 align="center">Track Basket</h1> <br><br>
  
TrackBasket is a grocery-delivery app for volunteer shoppers who serve people whose mobility is limited during the pandemic. The purpose of the app is to allow at-risk consumers to create shopping lists by searching items available at a nearby store and to make these lists available to volunteers who can sort them and select the one they can fulfill.
<p align="center">
<a href="http://g.recordit.co/Fq4vHJEapy.gif"><img src="http://g.recordit.co/Fq4vHJEapy.gif" width="500" height="500"/></a>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
  * [Schema](#schema)
* [Getting Started](#getting-started)
  * [Installation](#installation)
  * [Testing](#testing)

<!-- ABOUT THE PROJECT -->
## About The Project

As the thread of COVID-19 rises, it's not safe for some people to leave their house, even to buy essentials. Trackbasket connects this at-risk population with volunteers who shop for and deliver customized grocery lists.

### Built With

Back end:
* Frameworks: Flask
* Language: Python 3.7
* Deployment: Heroku
* Database: PostgreSQL
* Testing: UnitTest, Coverage
* Dependency Management: Poetry
* Project Management: Github Project Board
* External API: Kroger

Front end:

* React Native
* React Navigation
* React Hooks/Context API
* Expo
* React Native Testing Library
* Jest

### Schema

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo
```sh
git clone https://github.com/track-basket/trackbasket_BE
```
2. Install Python

3. Install Poetry 

4. Run the app locally
```sh
python trackbasket_be/app.py
```
5. Your credentials should be stored locally

### Testing

Run the test suite from the `trackbasket_be` directory:

```sh
python -m unittest discover
```

## Back End Endpoints 

### Volunteer Endpoint

Retrieve a volunteer's profile information:
```sh
GET https://trackbasket.herokuapp.com/volunteer/<volunteer_id>
```
Create a new volunteer:

```sh
POST https://trackbasket.herokuapp.com/volunteer/<volunteer_id>

```

### AtRiskUser Endpoints

Retrieve an at risk user's profile information:
```sh
GET https://trackbasket.herokuapp.com/atriskuser/<at_risk_user_id>
```
Create a new at risk user:
```sh
POST https://trackbasket.herokuapp.com/atriskuser/<at_risk_user_id>
```
Update an at risk user:
```sh
PATCH https://trackbasket.herokuapp.com/atriskuser/<at_risk_user_id>
```
Delete an at risk user:
```sh
DELETE https://trackbasket.herokuapp.com/atriskuser/<at_risk_user_id>
```

### ShoppingList Endpoints

Retrieve a shopping list's information:
```sh
GET https://trackbasket.herokuapp.com/shoppinglist/<at_risk_user_id>
```
Create a new shopping list:
```sh
POST https://trackbasket.herokuapp.com/shoppinglist/<at_risk_user_id>
```
Update a shopping list:
```sh
PATCH https://trackbasket.herokuapp.com/shoppinglist/<at_risk_user_id>
```
Delete an at risk user:
```sh
DELETE https://trackbasket.herokuapp.com/shoppinglist/<at_risk_user_id>
```

### List of ShoppingLists Endpoint

Retrieve all shopping lists' and its information:
```sh
GET https://trackbasket.herokuapp.com/listshoppinglists
```
<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* Alex Robinson (PM) - [GitHub](https://github.com/scottalexandra)<br>
* Eric Weissman (PM) - [GitHub](https://github.com/ericweissman)<br>

## Developer GitHub Profiles

* Alexis Dumortier (Backend) - [GitHub](https://github.com/adumortier)<br>
* Maria Ronauli (Backend) - [GitHub](https://github.com/mronauli)<br>

* Ed Stoner (Frontend) - [GitHub](https://github.com/edlsto)<br>
* Cody Smith (Frontend) - [GitHub](https://github.com/monstaro)<br>

Deployed Application on Heroku: [TrackBasket](https://trackbasket.herokuapp.com/)