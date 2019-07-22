# Tenant project

## System Requirements

- Python 3.6
- Django 2.2.1
- PostgresSQL 10

## Dependencies

- Python 3.6
- virtualenv

### Django

    pip install -r requirements.txt

## Database Management

Setup in your `.env` file the next content with your own settings:

    DATABASE_NAME=YOUR_DATABASE_NAME
    DATABASE_USER=YOUR_DATABASE_USER
    DATABASE_PSW=YOUR_DATABASE_PSW


### Running migrations

To run migrations use the following command:

    ./manage migrate

## Tenant app

For the shared tenant apps every time you add or modify a model you need to run

    ./manage.py makemigrations

To apply a migration in your tenants schemas you need to execute

    ./manage.py migrate_schemas --shared


First at all you need to create the main tenant for your entire project, this will be link to the public_urls (PUBLIC_SCHEMA_URLCONF) that would be the landing page for your product.

    from customers.models import Client, Domain

    # create your public tenant
    tenant = Client(schema_name='public',
                    name='Novacoco SAPI de CV',
                    paid_until='2016-12-05',
                    on_trial=False)
    tenant.save()

    # Add one or more domains for the tenant
    domain = Domain()
    domain.domain = 'novacoco.local' # don't add your port or www here! on a local server you'll want to use localhost here
    domain.tenant = tenant
    domain.is_primary = True
    domain.save()

In your local this is the file you need to edit and config de redirection from a domain to localhost

    vim /etc/hosts

Add next structure 

    127.0.0.1       novacoco.local first.novacoco.local second.novacoco.local # ... your tenants

You can create your tenants using the command line using

    clone_tenant
    collectstatic_schemas
    create_tenant # Create a tenant using wizard
    create_tenant_superuser # add a super user to the tenant
    migrate
    migrate_schemas
    syncdb
    tenant_command
