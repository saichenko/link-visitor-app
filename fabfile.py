from fabric.api import local


def bash():
    local("docker exec -it $(docker ps | grep server_ | awk '{{ print $1 }}')"
          " bash")


def shell():
    local("docker exec -it $(docker ps | grep server_ | awk '{{ print $1 }}')"
          " python manage.py shell")


def dev():
    local("docker-compose run --rm --service-ports server")


def pip_compile_dev():
    local("docker exec -i $(docker ps | grep server_ | awk '{{ print $1 }}') "
          "pip-compile --generate-hashes requirements/development.in")


def pip_compile_prod():
    local("docker exec -i $(docker ps | grep server_ | awk '{{ print $1 }}') "
          "pip-compile --generate-hashes requirements/production.in")


def test():
    local("docker exec -it $(docker ps | grep server_ | awk '{{ print $1 }}') "
          "pytest -v")


def kill():
    local("docker kill $(docker ps -q)")
