# PostTrainingJobArtifactsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**JobUuid** | **string** |  | 
**Checkpoints** | **[]interface{}** |  | 

## Methods

### NewPostTrainingJobArtifactsResponse

`func NewPostTrainingJobArtifactsResponse(jobUuid string, checkpoints []interface{}, ) *PostTrainingJobArtifactsResponse`

NewPostTrainingJobArtifactsResponse instantiates a new PostTrainingJobArtifactsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPostTrainingJobArtifactsResponseWithDefaults

`func NewPostTrainingJobArtifactsResponseWithDefaults() *PostTrainingJobArtifactsResponse`

NewPostTrainingJobArtifactsResponseWithDefaults instantiates a new PostTrainingJobArtifactsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetJobUuid

`func (o *PostTrainingJobArtifactsResponse) GetJobUuid() string`

GetJobUuid returns the JobUuid field if non-nil, zero value otherwise.

### GetJobUuidOk

`func (o *PostTrainingJobArtifactsResponse) GetJobUuidOk() (*string, bool)`

GetJobUuidOk returns a tuple with the JobUuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJobUuid

`func (o *PostTrainingJobArtifactsResponse) SetJobUuid(v string)`

SetJobUuid sets JobUuid field to given value.


### GetCheckpoints

`func (o *PostTrainingJobArtifactsResponse) GetCheckpoints() []interface{}`

GetCheckpoints returns the Checkpoints field if non-nil, zero value otherwise.

### GetCheckpointsOk

`func (o *PostTrainingJobArtifactsResponse) GetCheckpointsOk() (*[]interface{}, bool)`

GetCheckpointsOk returns a tuple with the Checkpoints field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCheckpoints

`func (o *PostTrainingJobArtifactsResponse) SetCheckpoints(v []interface{})`

SetCheckpoints sets Checkpoints field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


