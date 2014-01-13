# Scenable: Mt. Washington Edition

This time, it's *personal*.

## Deploy notes

### Admin site

The Django admin site will have two different access levels: superuser and
editor. Scenable gets superuser access, MWCDC staff get editor access. The main
reason is to disable access to editing the relations involved with Skyline view and the Place information being pulled from O2DCA.

To configure this on a deployment:


* Create a new Group with the following permissions:
	- `<Permission: places | place | Can change place>`
	- `<Permission: skyline | interest point | Can change interest point>`
	- `<Permission: skyline | viewpoint | Can change viewpoint>`

* New users from MWCDC should have the following settings:
	- `is_staff = True`
	- `groups` includes the Group created above

### Dotcloud deployment cheatsheet

*(Note that dotcloud-specific config settings are only set in the deploy-dotcloud branch)*

#### Pushing repository

The project is currently just set to deploy using rsync, using:

> dotcloud push

#### Importing/exporting data

To import data to the Dotcloud db instance, first create the dump file as follows:

> pg_dump --format=plain --no-owner --clean --no-privileges mwcdc_development > dump.sql

Then, to import, run `dotcloud env list` to get all the database env options, and use them 
in this command:

> psql --username=<USENAME> --password --port=<PORT> --host=<HOST> mwcdcserverapp_production < dump.sql
