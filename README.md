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
- Molecule with docker as driver: pip3 install --user "molecule[docker]"
- Testinfra library: pip3 install testinfra

Because of limitations on docker with systemd (centos7 and 8), we need to install the following packages to run libvirt (KVM) as provider for vagrant boxes:

note: mac users have to install libvirt before using ´brew install libvirt´

```shell
pip3 install --user python-vagrant
pip3 install --user libvirt-python
pip3 install --user molecule-vagrant
pip3 install --user rich
```

About molecule + libvirt(vagrant): https://www.tauceti.blog/posts/testing-ansible-roles-with-molecule-libvirt-vagrant-qemu-kvm/

To execute tests, do the following:

```shell

$  molecule test -s default

```

To create another role like this, do the following:

```shell

$ molecule create role namespace.name-of-your-role -d docker

```
