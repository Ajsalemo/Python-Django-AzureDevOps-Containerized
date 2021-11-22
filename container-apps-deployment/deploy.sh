#!/bin/bash

az deployment group create \
  --resource-group "$RESOURCE_GROUP" \
  --template-file deploy.json \
  --parameters \
      environment_name="$CONTAINERAPPS_ENVIRONMENT" \
      location="$LOCATION" \
      name="$NAME" \
      acr-password="$ACR_PASSWORD" \
      postgres-engine-secret-ref="$POSTGRES_ENGINE_SECRET_REF" \
      postgres-name-secret-ref="$POSTGRES_NAME_SECRET_REF" \
      postgres-user-secret-ref="$POSTGRES_USER_SECRET_REF" \
      postgres-host-secret-ref="$POSTGRES_HOST_SECRET_REF" \
      postgres-port-secret-ref="$POSTGRES_PORT_SECRET_REF" \
      postgres-password-secret-ref="$POSTGRES_PASSWORD_SECRET_REF" \
      unsplash-api-prefix-secret-ref="$UNSPLASH_API_PREFIX_SECRET_REF" \
      unsplash-api-access-key-secret-ref="$UNSPLASH_API_ACCESS_KEY_SECRET_REF" \
      unsplash-api-secret-key-secret-ref="$UNSPLASH_API_SECRET_KEY_SECRET_REF"


