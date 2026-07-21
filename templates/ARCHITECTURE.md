# Architecture

## Metadata

- Project ID: `<project_id>`
- Version: `<version>`
- Status: `DRAFT | NEEDS_APPROVAL | APPROVED | SUPERSEDED`
- Current commit inspected: `<sha>`
- Approved by: `<human_or_pending>`

## Architectural drivers

- Linked requirements:
- Quality attributes:
- Constraints:
- Risks:

## Current architecture (`CURRENT`)

Describe only verified implementation.

### Components

| Component | Responsibility | Evidence path | Status |
|---|---|---|---|
| ... | ... | ... | `IMPLEMENTED | PARTIAL | UNKNOWN` |

### Current flow

```text
...
```

## Target architecture (`TARGET`)

Describe approved intended state.

### Planes

- Control plane:
- Execution plane:
- Knowledge plane:

### Components

| Component | Responsibility | Inputs | Outputs | Trust boundary |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

### State model

```text
DRAFT -> READY -> IN_PROGRESS -> NEEDS_REVIEW -> NEEDS_APPROVAL -> DONE
                         |              |
                       BLOCKED       NEEDS_REWORK
```

### Data model

- Project:
- Run:
- Task:
- Agent assignment:
- Artifact:
- Evidence:
- Decision:
- Memory item:

### Interfaces

| Interface | Producer | Consumer | Contract | Versioning |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Options considered

| Option | Advantages | Costs | Risks | Reversibility | Decision |
|---|---|---|---|---|---|
| A | ... | ... | ... | ... | ... |

## Security and isolation

- ...

## Observability

- logs;
- traces;
- run/event IDs;
- command results;
- token/cost metrics when available;
- audit events.

## Migration plan

1. ...

## Non-goals

- ...

## Related ADRs

- ...
