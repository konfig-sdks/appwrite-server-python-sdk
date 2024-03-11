operation_parameter_map = {
    '/account/mfa/authenticators/{type}-POST': {
        'parameters': [
            {
                'name': 'type'
            },
        ]
    },
    '/account/mfa/challenge-POST': {
        'parameters': [
            {
                'name': 'factor'
            },
        ]
    },
    '/account/status-PATCH': {
        'parameters': [
        ]
    },
    '/account/verification-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
        ]
    },
    '/account/mfa/challenge-PUT': {
        'parameters': [
            {
                'name': 'challengeId'
            },
            {
                'name': 'otp'
            },
        ]
    },
    '/account/recovery-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/account/verification/phone-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
        ]
    },
    '/account/sessions/anonymous-POST': {
        'parameters': [
        ]
    },
    '/account/sessions/email-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/account/tokens/email-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'phrase'
            },
        ]
    },
    '/account/verification-POST': {
        'parameters': [
            {
                'name': 'url'
            },
        ]
    },
    '/account/jwt-POST': {
        'parameters': [
        ]
    },
    '/account/tokens/magic-url-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'url'
            },
            {
                'name': 'phrase'
            },
        ]
    },
    '/account-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/account/tokens/oauth2/{provider}-GET': {
        'parameters': [
            {
                'name': 'provider'
            },
            {
                'name': 'success'
            },
            {
                'name': 'failure'
            },
            {
                'name': 'scopes'
            },
        ]
    },
    '/account/recovery-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'url'
            },
        ]
    },
    '/account/tokens/phone-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'phone'
            },
        ]
    },
    '/account/verification/phone-POST': {
        'parameters': [
        ]
    },
    '/account/sessions/token-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
        ]
    },
    '/account/mfa/authenticators/{type}-DELETE': {
        'parameters': [
            {
                'name': 'otp'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/account/identities/{identityId}-DELETE': {
        'parameters': [
            {
                'name': 'identityId'
            },
        ]
    },
    '/account/sessions-DELETE': {
        'parameters': [
        ]
    },
    '/account/sessions/{sessionId}-PATCH': {
        'parameters': [
            {
                'name': 'sessionId'
            },
        ]
    },
    '/account/mfa/recovery-codes-POST': {
        'parameters': [
        ]
    },
    '/account-GET': {
        'parameters': [
        ]
    },
    '/account/mfa/recovery-codes-GET': {
        'parameters': [
        ]
    },
    '/account/prefs-GET': {
        'parameters': [
        ]
    },
    '/account/sessions/{sessionId}-GET': {
        'parameters': [
            {
                'name': 'sessionId'
            },
        ]
    },
    '/account/identities-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
        ]
    },
    '/account/logs-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
        ]
    },
    '/account/mfa/factors-GET': {
        'parameters': [
        ]
    },
    '/account/sessions-GET': {
        'parameters': [
        ]
    },
    '/account/sessions/{sessionId}-DELETE': {
        'parameters': [
            {
                'name': 'sessionId'
            },
        ]
    },
    '/account/mfa/recovery-codes-PATCH': {
        'parameters': [
        ]
    },
    '/account/email-PATCH': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/account/sessions/magic-url-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
        ]
    },
    '/account/mfa-PATCH': {
        'parameters': [
            {
                'name': 'mfa'
            },
        ]
    },
    '/account/name-PATCH': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/account/password-PATCH': {
        'parameters': [
            {
                'name': 'password'
            },
            {
                'name': 'oldPassword'
            },
        ]
    },
    '/account/phone-PATCH': {
        'parameters': [
            {
                'name': 'phone'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/account/sessions/phone-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
        ]
    },
    '/account/prefs-PATCH': {
        'parameters': [
            {
                'name': 'prefs'
            },
        ]
    },
    '/account/mfa/authenticators/{type}-PUT': {
        'parameters': [
            {
                'name': 'otp'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/avatars/qr-GET': {
        'parameters': [
            {
                'name': 'text'
            },
            {
                'name': 'size'
            },
            {
                'name': 'margin'
            },
            {
                'name': 'download'
            },
        ]
    },
    '/avatars/browsers/{code}-GET': {
        'parameters': [
            {
                'name': 'code'
            },
            {
                'name': 'width'
            },
            {
                'name': 'height'
            },
            {
                'name': 'quality'
            },
        ]
    },
    '/avatars/flags/{code}-GET': {
        'parameters': [
            {
                'name': 'code'
            },
            {
                'name': 'width'
            },
            {
                'name': 'height'
            },
            {
                'name': 'quality'
            },
        ]
    },
    '/avatars/credit-cards/{code}-GET': {
        'parameters': [
            {
                'name': 'code'
            },
            {
                'name': 'width'
            },
            {
                'name': 'height'
            },
            {
                'name': 'quality'
            },
        ]
    },
    '/avatars/favicon-GET': {
        'parameters': [
            {
                'name': 'url'
            },
        ]
    },
    '/avatars/image-GET': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'width'
            },
            {
                'name': 'height'
            },
        ]
    },
    '/avatars/initials-GET': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'width'
            },
            {
                'name': 'height'
            },
            {
                'name': 'background'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/boolean-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'required'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'default'
            },
            {
                'name': 'array'
            },
        ]
    },
    '/databases/{databaseId}/collections-POST': {
        'parameters': [
            {
                'name': 'collectionId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'permissions'
            },
            {
                'name': 'documentSecurity'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/databases-POST': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/datetime-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'required'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'default'
            },
            {
                'name': 'array'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/documents-POST': {
        'parameters': [
            {
                'name': 'documentId'
            },
            {
                'name': 'data'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'permissions'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/email-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'required'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'default'
            },
            {
                'name': 'array'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/enum-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'elements'
            },
            {
                'name': 'required'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'default'
            },
            {
                'name': 'array'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/float-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'required'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'min'
            },
            {
                'name': 'max'
            },
            {
                'name': 'default'
            },
            {
                'name': 'array'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/indexes-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'type'
            },
            {
                'name': 'attributes'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'orders'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/integer-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'required'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'min'
            },
            {
                'name': 'max'
            },
            {
                'name': 'default'
            },
            {
                'name': 'array'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/ip-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'required'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'default'
            },
            {
                'name': 'array'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/relationship-POST': {
        'parameters': [
            {
                'name': 'relatedCollectionId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'twoWay'
            },
            {
                'name': 'key'
            },
            {
                'name': 'twoWayKey'
            },
            {
                'name': 'onDelete'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/string-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'size'
            },
            {
                'name': 'required'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'default'
            },
            {
                'name': 'array'
            },
            {
                'name': 'encrypt'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/url-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'required'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'default'
            },
            {
                'name': 'array'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/{key}-DELETE': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}-DELETE': {
        'parameters': [
            {
                'name': 'databaseId'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}-DELETE': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}-DELETE': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'documentId'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/indexes/{key}-DELETE': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/{key}-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'documentId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/indexes/{key}-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/documents-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/databases/{databaseId}/collections-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/indexes-GET': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/boolean/{key}-PATCH': {
        'parameters': [
            {
                'name': 'required'
            },
            {
                'name': 'default'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'permissions'
            },
            {
                'name': 'documentSecurity'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/datetime/{key}-PATCH': {
        'parameters': [
            {
                'name': 'required'
            },
            {
                'name': 'default'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/documents/{documentId}-PATCH': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'documentId'
            },
            {
                'name': 'data'
            },
            {
                'name': 'permissions'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/email/{key}-PATCH': {
        'parameters': [
            {
                'name': 'required'
            },
            {
                'name': 'default'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/enum/{key}-PATCH': {
        'parameters': [
            {
                'name': 'elements'
            },
            {
                'name': 'required'
            },
            {
                'name': 'default'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/float/{key}-PATCH': {
        'parameters': [
            {
                'name': 'required'
            },
            {
                'name': 'min'
            },
            {
                'name': 'max'
            },
            {
                'name': 'default'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/integer/{key}-PATCH': {
        'parameters': [
            {
                'name': 'required'
            },
            {
                'name': 'min'
            },
            {
                'name': 'max'
            },
            {
                'name': 'default'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/ip/{key}-PATCH': {
        'parameters': [
            {
                'name': 'required'
            },
            {
                'name': 'default'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/{key}/relationship-PATCH': {
        'parameters': [
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
            {
                'name': 'onDelete'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/string/{key}-PATCH': {
        'parameters': [
            {
                'name': 'required'
            },
            {
                'name': 'default'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/databases/{databaseId}/collections/{collectionId}/attributes/url/{key}-PATCH': {
        'parameters': [
            {
                'name': 'required'
            },
            {
                'name': 'default'
            },
            {
                'name': 'databaseId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/functions/{functionId}/deployments/{deploymentId}/builds/{buildId}-POST': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'deploymentId'
            },
            {
                'name': 'buildId'
            },
        ]
    },
    '/functions/{functionId}/deployments-POST': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'code'
            },
            {
                'name': 'activate'
            },
            {
                'name': 'entrypoint'
            },
            {
                'name': 'commands'
            },
        ]
    },
    '/functions-POST': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'runtime'
            },
            {
                'name': 'execute'
            },
            {
                'name': 'events'
            },
            {
                'name': 'schedule'
            },
            {
                'name': 'timeout'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'logging'
            },
            {
                'name': 'entrypoint'
            },
            {
                'name': 'commands'
            },
            {
                'name': 'installationId'
            },
            {
                'name': 'providerRepositoryId'
            },
            {
                'name': 'providerBranch'
            },
            {
                'name': 'providerSilentMode'
            },
            {
                'name': 'providerRootDirectory'
            },
            {
                'name': 'templateRepository'
            },
            {
                'name': 'templateOwner'
            },
            {
                'name': 'templateRootDirectory'
            },
            {
                'name': 'templateBranch'
            },
        ]
    },
    '/functions/{functionId}/variables-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'value'
            },
            {
                'name': 'functionId'
            },
        ]
    },
    '/functions/{functionId}-DELETE': {
        'parameters': [
            {
                'name': 'functionId'
            },
        ]
    },
    '/functions/{functionId}/deployments/{deploymentId}-DELETE': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'deploymentId'
            },
        ]
    },
    '/functions/{functionId}/variables/{variableId}-DELETE': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'variableId'
            },
        ]
    },
    '/functions/{functionId}-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
        ]
    },
    '/functions/{functionId}/deployments/{deploymentId}-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'deploymentId'
            },
        ]
    },
    '/functions/{functionId}/deployments/{deploymentId}/download-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'deploymentId'
            },
        ]
    },
    '/functions/{functionId}/executions/{executionId}-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'executionId'
            },
        ]
    },
    '/functions/{functionId}/variables/{variableId}-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'variableId'
            },
        ]
    },
    '/functions-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/functions/{functionId}/deployments-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/functions/{functionId}/executions-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/functions/runtimes-GET': {
        'parameters': [
        ]
    },
    '/functions/{functionId}/variables-GET': {
        'parameters': [
            {
                'name': 'functionId'
            },
        ]
    },
    '/functions/{functionId}/executions-POST': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'body'
            },
            {
                'name': 'async'
            },
            {
                'name': 'path'
            },
            {
                'name': 'method'
            },
            {
                'name': 'headers'
            },
        ]
    },
    '/functions/{functionId}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'functionId'
            },
            {
                'name': 'runtime'
            },
            {
                'name': 'execute'
            },
            {
                'name': 'events'
            },
            {
                'name': 'schedule'
            },
            {
                'name': 'timeout'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'logging'
            },
            {
                'name': 'entrypoint'
            },
            {
                'name': 'commands'
            },
            {
                'name': 'installationId'
            },
            {
                'name': 'providerRepositoryId'
            },
            {
                'name': 'providerBranch'
            },
            {
                'name': 'providerSilentMode'
            },
            {
                'name': 'providerRootDirectory'
            },
        ]
    },
    '/functions/{functionId}/deployments/{deploymentId}-PATCH': {
        'parameters': [
            {
                'name': 'functionId'
            },
            {
                'name': 'deploymentId'
            },
        ]
    },
    '/functions/{functionId}/variables/{variableId}-PUT': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'functionId'
            },
            {
                'name': 'variableId'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/graphql-POST': {
        'parameters': [
        ]
    },
    '/graphql/mutation-POST': {
        'parameters': [
        ]
    },
    '/health/anti-virus-GET': {
        'parameters': [
        ]
    },
    '/health/cache-GET': {
        'parameters': [
        ]
    },
    '/health/db-GET': {
        'parameters': [
        ]
    },
    '/health/storage/local-GET': {
        'parameters': [
        ]
    },
    '/health/pubsub-GET': {
        'parameters': [
        ]
    },
    '/health-GET': {
        'parameters': [
        ]
    },
    '/health/storage-GET': {
        'parameters': [
        ]
    },
    '/health/queue/functions-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/queue/builds-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/queue/databases-GET': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/queue/deletes-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/queue/failed/{name}-GET': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/queue/mails-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/queue/migrations-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/queue/logs-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/queue/messaging-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/queue-GET': {
        'parameters': [
        ]
    },
    '/health/queue/usage-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/queue/usage-dump-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/certificate-GET': {
        'parameters': [
            {
                'name': 'domain'
            },
        ]
    },
    '/health/time-GET': {
        'parameters': [
        ]
    },
    '/health/queue/webhooks-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/health/queue/certificates-GET': {
        'parameters': [
            {
                'name': 'threshold'
            },
        ]
    },
    '/locale/languages-GET': {
        'parameters': [
        ]
    },
    '/locale-GET': {
        'parameters': [
        ]
    },
    '/locale/codes-GET': {
        'parameters': [
        ]
    },
    '/locale/continents-GET': {
        'parameters': [
        ]
    },
    '/locale/countries-GET': {
        'parameters': [
        ]
    },
    '/locale/currencies-GET': {
        'parameters': [
        ]
    },
    '/locale/countries/eu-GET': {
        'parameters': [
        ]
    },
    '/locale/countries/phones-GET': {
        'parameters': [
        ]
    },
    '/messaging/providers/apns-POST': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'authKey'
            },
            {
                'name': 'authKeyId'
            },
            {
                'name': 'teamId'
            },
            {
                'name': 'bundleId'
            },
            {
                'name': 'sandbox'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/messages/email-POST': {
        'parameters': [
            {
                'name': 'messageId'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'content'
            },
            {
                'name': 'topics'
            },
            {
                'name': 'users'
            },
            {
                'name': 'targets'
            },
            {
                'name': 'cc'
            },
            {
                'name': 'bcc'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'draft'
            },
            {
                'name': 'html'
            },
            {
                'name': 'scheduledAt'
            },
        ]
    },
    '/messaging/providers/fcm-POST': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'serviceAccountJSON'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/providers/msg91-POST': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'from'
            },
            {
                'name': 'senderId'
            },
            {
                'name': 'authKey'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/providers/mailgun-POST': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'isEuRegion'
            },
            {
                'name': 'fromName'
            },
            {
                'name': 'fromEmail'
            },
            {
                'name': 'replyToName'
            },
            {
                'name': 'replyToEmail'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/messages/push-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'messageId'
            },
            {
                'name': 'body'
            },
            {
                'name': 'topics'
            },
            {
                'name': 'users'
            },
            {
                'name': 'targets'
            },
            {
                'name': 'data'
            },
            {
                'name': 'action'
            },
            {
                'name': 'image'
            },
            {
                'name': 'icon'
            },
            {
                'name': 'sound'
            },
            {
                'name': 'color'
            },
            {
                'name': 'tag'
            },
            {
                'name': 'badge'
            },
            {
                'name': 'draft'
            },
            {
                'name': 'scheduledAt'
            },
        ]
    },
    '/messaging/providers/sendgrid-POST': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'fromName'
            },
            {
                'name': 'fromEmail'
            },
            {
                'name': 'replyToName'
            },
            {
                'name': 'replyToEmail'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/messages/sms-POST': {
        'parameters': [
            {
                'name': 'messageId'
            },
            {
                'name': 'content'
            },
            {
                'name': 'topics'
            },
            {
                'name': 'users'
            },
            {
                'name': 'targets'
            },
            {
                'name': 'draft'
            },
            {
                'name': 'scheduledAt'
            },
        ]
    },
    '/messaging/providers/smtp-POST': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'host'
            },
            {
                'name': 'port'
            },
            {
                'name': 'username'
            },
            {
                'name': 'password'
            },
            {
                'name': 'encryption'
            },
            {
                'name': 'autoTLS'
            },
            {
                'name': 'mailer'
            },
            {
                'name': 'fromName'
            },
            {
                'name': 'fromEmail'
            },
            {
                'name': 'replyToName'
            },
            {
                'name': 'replyToEmail'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/topics/{topicId}/subscribers-POST': {
        'parameters': [
            {
                'name': 'subscriberId'
            },
            {
                'name': 'targetId'
            },
            {
                'name': 'topicId'
            },
        ]
    },
    '/messaging/providers/telesign-POST': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'from'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/providers/textmagic-POST': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'from'
            },
            {
                'name': 'username'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/topics-POST': {
        'parameters': [
            {
                'name': 'topicId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'subscribe'
            },
        ]
    },
    '/messaging/providers/twilio-POST': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'from'
            },
            {
                'name': 'accountSid'
            },
            {
                'name': 'authToken'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/providers/vonage-POST': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'from'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'apiSecret'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/messages/{messageId}-DELETE': {
        'parameters': [
            {
                'name': 'messageId'
            },
        ]
    },
    '/messaging/providers/{providerId}-DELETE': {
        'parameters': [
            {
                'name': 'providerId'
            },
        ]
    },
    '/messaging/topics/{topicId}/subscribers/{subscriberId}-DELETE': {
        'parameters': [
            {
                'name': 'topicId'
            },
            {
                'name': 'subscriberId'
            },
        ]
    },
    '/messaging/topics/{topicId}-DELETE': {
        'parameters': [
            {
                'name': 'topicId'
            },
        ]
    },
    '/messaging/messages/{messageId}-GET': {
        'parameters': [
            {
                'name': 'messageId'
            },
        ]
    },
    '/messaging/messages/{messageId}/logs-GET': {
        'parameters': [
            {
                'name': 'messageId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/messaging/providers/{providerId}-GET': {
        'parameters': [
            {
                'name': 'providerId'
            },
        ]
    },
    '/messaging/topics/{topicId}/subscribers/{subscriberId}-GET': {
        'parameters': [
            {
                'name': 'topicId'
            },
            {
                'name': 'subscriberId'
            },
        ]
    },
    '/messaging/topics/{topicId}-GET': {
        'parameters': [
            {
                'name': 'topicId'
            },
        ]
    },
    '/messaging/messages/{messageId}/targets-GET': {
        'parameters': [
            {
                'name': 'messageId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/messaging/messages-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/messaging/providers/{providerId}/logs-GET': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/messaging/providers-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/messaging/subscribers/{subscriberId}/logs-GET': {
        'parameters': [
            {
                'name': 'subscriberId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/messaging/topics/{topicId}/subscribers-GET': {
        'parameters': [
            {
                'name': 'topicId'
            },
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/messaging/topics/{topicId}/logs-GET': {
        'parameters': [
            {
                'name': 'topicId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/messaging/topics-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/messaging/providers/apns/{providerId}-PATCH': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'authKey'
            },
            {
                'name': 'authKeyId'
            },
            {
                'name': 'teamId'
            },
            {
                'name': 'bundleId'
            },
            {
                'name': 'sandbox'
            },
        ]
    },
    '/messaging/messages/email/{messageId}-PATCH': {
        'parameters': [
            {
                'name': 'messageId'
            },
            {
                'name': 'topics'
            },
            {
                'name': 'users'
            },
            {
                'name': 'targets'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'content'
            },
            {
                'name': 'draft'
            },
            {
                'name': 'html'
            },
            {
                'name': 'cc'
            },
            {
                'name': 'bcc'
            },
            {
                'name': 'scheduledAt'
            },
        ]
    },
    '/messaging/providers/fcm/{providerId}-PATCH': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'serviceAccountJSON'
            },
        ]
    },
    '/messaging/providers/mailgun/{providerId}-PATCH': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'isEuRegion'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'fromName'
            },
            {
                'name': 'fromEmail'
            },
            {
                'name': 'replyToName'
            },
            {
                'name': 'replyToEmail'
            },
        ]
    },
    '/messaging/providers/msg91/{providerId}-PATCH': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'senderId'
            },
            {
                'name': 'authKey'
            },
            {
                'name': 'from'
            },
        ]
    },
    '/messaging/providers/sendgrid/{providerId}-PATCH': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'fromName'
            },
            {
                'name': 'fromEmail'
            },
            {
                'name': 'replyToName'
            },
            {
                'name': 'replyToEmail'
            },
        ]
    },
    '/messaging/providers/smtp/{providerId}-PATCH': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'host'
            },
            {
                'name': 'port'
            },
            {
                'name': 'username'
            },
            {
                'name': 'password'
            },
            {
                'name': 'encryption'
            },
            {
                'name': 'autoTLS'
            },
            {
                'name': 'mailer'
            },
            {
                'name': 'fromName'
            },
            {
                'name': 'fromEmail'
            },
            {
                'name': 'replyToName'
            },
            {
                'name': 'replyToEmail'
            },
            {
                'name': 'enabled'
            },
        ]
    },
    '/messaging/messages/push/{messageId}-PATCH': {
        'parameters': [
            {
                'name': 'messageId'
            },
            {
                'name': 'title'
            },
            {
                'name': 'topics'
            },
            {
                'name': 'users'
            },
            {
                'name': 'targets'
            },
            {
                'name': 'body'
            },
            {
                'name': 'data'
            },
            {
                'name': 'action'
            },
            {
                'name': 'image'
            },
            {
                'name': 'icon'
            },
            {
                'name': 'sound'
            },
            {
                'name': 'color'
            },
            {
                'name': 'tag'
            },
            {
                'name': 'badge'
            },
            {
                'name': 'draft'
            },
            {
                'name': 'scheduledAt'
            },
        ]
    },
    '/messaging/messages/sms/{messageId}-PATCH': {
        'parameters': [
            {
                'name': 'messageId'
            },
            {
                'name': 'topics'
            },
            {
                'name': 'users'
            },
            {
                'name': 'targets'
            },
            {
                'name': 'content'
            },
            {
                'name': 'draft'
            },
            {
                'name': 'scheduledAt'
            },
        ]
    },
    '/messaging/providers/telesign/{providerId}-PATCH': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'customerId'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'from'
            },
        ]
    },
    '/messaging/providers/textmagic/{providerId}-PATCH': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'username'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'from'
            },
        ]
    },
    '/messaging/topics/{topicId}-PATCH': {
        'parameters': [
            {
                'name': 'topicId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'subscribe'
            },
        ]
    },
    '/messaging/providers/twilio/{providerId}-PATCH': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'accountSid'
            },
            {
                'name': 'authToken'
            },
            {
                'name': 'from'
            },
        ]
    },
    '/messaging/providers/vonage/{providerId}-PATCH': {
        'parameters': [
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'apiKey'
            },
            {
                'name': 'apiSecret'
            },
            {
                'name': 'from'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files-POST': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
            {
                'name': 'file'
            },
            {
                'name': 'permissions'
            },
        ]
    },
    '/storage/buckets-POST': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'permissions'
            },
            {
                'name': 'fileSecurity'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'maximumFileSize'
            },
            {
                'name': 'allowedFileExtensions'
            },
            {
                'name': 'compression'
            },
            {
                'name': 'encryption'
            },
            {
                'name': 'antivirus'
            },
        ]
    },
    '/storage/buckets/{bucketId}-DELETE': {
        'parameters': [
            {
                'name': 'bucketId'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files/{fileId}-DELETE': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
        ]
    },
    '/storage/buckets/{bucketId}-GET': {
        'parameters': [
            {
                'name': 'bucketId'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files/{fileId}-GET': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files/{fileId}/download-GET': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files/{fileId}/preview-GET': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
            {
                'name': 'width'
            },
            {
                'name': 'height'
            },
            {
                'name': 'gravity'
            },
            {
                'name': 'quality'
            },
            {
                'name': 'borderWidth'
            },
            {
                'name': 'borderColor'
            },
            {
                'name': 'borderRadius'
            },
            {
                'name': 'opacity'
            },
            {
                'name': 'rotation'
            },
            {
                'name': 'background'
            },
            {
                'name': 'output'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files/{fileId}/view-GET': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
        ]
    },
    '/storage/buckets-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files-GET': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/storage/buckets/{bucketId}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'bucketId'
            },
            {
                'name': 'permissions'
            },
            {
                'name': 'fileSecurity'
            },
            {
                'name': 'enabled'
            },
            {
                'name': 'maximumFileSize'
            },
            {
                'name': 'allowedFileExtensions'
            },
            {
                'name': 'compression'
            },
            {
                'name': 'encryption'
            },
            {
                'name': 'antivirus'
            },
        ]
    },
    '/storage/buckets/{bucketId}/files/{fileId}-PUT': {
        'parameters': [
            {
                'name': 'bucketId'
            },
            {
                'name': 'fileId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'permissions'
            },
        ]
    },
    '/teams/{teamId}/memberships-POST': {
        'parameters': [
            {
                'name': 'roles'
            },
            {
                'name': 'teamId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'url'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/teams-POST': {
        'parameters': [
            {
                'name': 'teamId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'roles'
            },
        ]
    },
    '/teams/{teamId}/memberships/{membershipId}-DELETE': {
        'parameters': [
            {
                'name': 'teamId'
            },
            {
                'name': 'membershipId'
            },
        ]
    },
    '/teams/{teamId}-GET': {
        'parameters': [
            {
                'name': 'teamId'
            },
        ]
    },
    '/teams/{teamId}/memberships/{membershipId}-GET': {
        'parameters': [
            {
                'name': 'teamId'
            },
            {
                'name': 'membershipId'
            },
        ]
    },
    '/teams/{teamId}/prefs-GET': {
        'parameters': [
            {
                'name': 'teamId'
            },
        ]
    },
    '/teams-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/teams/{teamId}/memberships-GET': {
        'parameters': [
            {
                'name': 'teamId'
            },
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/teams/{teamId}-DELETE': {
        'parameters': [
            {
                'name': 'teamId'
            },
        ]
    },
    '/teams/{teamId}/memberships/{membershipId}-PATCH': {
        'parameters': [
            {
                'name': 'roles'
            },
            {
                'name': 'teamId'
            },
            {
                'name': 'membershipId'
            },
        ]
    },
    '/teams/{teamId}/memberships/{membershipId}/status-PATCH': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'secret'
            },
            {
                'name': 'teamId'
            },
            {
                'name': 'membershipId'
            },
        ]
    },
    '/teams/{teamId}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'teamId'
            },
        ]
    },
    '/teams/{teamId}/prefs-PUT': {
        'parameters': [
            {
                'name': 'prefs'
            },
            {
                'name': 'teamId'
            },
        ]
    },
    '/users/argon2-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/users/bcrypt-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/users/md5-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/users/{userId}/mfa/recovery-codes-PATCH': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'password'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/users/phpass-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/users/scrypt-modified-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
            {
                'name': 'passwordSalt'
            },
            {
                'name': 'passwordSaltSeparator'
            },
            {
                'name': 'passwordSignerKey'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/users/scrypt-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
            {
                'name': 'passwordSalt'
            },
            {
                'name': 'passwordCpu'
            },
            {
                'name': 'passwordMemory'
            },
            {
                'name': 'passwordParallel'
            },
            {
                'name': 'passwordLength'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/users/{userId}/sessions-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/sha-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'password'
            },
            {
                'name': 'passwordVersion'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/users/{userId}/targets-POST': {
        'parameters': [
            {
                'name': 'targetId'
            },
            {
                'name': 'providerType'
            },
            {
                'name': 'identifier'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/users/{userId}/tokens-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'length'
            },
            {
                'name': 'expire'
            },
        ]
    },
    '/users/{userId}/mfa/authenticators/{type}-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/users/identities/{identityId}-DELETE': {
        'parameters': [
            {
                'name': 'identityId'
            },
        ]
    },
    '/users/{userId}/sessions/{sessionId}-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'sessionId'
            },
        ]
    },
    '/users/{userId}/targets/{targetId}-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'targetId'
            },
        ]
    },
    '/users/{userId}-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/sessions-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/mfa/recovery-codes-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/prefs-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/targets/{targetId}-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'targetId'
            },
        ]
    },
    '/users-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/users/{userId}/mfa/factors-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/identities-GET': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'search'
            },
        ]
    },
    '/users/{userId}/memberships-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/sessions-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/targets-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/users/{userId}/logs-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'queries'
            },
        ]
    },
    '/users/{userId}/mfa/recovery-codes-PUT': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/email-PATCH': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/verification-PATCH': {
        'parameters': [
            {
                'name': 'emailVerification'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/labels-PUT': {
        'parameters': [
            {
                'name': 'labels'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/mfa-PATCH': {
        'parameters': [
            {
                'name': 'mfa'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/password-PATCH': {
        'parameters': [
            {
                'name': 'password'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/phone-PATCH': {
        'parameters': [
            {
                'name': 'number'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/verification/phone-PATCH': {
        'parameters': [
            {
                'name': 'phoneVerification'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/prefs-PATCH': {
        'parameters': [
            {
                'name': 'prefs'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/status-PATCH': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/targets/{targetId}-PATCH': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'targetId'
            },
            {
                'name': 'identifier'
            },
            {
                'name': 'providerId'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/users/{userId}/name-PATCH': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'userId'
            },
        ]
    },
};