def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644


def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed
    # latest nginx version for centos7
    assert nginx.version.startswith("1.20.1")


def test_nginx_running(host):
    nginx = host.service("nginx")
    assert nginx.is_running
