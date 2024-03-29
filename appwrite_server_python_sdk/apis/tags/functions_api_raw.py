# coding: utf-8

"""
    Appwrite

    Appwrite backend as a service cuts up to 70% of the time and costs required for building a modern application. We abstract and simplify common development tasks behind a REST APIs, to help you develop your app in a fast and secure way. For full API documentation and tutorials go to [https://appwrite.io/docs](https://appwrite.io/docs)

    The version of the OpenAPI document: 1.5.0
    Contact: team@appwrite.io
    Created by: https://appwrite.io/support
"""

from appwrite_server_python_sdk.paths.functions_function_id_deployments_deployment_id_builds_build_id.post import CreateBuildRaw
from appwrite_server_python_sdk.paths.functions_function_id_deployments.post import CreateDeploymentFunctionCodeRaw
from appwrite_server_python_sdk.paths.functions.post import CreateNewFunctionRaw
from appwrite_server_python_sdk.paths.functions_function_id_variables.post import CreateVariableRaw
from appwrite_server_python_sdk.paths.functions_function_id.delete import DeleteByIdRaw
from appwrite_server_python_sdk.paths.functions_function_id_deployments_deployment_id.delete import DeleteDeploymentRaw
from appwrite_server_python_sdk.paths.functions_function_id_variables_variable_id.delete import DeleteVariableByIdRaw
from appwrite_server_python_sdk.paths.functions_function_id.get import GetByIdRaw
from appwrite_server_python_sdk.paths.functions_function_id_deployments_deployment_id.get import GetDeploymentByIdRaw
from appwrite_server_python_sdk.paths.functions_function_id_deployments_deployment_id_download.get import GetDeploymentContentsRaw
from appwrite_server_python_sdk.paths.functions_function_id_executions_execution_id.get import GetExecutionLogRaw
from appwrite_server_python_sdk.paths.functions_function_id_variables_variable_id.get import GetVariableByIdRaw
from appwrite_server_python_sdk.paths.functions.get import ListAllFunctionsRaw
from appwrite_server_python_sdk.paths.functions_function_id_deployments.get import ListDeploymentsRaw
from appwrite_server_python_sdk.paths.functions_function_id_executions.get import ListExecutionsRaw
from appwrite_server_python_sdk.paths.functions_runtimes.get import ListRuntimesRaw
from appwrite_server_python_sdk.paths.functions_function_id_variables.get import ListVariablesRaw
from appwrite_server_python_sdk.paths.functions_function_id_executions.post import TriggerExecutionRaw
from appwrite_server_python_sdk.paths.functions_function_id.put import UpdateByIdRaw
from appwrite_server_python_sdk.paths.functions_function_id_deployments_deployment_id.patch import UpdateDeploymentFunctionCodeRaw
from appwrite_server_python_sdk.paths.functions_function_id_variables_variable_id.put import UpdateVariableByIdRaw


class FunctionsApiRaw(
    CreateBuildRaw,
    CreateDeploymentFunctionCodeRaw,
    CreateNewFunctionRaw,
    CreateVariableRaw,
    DeleteByIdRaw,
    DeleteDeploymentRaw,
    DeleteVariableByIdRaw,
    GetByIdRaw,
    GetDeploymentByIdRaw,
    GetDeploymentContentsRaw,
    GetExecutionLogRaw,
    GetVariableByIdRaw,
    ListAllFunctionsRaw,
    ListDeploymentsRaw,
    ListExecutionsRaw,
    ListRuntimesRaw,
    ListVariablesRaw,
    TriggerExecutionRaw,
    UpdateByIdRaw,
    UpdateDeploymentFunctionCodeRaw,
    UpdateVariableByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
