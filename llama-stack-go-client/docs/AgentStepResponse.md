# AgentStepResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Step** | [**TurnStepsInner**](TurnStepsInner.md) |  | 

## Methods

### NewAgentStepResponse

`func NewAgentStepResponse(step TurnStepsInner, ) *AgentStepResponse`

NewAgentStepResponse instantiates a new AgentStepResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAgentStepResponseWithDefaults

`func NewAgentStepResponseWithDefaults() *AgentStepResponse`

NewAgentStepResponseWithDefaults instantiates a new AgentStepResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStep

`func (o *AgentStepResponse) GetStep() TurnStepsInner`

GetStep returns the Step field if non-nil, zero value otherwise.

### GetStepOk

`func (o *AgentStepResponse) GetStepOk() (*TurnStepsInner, bool)`

GetStepOk returns a tuple with the Step field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStep

`func (o *AgentStepResponse) SetStep(v TurnStepsInner)`

SetStep sets Step field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


