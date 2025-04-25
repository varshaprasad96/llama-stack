# MemoryRetrievalStep

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TurnId** | **string** | The ID of the turn. | 
**StepId** | **string** | The ID of the step. | 
**StartedAt** | Pointer to **time.Time** | The time the step started. | [optional] 
**CompletedAt** | Pointer to **time.Time** | The time the step completed. | [optional] 
**StepType** | **string** |  | [default to "memory_retrieval"]
**VectorDbIds** | **string** | The IDs of the vector databases to retrieve context from. | 
**InsertedContext** | [**InterleavedContent**](InterleavedContent.md) | The context retrieved from the vector databases. | 

## Methods

### NewMemoryRetrievalStep

`func NewMemoryRetrievalStep(turnId string, stepId string, stepType string, vectorDbIds string, insertedContext InterleavedContent, ) *MemoryRetrievalStep`

NewMemoryRetrievalStep instantiates a new MemoryRetrievalStep object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMemoryRetrievalStepWithDefaults

`func NewMemoryRetrievalStepWithDefaults() *MemoryRetrievalStep`

NewMemoryRetrievalStepWithDefaults instantiates a new MemoryRetrievalStep object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTurnId

`func (o *MemoryRetrievalStep) GetTurnId() string`

GetTurnId returns the TurnId field if non-nil, zero value otherwise.

### GetTurnIdOk

`func (o *MemoryRetrievalStep) GetTurnIdOk() (*string, bool)`

GetTurnIdOk returns a tuple with the TurnId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTurnId

`func (o *MemoryRetrievalStep) SetTurnId(v string)`

SetTurnId sets TurnId field to given value.


### GetStepId

`func (o *MemoryRetrievalStep) GetStepId() string`

GetStepId returns the StepId field if non-nil, zero value otherwise.

### GetStepIdOk

`func (o *MemoryRetrievalStep) GetStepIdOk() (*string, bool)`

GetStepIdOk returns a tuple with the StepId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepId

`func (o *MemoryRetrievalStep) SetStepId(v string)`

SetStepId sets StepId field to given value.


### GetStartedAt

`func (o *MemoryRetrievalStep) GetStartedAt() time.Time`

GetStartedAt returns the StartedAt field if non-nil, zero value otherwise.

### GetStartedAtOk

`func (o *MemoryRetrievalStep) GetStartedAtOk() (*time.Time, bool)`

GetStartedAtOk returns a tuple with the StartedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedAt

`func (o *MemoryRetrievalStep) SetStartedAt(v time.Time)`

SetStartedAt sets StartedAt field to given value.

### HasStartedAt

`func (o *MemoryRetrievalStep) HasStartedAt() bool`

HasStartedAt returns a boolean if a field has been set.

### GetCompletedAt

`func (o *MemoryRetrievalStep) GetCompletedAt() time.Time`

GetCompletedAt returns the CompletedAt field if non-nil, zero value otherwise.

### GetCompletedAtOk

`func (o *MemoryRetrievalStep) GetCompletedAtOk() (*time.Time, bool)`

GetCompletedAtOk returns a tuple with the CompletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompletedAt

`func (o *MemoryRetrievalStep) SetCompletedAt(v time.Time)`

SetCompletedAt sets CompletedAt field to given value.

### HasCompletedAt

`func (o *MemoryRetrievalStep) HasCompletedAt() bool`

HasCompletedAt returns a boolean if a field has been set.

### GetStepType

`func (o *MemoryRetrievalStep) GetStepType() string`

GetStepType returns the StepType field if non-nil, zero value otherwise.

### GetStepTypeOk

`func (o *MemoryRetrievalStep) GetStepTypeOk() (*string, bool)`

GetStepTypeOk returns a tuple with the StepType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStepType

`func (o *MemoryRetrievalStep) SetStepType(v string)`

SetStepType sets StepType field to given value.


### GetVectorDbIds

`func (o *MemoryRetrievalStep) GetVectorDbIds() string`

GetVectorDbIds returns the VectorDbIds field if non-nil, zero value otherwise.

### GetVectorDbIdsOk

`func (o *MemoryRetrievalStep) GetVectorDbIdsOk() (*string, bool)`

GetVectorDbIdsOk returns a tuple with the VectorDbIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVectorDbIds

`func (o *MemoryRetrievalStep) SetVectorDbIds(v string)`

SetVectorDbIds sets VectorDbIds field to given value.


### GetInsertedContext

`func (o *MemoryRetrievalStep) GetInsertedContext() InterleavedContent`

GetInsertedContext returns the InsertedContext field if non-nil, zero value otherwise.

### GetInsertedContextOk

`func (o *MemoryRetrievalStep) GetInsertedContextOk() (*InterleavedContent, bool)`

GetInsertedContextOk returns a tuple with the InsertedContext field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInsertedContext

`func (o *MemoryRetrievalStep) SetInsertedContext(v InterleavedContent)`

SetInsertedContext sets InsertedContext field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


