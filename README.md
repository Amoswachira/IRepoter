# IRepoter [![Build Status](https://travis-ci.org/Amoswachira/IRepoter.svg?branch=ft-patch-location-comment-%23162341392)](https://travis-ci.org/Amoswachira/IRepoter) [![Coverage Status](https://coveralls.io/repos/github/Amoswachira/IRepoter/badge.svg?branch=ft-patch-location-comment-%23162341392)](https://coveralls.io/github/Amoswachira/IRepoter?branch=ft-patch-location-comment-%23162341392) [![Maintainability](https://api.codeclimate.com/v1/badges/9debc84167f58e9232c4/maintainability)](https://codeclimate.com/github/Amoswachira/IRepoter/maintainability)
Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

### MAIN FEATURES

- Users can create a red-flag record (An incident linked to corruption).
- Users can create intervention record (a call for a government agency to intervene e.g repair bad road sections, collapsed bridges, flooding e.t.c).
- Users can edit their red-flag or intervention records.
- Users can delete their red-flag or intervention records.
- Users can add geolocation (Lat Long Coordinates) to their red-flag or intervention records.
- Users can change the geolocation (Lat Long Coordinates) attached to their red-flag or intervention records.
- Admin can change the status of a record to either under investigation, rejected (in the event of a false claim) or resolved (in the event that the claim has been investigated and resolved).
- Users can add images to their red-flag or intervention records, to support their claims.
- Users can add videos to their red-flag or intervention records, to support their claims.
- The application should display a Google Map with Marker showing the red-flag or intervention location.

### Postman link
https://web.postman.co/collections/3870907-2c54498f-d063-61ef-833e-53a48ca70283?workspace=0f58c448-3ac6-4606-8c31-394ef43facc1

### Heroku Link
https://irepoterapiv1.herokuapp.com/api/v1/red-flags

## Installation and Deployment.

### Clone the repo
 > git clone https://github.com/Amoswachira/IRepoter.git

### Setup environment

#### create a virtual environment and activate it asap
>cd IRepoter
>virtualenv env

### Activate your virtualenv:

on Windows, virtualenv creates a batch file
>cd env
>\env\Scripts\activate.bat

#### Install all the dependencies using the command
> pip install - r Requirements.txt

#### How to Run the App
> ```.env
> flask run


## Endpoints to test

| Method | Endpoint                                    | Description                                    |
| ------ | ------------------------------------------- | ---------------------------------------------- |
| POST   | /api/v1/red-flags                           | Create a red-flag record.                      |
| GET    | /api/v1/red-flags                           | Fetch all red-flag records.                    |
| GET    | /api/v1/red-flags/<red-flag-id>id             | Fetch a specific red-flag record.              |
| PATCH  | /api/v1/red-flags/<red-flag-id>id/location    | Edit the location of a specific record.        |
| PATCH  | /api/v1/red-flags/<red-flag-id>id/comment     | Edit the comment of a specific record.         |
| DELETE | /api/v1/red-flags/<red-flag-id>id             | Delete a specific red flag record.             |

