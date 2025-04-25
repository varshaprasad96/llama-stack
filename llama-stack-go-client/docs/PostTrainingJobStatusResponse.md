# PostTrainingJobStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**JobUuid** | **string** |  | 
**Status** | **string** |  | 
**ScheduledAt** | Pointer to **time.Time** |  | [optional] 
**StartedAt** | Pointer to **time.Time** |  | [optional] 
**CompletedAt** | Pointer to **time.Time** |  | [optional] 
**ResourcesAllocated** | Pointer to [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) |  | [optional] 
**Checkpoints** | **[]interface{}** |  | 

## Methods

### NewPostTrainingJobStatusResponse

`func NewPostTrainingJobStatusResponse(jobUuid string, status string, checkpoints []interface{}, ) *PostTrainingJobStatusResponse`

NewPostTrainingJobStatusResponse instantiates a new PostTrainingJobStatusResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPostTrainingJobStatusResponseWithDefaults

`func NewPostTrainingJobStatusResponseWithDefaults() *PostTrainingJobStatusResponse`

NewPostTrainingJobStatusResponseWithDefaults instantiates a new PostTrainingJobStatusResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetJobUuid

`func (o *PostTrainingJobStatusResponse) GetJobUuid() string`

GetJobUuid returns the JobUuid field if non-nil, zero value otherwise.

### GetJobUuidOk

`func (o *PostTrainingJobStatusResponse) GetJobUuidOk() (*string, bool)`

GetJobUuidOk returns a tuple with the JobUuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJobUuid

`func (o *PostTrainingJobStatusResponse) SetJobUuid(v string)`

SetJobUuid sets JobUuid field to given value.


### GetStatus

`func (o *PostTrainingJobStatusResponse) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *PostTrainingJobStatusResponse) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *PostTrainingJobStatusResponse) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetScheduledAt

`func (o *PostTrainingJobStatusResponse) GetScheduledAt() time.Time`

GetScheduledAt returns the ScheduledAt field if non-nil, zero value otherwise.

### GetScheduledAtOk

`func (o *PostTrainingJobStatusResponse) GetScheduledAtOk() (*time.Time, bool)`

GetScheduledAtOk returns a tuple with the ScheduledAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScheduledAt

`func (o *PostTrainingJobStatusResponse) SetScheduledAt(v time.Time)`

SetScheduledAt sets ScheduledAt field to given value.

### HasScheduledAt

`func (o *PostTrainingJobStatusResponse) HasScheduledAt() bool`

HasScheduledAt returns a boolean if a field has been set.

### GetStartedAt

`func (o *PostTrainingJobStatusResponse) GetStartedAt() time.Time`

GetStartedAt returns the StartedAt field if non-nil, zero value otherwise.

### GetStartedAtOk

`func (o *PostTrainingJobStatusResponse) GetStartedAtOk() (*time.Time, bool)`

GetStartedAtOk returns a tuple with the StartedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStartedAt

`func (o *PostTrainingJobStatusResponse) SetStartedAt(v time.Time)`

SetStartedAt sets StartedAt field to given value.

### HasStartedAt

`func (o *PostTrainingJobStatusResponse) HasStartedAt() bool`

HasStartedAt returns a boolean if a field has been set.

### GetCompletedAt

`func (o *PostTrainingJobStatusResponse) GetCompletedAt() time.Time`

GetCompletedAt returns the CompletedAt field if non-nil, zero value otherwise.

### GetCompletedAtOk

`func (o *PostTrainingJobStatusResponse) GetCompletedAtOk() (*time.Time, bool)`

GetCompletedAtOk returns a tuple with the CompletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCompletedAt

`func (o *PostTrainingJobStatusResponse) SetCompletedAt(v time.Time)`

SetCompletedAt sets CompletedAt field to given value.

### HasCompletedAt

`func (o *PostTrainingJobStatusResponse) HasCompletedAt() bool`

HasCompletedAt returns a boolean if a field has been set.

### GetResourcesAllocated

`func (o *PostTrainingJobStatusResponse) GetResourcesAllocated() map[string]AppendRowsRequestRowsInnerValue`

GetResourcesAllocated returns the ResourcesAllocated field if non-nil, zero value otherwise.

### GetResourcesAllocatedOk

`func (o *PostTrainingJobStatusResponse) GetResourcesAllocatedOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetResourcesAllocatedOk returns a tuple with the ResourcesAllocated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResourcesAllocated

`func (o *PostTrainingJobStatusResponse) SetResourcesAllocated(v map[string]AppendRowsRequestRowsInnerValue)`

SetResourcesAllocated sets ResourcesAllocated field to given value.

### HasResourcesAllocated

`func (o *PostTrainingJobStatusResponse) HasResourcesAllocated() bool`

HasResourcesAllocated returns a boolean if a field has been set.

### GetCheckpoints

`func (o *PostTrainingJobStatusResponse) GetCheckpoints() []interface{}`

GetCheckpoints returns the Checkpoints field if non-nil, zero value otherwise.

### GetCheckpointsOk

`func (o *PostTrainingJobStatusResponse) GetCheckpointsOk() (*[]interface{}, bool)`

GetCheckpointsOk returns a tuple with the Checkpoints field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCheckpoints

`func (o *PostTrainingJobStatusResponse) SetCheckpoints(v []interface{})`

SetCheckpoints sets Checkpoints field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


