# Scenable: Mt. Washington Edition

This time, it's *personal*.

# Deploy notes

## Admin site

The Django admin site will have two different access levels: superuser and
editor. Scenable gets superuser access, MWCDC staff get editor access. The main
reason is to disable access to editing the relations involved with Skyline view and the Place information being pulled from O2DCA.

To configure this on a deployment:

1. Create a new Group with the following permissions:

	- `<Permission: places | place | Can change place>`
	- `<Permission: skyline | interest point | Can change interest point>`
	- `<Permission: skyline | viewpoint | Can change viewpoint>`

2. New users from MWCDC should have the following settings:

	- `is_staff = True`
	- `groups` includes the Group created above
