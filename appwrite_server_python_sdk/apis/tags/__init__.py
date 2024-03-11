# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from appwrite_server_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    MESSAGING = "messaging"
    ACCOUNT = "account"
    DATABASES = "databases"
    USERS = "users"
    HEALTH = "health"
    FUNCTIONS = "functions"
    STORAGE = "storage"
    TEAMS = "teams"
    LOCALE = "locale"
    AVATARS = "avatars"
    GRAPHQL = "graphql"
    PROJECTS = "projects"
    PROJECT = "project"
    PROXY = "proxy"
    CONSOLE = "console"
    MIGRATIONS = "migrations"
