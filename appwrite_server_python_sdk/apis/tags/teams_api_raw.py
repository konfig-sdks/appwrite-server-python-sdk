# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_server_python_sdk.paths.teams_team_id_memberships.post import CreateMembershipRequestRaw
from appwrite_server_python_sdk.paths.teams.post import CreateNewTeamRaw
from appwrite_server_python_sdk.paths.teams_team_id_memberships_membership_id.delete import DeleteMembershipRaw
from appwrite_server_python_sdk.paths.teams_team_id.get import GetByIdRaw
from appwrite_server_python_sdk.paths.teams_team_id_memberships_membership_id.get import GetMembershipRaw
from appwrite_server_python_sdk.paths.teams_team_id_prefs.get import GetPrefsByIdRaw
from appwrite_server_python_sdk.paths.teams.get import GetUserTeamsRaw
from appwrite_server_python_sdk.paths.teams_team_id_memberships.get import ListMembershipsRaw
from appwrite_server_python_sdk.paths.teams_team_id.delete import RemoveTeamByIdRaw
from appwrite_server_python_sdk.paths.teams_team_id_memberships_membership_id.patch import UpdateMembershipRolesRaw
from appwrite_server_python_sdk.paths.teams_team_id_memberships_membership_id_status.patch import UpdateMembershipStatusRaw
from appwrite_server_python_sdk.paths.teams_team_id.put import UpdateNameByIdRaw
from appwrite_server_python_sdk.paths.teams_team_id_prefs.put import UpdatePrefsByIdRaw


class TeamsApiRaw(
    CreateMembershipRequestRaw,
    CreateNewTeamRaw,
    DeleteMembershipRaw,
    GetByIdRaw,
    GetMembershipRaw,
    GetPrefsByIdRaw,
    GetUserTeamsRaw,
    ListMembershipsRaw,
    RemoveTeamByIdRaw,
    UpdateMembershipRolesRaw,
    UpdateMembershipStatusRaw,
    UpdateNameByIdRaw,
    UpdatePrefsByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
