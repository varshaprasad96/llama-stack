# RunShieldResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Violation** | Pointer to [**SafetyViolation**](SafetyViolation.md) |  | [optional] 

## Methods

### NewRunShieldResponse

`func NewRunShieldResponse() *RunShieldResponse`

NewRunShieldResponse instantiates a new RunShieldResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRunShieldResponseWithDefaults

`func NewRunShieldResponseWithDefaults() *RunShieldResponse`

NewRunShieldResponseWithDefaults instantiates a new RunShieldResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetViolation

`func (o *RunShieldResponse) GetViolation() SafetyViolation`

GetViolation returns the Violation field if non-nil, zero value otherwise.

### GetViolationOk

`func (o *RunShieldResponse) GetViolationOk() (*SafetyViolation, bool)`

GetViolationOk returns a tuple with the Violation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetViolation

`func (o *RunShieldResponse) SetViolation(v SafetyViolation)`

SetViolation sets Violation field to given value.

### HasViolation

`func (o *RunShieldResponse) HasViolation() bool`

HasViolation returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


