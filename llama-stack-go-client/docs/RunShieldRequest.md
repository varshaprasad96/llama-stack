# RunShieldRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ShieldId** | **string** |  | 
**Messages** | [**[]Message**](Message.md) |  | 
**Params** | [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | 

## Methods

### NewRunShieldRequest

`func NewRunShieldRequest(shieldId string, messages []Message, params map[string]AppendRowsRequestRowsInnerValue, ) *RunShieldRequest`

NewRunShieldRequest instantiates a new RunShieldRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRunShieldRequestWithDefaults

`func NewRunShieldRequestWithDefaults() *RunShieldRequest`

NewRunShieldRequestWithDefaults instantiates a new RunShieldRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetShieldId

`func (o *RunShieldRequest) GetShieldId() string`

GetShieldId returns the ShieldId field if non-nil, zero value otherwise.

### GetShieldIdOk

`func (o *RunShieldRequest) GetShieldIdOk() (*string, bool)`

GetShieldIdOk returns a tuple with the ShieldId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShieldId

`func (o *RunShieldRequest) SetShieldId(v string)`

SetShieldId sets ShieldId field to given value.


### GetMessages

`func (o *RunShieldRequest) GetMessages() []Message`

GetMessages returns the Messages field if non-nil, zero value otherwise.

### GetMessagesOk

`func (o *RunShieldRequest) GetMessagesOk() (*[]Message, bool)`

GetMessagesOk returns a tuple with the Messages field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessages

`func (o *RunShieldRequest) SetMessages(v []Message)`

SetMessages sets Messages field to given value.


### GetParams

`func (o *RunShieldRequest) GetParams() map[string]AppendRowsRequestRowsInnerValue`

GetParams returns the Params field if non-nil, zero value otherwise.

### GetParamsOk

`func (o *RunShieldRequest) GetParamsOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetParamsOk returns a tuple with the Params field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParams

`func (o *RunShieldRequest) SetParams(v map[string]AppendRowsRequestRowsInnerValue)`

SetParams sets Params field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


