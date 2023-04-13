# projectcars

## Installation

## Docker mode
**requirements:** docker and docker-compose installed  
To launch, your terminal must be in the root folder of this repository. Then issue :  
`docker-compose up --build`

## Uvicorn mode
**requirements:** python3.10 or greater installed  
First, install dependencies
`pip install -r requirements.txt`

Then, run the app:  
`uvicorn app.main:app --host 0.0.0.0 --port 80`
