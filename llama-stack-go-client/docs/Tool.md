# Tool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Identifier** | **string** |  | 
**ProviderResourceId** | **string** |  | 
**ProviderId** | **string** |  | 
**Type** | **string** |  | [default to "tool"]
**ToolgroupId** | **string** |  | 
**ToolHost** | [**ToolHost**](ToolHost.md) |  | 
**Description** | **string** |  | 
**Parameters** | [**[]ToolParameter**](ToolParameter.md) |  | 
**Metadata** | Pointer to [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | [optional] 

## Methods

### NewTool

`func NewTool(identifier string, providerResourceId string, providerId string, type_ string, toolgroupId string, toolHost ToolHost, description string, parameters []ToolParameter, ) *Tool`

NewTool instantiates a new Tool object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewToolWithDefaults

`func NewToolWithDefaults() *Tool`

NewToolWithDefaults instantiates a new Tool object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIdentifier

`func (o *Tool) GetIdentifier() string`

GetIdentifier returns the Identifier field if non-nil, zero value otherwise.

### GetIdentifierOk

`func (o *Tool) GetIdentifierOk() (*string, bool)`

GetIdentifierOk returns a tuple with the Identifier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdentifier

`func (o *Tool) SetIdentifier(v string)`

SetIdentifier sets Identifier field to given value.


### GetProviderResourceId

`func (o *Tool) GetProviderResourceId() string`

GetProviderResourceId returns the ProviderResourceId field if non-nil, zero value otherwise.

### GetProviderResourceIdOk

`func (o *Tool) GetProviderResourceIdOk() (*string, bool)`

GetProviderResourceIdOk returns a tuple with the ProviderResourceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderResourceId

`func (o *Tool) SetProviderResourceId(v string)`

SetProviderResourceId sets ProviderResourceId field to given value.


### GetProviderId

`func (o *Tool) GetProviderId() string`

GetProviderId returns the ProviderId field if non-nil, zero value otherwise.

### GetProviderIdOk

`func (o *Tool) GetProviderIdOk() (*string, bool)`

GetProviderIdOk returns a tuple with the ProviderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderId

`func (o *Tool) SetProviderId(v string)`

SetProviderId sets ProviderId field to given value.


### GetType

`func (o *Tool) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *Tool) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *Tool) SetType(v string)`

SetType sets Type field to given value.


### GetToolgroupId

`func (o *Tool) GetToolgroupId() string`

GetToolgroupId returns the ToolgroupId field if non-nil, zero value otherwise.

### GetToolgroupIdOk

`func (o *Tool) GetToolgroupIdOk() (*string, bool)`

GetToolgroupIdOk returns a tuple with the ToolgroupId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolgroupId

`func (o *Tool) SetToolgroupId(v string)`

SetToolgroupId sets ToolgroupId field to given value.


### GetToolHost

`func (o *Tool) GetToolHost() ToolHost`

GetToolHost returns the ToolHost field if non-nil, zero value otherwise.

### GetToolHostOk

`func (o *Tool) GetToolHostOk() (*ToolHost, bool)`

GetToolHostOk returns a tuple with the ToolHost field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolHost

`func (o *Tool) SetToolHost(v ToolHost)`

SetToolHost sets ToolHost field to given value.


### GetDescription

`func (o *Tool) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Tool) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Tool) SetDescription(v string)`

SetDescription sets Description field to given value.


### GetParameters

`func (o *Tool) GetParameters() []ToolParameter`

GetParameters returns the Parameters field if non-nil, zero value otherwise.

### GetParametersOk

`func (o *Tool) GetParametersOk() (*[]ToolParameter, bool)`

GetParametersOk returns a tuple with the Parameters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParameters

`func (o *Tool) SetParameters(v []ToolParameter)`

SetParameters sets Parameters field to given value.


### GetMetadata

`func (o *Tool) GetMetadata() map[string]AppendRowsRequestRowsInnerValue`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *Tool) GetMetadataOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *Tool) SetMetadata(v map[string]AppendRowsRequestRowsInnerValue)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *Tool) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


