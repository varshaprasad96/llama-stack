# RegisterScoringFunctionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ScoringFnId** | **string** |  | 
**Description** | **string** |  | 
**ReturnType** | [**ParamType**](ParamType.md) |  | 
**ProviderScoringFnId** | Pointer to **string** |  | [optional] 
**ProviderId** | Pointer to **string** |  | [optional] 
**Params** | Pointer to [**ScoringFnParams**](ScoringFnParams.md) |  | [optional] 

## Methods

### NewRegisterScoringFunctionRequest

`func NewRegisterScoringFunctionRequest(scoringFnId string, description string, returnType ParamType, ) *RegisterScoringFunctionRequest`

NewRegisterScoringFunctionRequest instantiates a new RegisterScoringFunctionRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRegisterScoringFunctionRequestWithDefaults

`func NewRegisterScoringFunctionRequestWithDefaults() *RegisterScoringFunctionRequest`

NewRegisterScoringFunctionRequestWithDefaults instantiates a new RegisterScoringFunctionRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetScoringFnId

`func (o *RegisterScoringFunctionRequest) GetScoringFnId() string`

GetScoringFnId returns the ScoringFnId field if non-nil, zero value otherwise.

### GetScoringFnIdOk

`func (o *RegisterScoringFunctionRequest) GetScoringFnIdOk() (*string, bool)`

GetScoringFnIdOk returns a tuple with the ScoringFnId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScoringFnId

`func (o *RegisterScoringFunctionRequest) SetScoringFnId(v string)`

SetScoringFnId sets ScoringFnId field to given value.


### GetDescription

`func (o *RegisterScoringFunctionRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *RegisterScoringFunctionRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *RegisterScoringFunctionRequest) SetDescription(v string)`

SetDescription sets Description field to given value.


### GetReturnType

`func (o *RegisterScoringFunctionRequest) GetReturnType() ParamType`

GetReturnType returns the ReturnType field if non-nil, zero value otherwise.

### GetReturnTypeOk

`func (o *RegisterScoringFunctionRequest) GetReturnTypeOk() (*ParamType, bool)`

GetReturnTypeOk returns a tuple with the ReturnType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReturnType

`func (o *RegisterScoringFunctionRequest) SetReturnType(v ParamType)`

SetReturnType sets ReturnType field to given value.


### GetProviderScoringFnId

`func (o *RegisterScoringFunctionRequest) GetProviderScoringFnId() string`

GetProviderScoringFnId returns the ProviderScoringFnId field if non-nil, zero value otherwise.

### GetProviderScoringFnIdOk

`func (o *RegisterScoringFunctionRequest) GetProviderScoringFnIdOk() (*string, bool)`

GetProviderScoringFnIdOk returns a tuple with the ProviderScoringFnId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderScoringFnId

`func (o *RegisterScoringFunctionRequest) SetProviderScoringFnId(v string)`

SetProviderScoringFnId sets ProviderScoringFnId field to given value.

### HasProviderScoringFnId

`func (o *RegisterScoringFunctionRequest) HasProviderScoringFnId() bool`

HasProviderScoringFnId returns a boolean if a field has been set.

### GetProviderId

`func (o *RegisterScoringFunctionRequest) GetProviderId() string`

GetProviderId returns the ProviderId field if non-nil, zero value otherwise.

### GetProviderIdOk

`func (o *RegisterScoringFunctionRequest) GetProviderIdOk() (*string, bool)`

GetProviderIdOk returns a tuple with the ProviderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderId

`func (o *RegisterScoringFunctionRequest) SetProviderId(v string)`

SetProviderId sets ProviderId field to given value.

### HasProviderId

`func (o *RegisterScoringFunctionRequest) HasProviderId() bool`

HasProviderId returns a boolean if a field has been set.

### GetParams

`func (o *RegisterScoringFunctionRequest) GetParams() ScoringFnParams`

GetParams returns the Params field if non-nil, zero value otherwise.

### GetParamsOk

`func (o *RegisterScoringFunctionRequest) GetParamsOk() (*ScoringFnParams, bool)`

GetParamsOk returns a tuple with the Params field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParams

`func (o *RegisterScoringFunctionRequest) SetParams(v ScoringFnParams)`

SetParams sets Params field to given value.

### HasParams

`func (o *RegisterScoringFunctionRequest) HasParams() bool`

HasParams returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


