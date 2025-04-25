# SafetyViolation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ViolationLevel** | [**ViolationLevel**](ViolationLevel.md) |  | 
**UserMessage** | Pointer to **string** |  | [optional] 
**Metadata** | [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | 

## Methods

### NewSafetyViolation

`func NewSafetyViolation(violationLevel ViolationLevel, metadata map[string]AppendRowsRequestRowsInnerValue, ) *SafetyViolation`

NewSafetyViolation instantiates a new SafetyViolation object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSafetyViolationWithDefaults

`func NewSafetyViolationWithDefaults() *SafetyViolation`

NewSafetyViolationWithDefaults instantiates a new SafetyViolation object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetViolationLevel

`func (o *SafetyViolation) GetViolationLevel() ViolationLevel`

GetViolationLevel returns the ViolationLevel field if non-nil, zero value otherwise.

### GetViolationLevelOk

`func (o *SafetyViolation) GetViolationLevelOk() (*ViolationLevel, bool)`

GetViolationLevelOk returns a tuple with the ViolationLevel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetViolationLevel

`func (o *SafetyViolation) SetViolationLevel(v ViolationLevel)`

SetViolationLevel sets ViolationLevel field to given value.


### GetUserMessage

`func (o *SafetyViolation) GetUserMessage() string`

GetUserMessage returns the UserMessage field if non-nil, zero value otherwise.

### GetUserMessageOk

`func (o *SafetyViolation) GetUserMessageOk() (*string, bool)`

GetUserMessageOk returns a tuple with the UserMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserMessage

`func (o *SafetyViolation) SetUserMessage(v string)`

SetUserMessage sets UserMessage field to given value.

### HasUserMessage

`func (o *SafetyViolation) HasUserMessage() bool`

HasUserMessage returns a boolean if a field has been set.

### GetMetadata

`func (o *SafetyViolation) GetMetadata() map[string]AppendRowsRequestRowsInnerValue`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *SafetyViolation) GetMetadataOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *SafetyViolation) SetMetadata(v map[string]AppendRowsRequestRowsInnerValue)`

SetMetadata sets Metadata field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


