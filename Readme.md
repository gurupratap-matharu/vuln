
<h1 align="center">Vuln</h1>
<h5 align="center">Analyses vulnerabilities in your project</h5>

<img src="https://github.com/gurupratap-matharu/vuln/blob/master/staticfiles/img/hero.jpg" alt="drawing" width="1920"/>

## LIVE

<https://scan-vulnerability.herokuapp.com/>

## Motivation 🎯

- Finding vulnerabilites in legacy code
- Deployment with docker on heroku
- Working with tools that are free for open source
- Working with machine learning and data science tools
- Trainig models on the fly and getting critical predictions

## Features ✨

- Logs Requests and responses using logging module
- real time model training, evaluation and prediction
- Possiblity to connect with Stripe payments to creates a payment upon POST
- Versioning of api possible see `/api/v1/`
- Fast response time
- Easily customizable with Login | Logout | reset password features and rest-token authentication
- Make file for faster setup and reusability

## Development setup 🛠

Steps to locally setup development after cloning the project.

```bash
docker-compose up -d --build
```

```bash
make build
```

Make sure you rename .env.example to .env and declare the environment variables in root folder for docker to pickup!

## Licence

MIT
