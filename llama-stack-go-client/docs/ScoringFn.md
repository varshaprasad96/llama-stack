# ScoringFn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Identifier** | **string** |  | 
**ProviderResourceId** | **string** |  | 
**ProviderId** | **string** |  | 
**Type** | **string** |  | [default to "scoring_function"]
**Description** | Pointer to **string** |  | [optional] 
**Metadata** | [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | 
**ReturnType** | [**ParamType**](ParamType.md) |  | 
**Params** | Pointer to [**ScoringFnParams**](ScoringFnParams.md) |  | [optional] 

## Methods

### NewScoringFn

`func NewScoringFn(identifier string, providerResourceId string, providerId string, type_ string, metadata map[string]AppendRowsRequestRowsInnerValue, returnType ParamType, ) *ScoringFn`

NewScoringFn instantiates a new ScoringFn object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewScoringFnWithDefaults

`func NewScoringFnWithDefaults() *ScoringFn`

NewScoringFnWithDefaults instantiates a new ScoringFn object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIdentifier

`func (o *ScoringFn) GetIdentifier() string`

GetIdentifier returns the Identifier field if non-nil, zero value otherwise.

### GetIdentifierOk

`func (o *ScoringFn) GetIdentifierOk() (*string, bool)`

GetIdentifierOk returns a tuple with the Identifier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdentifier

`func (o *ScoringFn) SetIdentifier(v string)`

SetIdentifier sets Identifier field to given value.


### GetProviderResourceId

`func (o *ScoringFn) GetProviderResourceId() string`

GetProviderResourceId returns the ProviderResourceId field if non-nil, zero value otherwise.

### GetProviderResourceIdOk

`func (o *ScoringFn) GetProviderResourceIdOk() (*string, bool)`

GetProviderResourceIdOk returns a tuple with the ProviderResourceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderResourceId

`func (o *ScoringFn) SetProviderResourceId(v string)`

SetProviderResourceId sets ProviderResourceId field to given value.


### GetProviderId

`func (o *ScoringFn) GetProviderId() string`

GetProviderId returns the ProviderId field if non-nil, zero value otherwise.

### GetProviderIdOk

`func (o *ScoringFn) GetProviderIdOk() (*string, bool)`

GetProviderIdOk returns a tuple with the ProviderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderId

`func (o *ScoringFn) SetProviderId(v string)`

SetProviderId sets ProviderId field to given value.


### GetType

`func (o *ScoringFn) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ScoringFn) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ScoringFn) SetType(v string)`

SetType sets Type field to given value.


### GetDescription

`func (o *ScoringFn) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ScoringFn) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ScoringFn) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ScoringFn) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetMetadata

`func (o *ScoringFn) GetMetadata() map[string]AppendRowsRequestRowsInnerValue`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *ScoringFn) GetMetadataOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *ScoringFn) SetMetadata(v map[string]AppendRowsRequestRowsInnerValue)`

SetMetadata sets Metadata field to given value.


### GetReturnType

`func (o *ScoringFn) GetReturnType() ParamType`

GetReturnType returns the ReturnType field if non-nil, zero value otherwise.

### GetReturnTypeOk

`func (o *ScoringFn) GetReturnTypeOk() (*ParamType, bool)`

GetReturnTypeOk returns a tuple with the ReturnType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReturnType

`func (o *ScoringFn) SetReturnType(v ParamType)`

SetReturnType sets ReturnType field to given value.


### GetParams

`func (o *ScoringFn) GetParams() ScoringFnParams`

GetParams returns the Params field if non-nil, zero value otherwise.

### GetParamsOk

`func (o *ScoringFn) GetParamsOk() (*ScoringFnParams, bool)`

GetParamsOk returns a tuple with the Params field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParams

`func (o *ScoringFn) SetParams(v ScoringFnParams)`

SetParams sets Params field to given value.

### HasParams

`func (o *ScoringFn) HasParams() bool`

HasParams returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


