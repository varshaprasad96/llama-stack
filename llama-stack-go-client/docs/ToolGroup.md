# ToolGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Identifier** | **string** |  | 
**ProviderResourceId** | **string** |  | 
**ProviderId** | **string** |  | 
**Type** | **string** |  | [default to "tool_group"]
**McpEndpoint** | Pointer to [**URL**](URL.md) |  | [optional] 
**Args** | Pointer to [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | [optional] 

## Methods

### NewToolGroup

`func NewToolGroup(identifier string, providerResourceId string, providerId string, type_ string, ) *ToolGroup`

NewToolGroup instantiates a new ToolGroup object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewToolGroupWithDefaults

`func NewToolGroupWithDefaults() *ToolGroup`

NewToolGroupWithDefaults instantiates a new ToolGroup object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIdentifier

`func (o *ToolGroup) GetIdentifier() string`

GetIdentifier returns the Identifier field if non-nil, zero value otherwise.

### GetIdentifierOk

`func (o *ToolGroup) GetIdentifierOk() (*string, bool)`

GetIdentifierOk returns a tuple with the Identifier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdentifier

`func (o *ToolGroup) SetIdentifier(v string)`

SetIdentifier sets Identifier field to given value.


### GetProviderResourceId

`func (o *ToolGroup) GetProviderResourceId() string`

GetProviderResourceId returns the ProviderResourceId field if non-nil, zero value otherwise.

### GetProviderResourceIdOk

`func (o *ToolGroup) GetProviderResourceIdOk() (*string, bool)`

GetProviderResourceIdOk returns a tuple with the ProviderResourceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderResourceId

`func (o *ToolGroup) SetProviderResourceId(v string)`

SetProviderResourceId sets ProviderResourceId field to given value.


### GetProviderId

`func (o *ToolGroup) GetProviderId() string`

GetProviderId returns the ProviderId field if non-nil, zero value otherwise.

### GetProviderIdOk

`func (o *ToolGroup) GetProviderIdOk() (*string, bool)`

GetProviderIdOk returns a tuple with the ProviderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderId

`func (o *ToolGroup) SetProviderId(v string)`

SetProviderId sets ProviderId field to given value.


### GetType

`func (o *ToolGroup) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ToolGroup) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ToolGroup) SetType(v string)`

SetType sets Type field to given value.


### GetMcpEndpoint

`func (o *ToolGroup) GetMcpEndpoint() URL`

GetMcpEndpoint returns the McpEndpoint field if non-nil, zero value otherwise.

### GetMcpEndpointOk

`func (o *ToolGroup) GetMcpEndpointOk() (*URL, bool)`

GetMcpEndpointOk returns a tuple with the McpEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMcpEndpoint

`func (o *ToolGroup) SetMcpEndpoint(v URL)`

SetMcpEndpoint sets McpEndpoint field to given value.

### HasMcpEndpoint

`func (o *ToolGroup) HasMcpEndpoint() bool`

HasMcpEndpoint returns a boolean if a field has been set.

### GetArgs

`func (o *ToolGroup) GetArgs() map[string]AppendRowsRequestRowsInnerValue`

GetArgs returns the Args field if non-nil, zero value otherwise.

### GetArgsOk

`func (o *ToolGroup) GetArgsOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetArgsOk returns a tuple with the Args field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArgs

`func (o *ToolGroup) SetArgs(v map[string]AppendRowsRequestRowsInnerValue)`

SetArgs sets Args field to given value.

### HasArgs

`func (o *ToolGroup) HasArgs() bool`

HasArgs returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


