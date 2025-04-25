# RegisterToolGroupRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ToolgroupId** | **string** |  | 
**ProviderId** | **string** |  | 
**McpEndpoint** | Pointer to [**URL**](URL.md) |  | [optional] 
**Args** | Pointer to [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | [optional] 

## Methods

### NewRegisterToolGroupRequest

`func NewRegisterToolGroupRequest(toolgroupId string, providerId string, ) *RegisterToolGroupRequest`

NewRegisterToolGroupRequest instantiates a new RegisterToolGroupRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRegisterToolGroupRequestWithDefaults

`func NewRegisterToolGroupRequestWithDefaults() *RegisterToolGroupRequest`

NewRegisterToolGroupRequestWithDefaults instantiates a new RegisterToolGroupRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetToolgroupId

`func (o *RegisterToolGroupRequest) GetToolgroupId() string`

GetToolgroupId returns the ToolgroupId field if non-nil, zero value otherwise.

### GetToolgroupIdOk

`func (o *RegisterToolGroupRequest) GetToolgroupIdOk() (*string, bool)`

GetToolgroupIdOk returns a tuple with the ToolgroupId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToolgroupId

`func (o *RegisterToolGroupRequest) SetToolgroupId(v string)`

SetToolgroupId sets ToolgroupId field to given value.


### GetProviderId

`func (o *RegisterToolGroupRequest) GetProviderId() string`

GetProviderId returns the ProviderId field if non-nil, zero value otherwise.

### GetProviderIdOk

`func (o *RegisterToolGroupRequest) GetProviderIdOk() (*string, bool)`

GetProviderIdOk returns a tuple with the ProviderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderId

`func (o *RegisterToolGroupRequest) SetProviderId(v string)`

SetProviderId sets ProviderId field to given value.


### GetMcpEndpoint

`func (o *RegisterToolGroupRequest) GetMcpEndpoint() URL`

GetMcpEndpoint returns the McpEndpoint field if non-nil, zero value otherwise.

### GetMcpEndpointOk

`func (o *RegisterToolGroupRequest) GetMcpEndpointOk() (*URL, bool)`

GetMcpEndpointOk returns a tuple with the McpEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMcpEndpoint

`func (o *RegisterToolGroupRequest) SetMcpEndpoint(v URL)`

SetMcpEndpoint sets McpEndpoint field to given value.

### HasMcpEndpoint

`func (o *RegisterToolGroupRequest) HasMcpEndpoint() bool`

HasMcpEndpoint returns a boolean if a field has been set.

### GetArgs

`func (o *RegisterToolGroupRequest) GetArgs() map[string]AppendRowsRequestRowsInnerValue`

GetArgs returns the Args field if non-nil, zero value otherwise.

### GetArgsOk

`func (o *RegisterToolGroupRequest) GetArgsOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetArgsOk returns a tuple with the Args field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArgs

`func (o *RegisterToolGroupRequest) SetArgs(v map[string]AppendRowsRequestRowsInnerValue)`

SetArgs sets Args field to given value.

### HasArgs

`func (o *RegisterToolGroupRequest) HasArgs() bool`

HasArgs returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


