# della

Della is a Django app for managing Secret Santa/Gift Exchange. It is written for small communities where participants are in the range of 200-250 but not more.

## Features

Della has very limited set of features, however, if you need some extra feature then feel free to ask me and I _might_ consider adding it.

- User signup (with invite code)
- Messaging and secret/sneaky messaging (with email notifications)
- Gallery
- Admin features - Drawing names, Sending mass emails

## System Requirements

- Python 3.5
- PostgreSQL (or [MySQL](more.md#using-mysql))
- nginx
- supervisord

### Other requirements

Della uses [Sparkpost](https://www.sparkpost.com/) to send emails. So you need Sparkpost API Key and also an email address which can be used to send emails with Sparkpost. 

While signing up, every participant needs an invite code, which can be set to any string by admin.

These settings are to be set in `della/settings/secret.py` as `SPARKPOST_API_KEY`, `SENDER_EMAIL` and `INVITE_CODE`.

## Deployment

1. Clone the repo and rename/copy `della/settings/sample_secret.py` to `della/settings/secret.py` and set the variables appropriately.

2. Install the requirements 

        pip3 install -r requirements.txt

3. Setup ngnix (use `configs/nginx`)

4. Setup uWSGI (use `configs/uwsgi.conf`)

5. Setup supervisord (use `configs/supervisor.conf`)

Once everything is setup, CD into della directory and run following:

    pip3 install -r requirements.txt
    python3 manage.py migrate --settings=della.settings.production
    python3 manage.py collectstatic --settings=della.settings.production --noinput
    python3 manage.py createsuperuser --settings=della.settings.production
    python3 manage.py makemigrations background_task --settings=della.settings.production
    python3 manage.py migrate --settings=della.settings.production
    systemctl start della.uwsgi.service
    supervisorctl start della_background_tasks

## To Do

- Add tests
- Mark/confirm gifts received (or not)
- Add commenting system for Gallery
- Allow multiple exchanges
- Ability to set preference questionnaire for exchanges