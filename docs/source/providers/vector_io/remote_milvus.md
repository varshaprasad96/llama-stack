# remote::milvus

## Description


[Milvus](https://milvus.io/) is an inline and remote vector database provider for Llama Stack. It
allows you to store and query vectors directly within a Milvus database.
That means you're not limited to storing vectors in memory or in a separate service.

## Features

- Easy to use
- Fully integrated with Llama Stack

## Usage

To use Milvus in your Llama Stack project, follow these steps:

1. Install the necessary dependencies.
2. Configure your Llama Stack project to use Milvus.
3. Start storing and querying vectors.

## Installation

You can install Milvus using pymilvus:

```bash
pip install pymilvus
```

## Configuration

In Llama Stack, Milvus can be configured in two ways:
- **Inline (Local) Configuration** - Uses Milvus-Lite for local storage
- **Remote Configuration** - Connects to a remote Milvus server

### Inline (Local) Configuration

The simplest method is local configuration, which requires setting `db_path`, a path for locally storing Milvus-Lite files:

```yaml
vector_io:
  - provider_id: milvus
    provider_type: inline::milvus
    config:
      db_path: ~/.llama/distributions/together/milvus_store.db
```

### Remote Configuration

Remote configuration is suitable for larger data storage requirements:

#### Standard Remote Connection

```yaml
vector_io:
  - provider_id: milvus
    provider_type: remote::milvus
    config:
      uri: "http://<host>:<port>"
      token: "<user>:<password>"
```

#### TLS-Enabled Remote Connection (One-way TLS)

For connections to Milvus instances with one-way TLS enabled:

```yaml
vector_io:
  - provider_id: milvus
    provider_type: remote::milvus
    config:
      uri: "https://<host>:<port>"
      token: "<user>:<password>"
      secure: True
      server_pem_path: "/path/to/server.pem"
```

#### Mutual TLS (mTLS) Remote Connection

For connections to Milvus instances with mutual TLS (mTLS) enabled:

```yaml
vector_io:
  - provider_id: milvus
    provider_type: remote::milvus
    config:
      uri: "https://<host>:<port>"
      token: "<user>:<password>"
      secure: True
      ca_pem_path: "/path/to/ca.pem"
      client_pem_path: "/path/to/client.pem"
      client_key_path: "/path/to/client.key"
```

#### Key Parameters for TLS Configuration

- **`secure`**: Enables TLS encryption when set to `true`. Defaults to `false`.
- **`server_pem_path`**: Path to the **server certificate** for verifying the server's identity (used in one-way TLS).
- **`ca_pem_path`**: Path to the **Certificate Authority (CA) certificate** for validating the server certificate (required in mTLS).
- **`client_pem_path`**: Path to the **client certificate** file (required for mTLS).
- **`client_key_path`**: Path to the **client private key** file (required for mTLS).

## Supported Search Modes

The Milvus provider supports both vector-based and keyword-based (full-text) search modes, but with some limitations:

- Remote Milvus supports both vector-based and keyword-based search modes.
- Inline Milvus (Milvus-Lite) only supports vector-based search. Keyword search is not supported as Milvus-Lite has not implemented this functionality yet. For updates on this feature, see [Milvus GitHub Issue #40848](https://github.com/milvus-io/milvus/issues/40848).

When using the RAGTool interface, you can specify the desired search behavior via the `mode` parameter in `RAGQueryConfig`. For more details on Milvus's implementation of keyword search modes, refer to the [Milvus documentation](https://milvus.io/docs/full_text_search_with_milvus.md).

## Documentation
See the [Milvus documentation](https://milvus.io/docs/install-overview.md) for more details about Milvus in general.

For more details on TLS configuration, refer to the [TLS setup guide](https://milvus.io/docs/tls.md).


## Configuration

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `uri` | `<class 'str'>` | No | PydanticUndefined | The URI of the Milvus server |
| `token` | `str \| None` | No | PydanticUndefined | The token of the Milvus server |
| `consistency_level` | `<class 'str'>` | No | Strong | The consistency level of the Milvus server |
| `kvstore` | `utils.kvstore.config.RedisKVStoreConfig \| utils.kvstore.config.SqliteKVStoreConfig \| utils.kvstore.config.PostgresKVStoreConfig \| utils.kvstore.config.MongoDBKVStoreConfig, annotation=NoneType, required=False, default='sqlite', discriminator='type'` | No |  | Config for KV store backend (SQLite only for now) |
| `config` | `dict` | No | {} | This configuration allows additional fields to be passed through to the underlying Milvus client. See the [Milvus](https://milvus.io/docs/install-overview.md) documentation for more details about Milvus in general. |

> **Note**: This configuration class accepts additional fields beyond those listed above. You can pass any additional configuration options that will be forwarded to the underlying provider.

## Sample Configuration

```yaml
uri: ${env.MILVUS_ENDPOINT}
token: ${env.MILVUS_TOKEN}

```

