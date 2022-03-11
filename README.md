# Role Nginx

Intall and configure NGINX as a reverse proxy

## Requirements

A debian/ubuntu server, with python3 installed, a valid user and password for the root

## Role Variables

This role dont have any variable

## Dependencies

This role dont have any dependencies

## Example Playbook

    - hosts: localhost
      become: true
      roles:
         - nginx

## Molecule

This role was created using molecule.

First of all, you need to install:

- Python3
- Ansible : pip3 install ansible
- Molecule with docker as driver: python3 -m pip install --user "molecule[docker]"

To create another role like this, do the following:

```shell

$ molecule create role namespace.name-of-your-role -d docker

```

To execute tests, do the following:

```shell

$ molecule test

```
