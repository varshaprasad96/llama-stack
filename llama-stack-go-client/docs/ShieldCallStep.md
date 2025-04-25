# ShieldCallStep

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TurnId** | **string** | The ID of the turn. | 
**StepId** | **string** | The ID of the step. | 
**StartedAt** | Pointer to **time.Time** | The time the step started. | [optional] 
**CompletedAt** | Pointer to **time.Time** | The time the step completed. | [optional] 
**StepType** | **string** |  | [default to "shield_call"]
**Violation** | Pointer to [**SafetyViolation**](SafetyViolation.md) | The violation from the shield call. | [optional] 

## Methods

### NewShieldCallStep

`func NewShieldCallStep(turnId string, stepId string, stepType string, ) *ShieldCallStep`

NewShieldCallStep instantiates a new ShieldCallStep object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewShieldCallStepWithDefaults

`func NewShieldCallStepWithDefaults() *ShieldCallStep`

NewShieldCallStepWithDefaults instantiates a new ShieldCallStep object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTurnId

`func (o *ShieldCallStep) GetTurnId() string`

GetTurnId returns the TurnId field if non-nil, zero value otherwise.

### GetTurnIdOk

`func (o *ShieldCallStep) GetTurnIdOk() (*string, bool)`

GetTurnIdOk returns a tuple with the TurnId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTurnId

`func (o *ShieldCallStep) SetTurnId(v string)`

SetTurnId sets TurnId field to given value.


### GetStepId

`func (o *ShieldCallStep) GetStepId() string`

GetStepId returns the StepId field if non-nil, zero value otherwise.

### GetStepIdOk

`func (o *ShieldCallStep) GetStepIdOk() (*string, bool)`

GetStepIdOk returns a tuple with the StepId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepId

`func (o *ShieldCallStep) SetStepId(v string)`

SetStepId sets StepId field to given value.


### GetStartedAt

`func (o *ShieldCallStep) GetStartedAt() time.Time`

GetStartedAt returns the StartedAt field if non-nil, zero value otherwise.

### GetStartedAtOk

`func (o *ShieldCallStep) GetStartedAtOk() (*time.Time, bool)`

GetStartedAtOk returns a tuple with the StartedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedAt

`func (o *ShieldCallStep) SetStartedAt(v time.Time)`

SetStartedAt sets StartedAt field to given value.

### HasStartedAt

`func (o *ShieldCallStep) HasStartedAt() bool`

HasStartedAt returns a boolean if a field has been set.

### GetCompletedAt

`func (o *ShieldCallStep) GetCompletedAt() time.Time`

GetCompletedAt returns the CompletedAt field if non-nil, zero value otherwise.

### GetCompletedAtOk

`func (o *ShieldCallStep) GetCompletedAtOk() (*time.Time, bool)`

GetCompletedAtOk returns a tuple with the CompletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompletedAt

`func (o *ShieldCallStep) SetCompletedAt(v time.Time)`

SetCompletedAt sets CompletedAt field to given value.

### HasCompletedAt

`func (o *ShieldCallStep) HasCompletedAt() bool`

HasCompletedAt returns a boolean if a field has been set.

### GetStepType

`func (o *ShieldCallStep) GetStepType() string`

GetStepType returns the StepType field if non-nil, zero value otherwise.

### GetStepTypeOk

`func (o *ShieldCallStep) GetStepTypeOk() (*string, bool)`

GetStepTypeOk returns a tuple with the StepType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepType

`func (o *ShieldCallStep) SetStepType(v string)`

SetStepType sets StepType field to given value.


### GetViolation

`func (o *ShieldCallStep) GetViolation() SafetyViolation`

GetViolation returns the Violation field if non-nil, zero value otherwise.

### GetViolationOk

`func (o *ShieldCallStep) GetViolationOk() (*SafetyViolation, bool)`

GetViolationOk returns a tuple with the Violation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetViolation

`func (o *ShieldCallStep) SetViolation(v SafetyViolation)`

SetViolation sets Violation field to given value.

### HasViolation

`func (o *ShieldCallStep) HasViolation() bool`

HasViolation returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


