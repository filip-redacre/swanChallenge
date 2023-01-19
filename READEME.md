`swanChallenge` contains a Flask application that meets the below requirements:

- Allows the user to upload a Tech Pack, which is used by fashion brands to share garment measurements for production
- Parses the tech pack, derive its schema
- Allows users to perform basic queries on that data
- It has a REST based API

**Note**: Only garment measurements which map to body measurements are stored and accepted in the initial version of the product.

## Requirements
- [`Python 3.7+ and Pip`](https://www.python.org/)
- `make`
- A **localhost** [PostgreSQL](https://www.postgresql.org/) database on port **5433**, with a table **swan**, a user: **swan-user** and password: **Swan2023!**


## How to start

Clone this repository and change it later by own. Project is ready to run (with some requirements). You need to clone and run:

```sh
$ git clone git@github.com:xen/flask-project-template.git .
$ make setup
$ make run
```

Open `http://localhost:5000/` to see make sure the service is running, you will see a Hello World message.

- `POST` contents of `sample_tech_pack.json` to `http://localhost:5000/tech_pack`
- You can now view all products by doing a `GET` `http://localhost:5000/product/all`
- If you want to filter entries, please use the following query parameters on `http://localhost:5000/product`:
```
name
division
category
season
year
price
```

## Project structure

As it is a fairly small project at the moment, the file structure is relatively flat, with the key files displayed below: 

    ├── models
        ├── manufacturer.py
        ├── product.py
        ├── sizing.py
        ├── user.py
    ├── api.py
    ├── app.py
    ├── config_module.py
    ├── Makefile
    ├── READEME.md
    ├── requirements.txt
    ├── sample_tech_pack.json
    

## Configuration

Most application configuration is present in the `./config_module.py` in the form of a Python class.
This allows the user to quickly change the application environment from dev to production (e.g. `DevelopmentConfig` -> `ProductionConfig`) 
Accomplished by updating which config is used in `app.py`:
```
cfg = import_string("config_module.DevelopmentConfig")()
```

## To be done in the future
1. Use load balancer such as **NGINX** to handle multiple requests in parallel
2. **Dockerise** this application
3. Deploy to a cloud service such as **AWS** (Elastic Beanstalk)
4. Build unit and integration **tests**
5. Integrate a **linter** for Python (Flask) or JS (React) through CI/CD pipelines
6. **Document API** using Swagger and Open API 3+
7. **API Versioning** can be done in many ways, but the most practical one for a project like this could be passing it in as query parameters (unless referencing the latest API version)
8. Use a **logging** library for debugging any issues in the future (Flask Logger)
9. Authentication, authorisation and application **security** required
10. Normalising the DB to **3NF** aad implement tighter contains on user uploaded data 
11. Add **tolerances table** with a 1 to 1 mapping to the sizing table
12. **Terminology mapping table** for easier parsing of measurements for each manufacturer
13. **Investigate**: Some measurements such as front and back raise may not be interchangeable, depending on the clothing item 
14. Tighter **form validation**, no duplicate products allowed, etc
15. Robust **error handling** to the added for the API 
16. **Database migration** functionality may be required down the line