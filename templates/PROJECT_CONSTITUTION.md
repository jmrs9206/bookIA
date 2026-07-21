# Project Constitution

## Metadata

- Project ID: `<project_id>`
- Status: `DRAFT | APPROVED`
- Version: `<version>`
- Approved by: `<human_or_pending>`
- Effective from: `YYYY-MM-DD`

## Purpose of this constitution

Define project-specific permissions and restrictions. Global policies remain applicable unless this document is stricter.

## Allowed repositories and roots

| Root | Purpose | Read | Write | Notes |
|---|---|---:|---:|---|
| `<absolute_or_workspace_relative_path>` | ... | yes | yes/no | ... |

## Prohibited paths

- ...

## Allowed roles

- `@director`
- `@product`
- `@context`
- `@architect`
- `@planner`
- `<implementation roles>`
- `@qa`
- `@reviewer`

## Project-specific role restrictions

- ...

## Technology constraints

- Required:
- Allowed:
- Prohibited:
- Versions pinned by:
- Package manager:

## Data classification

| Data type | Classification | Storage allowed | External transmission | Notes |
|---|---|---|---|---|
| ... | `PUBLIC | INTERNAL | SENSITIVE | PROHIBITED` | ... | ... | ... |

## Actions requiring human approval

- adding production dependencies;
- changing public API;
- schema migration;
- push/merge/release;
- external deployment;
- use of secrets;
- cloud resource or cost;
- destructive data action;
- license-affecting reuse.

Add project-specific gates below:

- ...

## Testing requirements

- Mandatory commands:
- Minimum environments:
- Required security checks:
- Required evidence:

## Git policy

- Default branch:
- Branch naming:
- Worktree policy:
- Commit policy:
- Merge policy:

## Definition of done additions

- ...

## Exceptions

Every exception requires owner, reason, scope, expiry and approval.

| Exception | Scope | Owner | Expiry | Approval |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
