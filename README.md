# IRepoter [![Build Status](https://travis-ci.org/Amoswachira/IRepoter.svg?branch=ft-patch-location-comment-%23162341392)](https://travis-ci.org/Amoswachira/IRepoter) [![Coverage Status](https://coveralls.io/repos/github/Amoswachira/IRepoter/badge.svg?branch=ft-patch-location-comment-%23162341392)](https://coveralls.io/github/Amoswachira/IRepoter?branch=ft-patch-location-comment-%23162341392)
Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention


## Endpoints to test

| Method | Endpoint                                    | Description                                    |
| ------ | ------------------------------------------- | ---------------------------------------------- |
| POST   | /api/v1/red-flags                           | Create a red-flag record.                      |
| GET    | /api/v1/red-flags                           | Fetch all red-flag records.                    |
| GET    | /api/v1/red-flags/<red-flag-id>id             | Fetch a specific red-flag record.              |
| PATCH  | /api/v1/red-flags/<red-flag-id>id/location    | Edit the location of a specific record.        |
| PATCH  | /api/v1/red-flags/<red-flag-id>id/comment     | Edit the comment of a specific record.         |
| DELETE | /api/v1/red-flags/<red-flag-id>id             | Delete a specific red flag record.             |

