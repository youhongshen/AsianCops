The configure directory contains automation scripts using ansible.
The tasks are written specific to deploying to an AWS ec2 instance
with RHEL 7 and RDS with MySQL.

Roles:
- aws: creates ec2 and RDS instances (IAM roles are pre-configured manually)
- circle: retrieves artifact after it's built by Circle CI
- web: sets up the web server and deploys the artifact