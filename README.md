install-openerp
===============
A little script to get you up and running with [OpenERP](http://openerp.com).


## Launching a local development environment in Docker

1. Install docker on your machine.
2. If on Windows, ensure Linux containers is the selected container mode.
3. Run `./_docker/build.sh` in bash to build the container images.
4. Run `./_docker/deploy.sh` in bash to deploy the containers.
5. Navigate to http://localhost:8080
6. For Database Name, type `odoo`.
7. For Email Address, type `no-reply@example.com`.
8. For Password, type `admin`.
9. For Country, select `United States`.
10. Ensure `Load Demonstration data` is checked.
11. Click Create Database.