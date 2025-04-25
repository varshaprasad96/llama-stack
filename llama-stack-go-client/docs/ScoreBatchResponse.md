# ScoreBatchResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DatasetId** | Pointer to **string** |  | [optional] 
**Results** | [**map[string]ScoringResult**](ScoringResult.md) |  | 

## Methods

### NewScoreBatchResponse

`func NewScoreBatchResponse(results map[string]ScoringResult, ) *ScoreBatchResponse`

NewScoreBatchResponse instantiates a new ScoreBatchResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewScoreBatchResponseWithDefaults

`func NewScoreBatchResponseWithDefaults() *ScoreBatchResponse`

NewScoreBatchResponseWithDefaults instantiates a new ScoreBatchResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDatasetId

`func (o *ScoreBatchResponse) GetDatasetId() string`

GetDatasetId returns the DatasetId field if non-nil, zero value otherwise.

### GetDatasetIdOk

`func (o *ScoreBatchResponse) GetDatasetIdOk() (*string, bool)`

GetDatasetIdOk returns a tuple with the DatasetId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDatasetId

`func (o *ScoreBatchResponse) SetDatasetId(v string)`

SetDatasetId sets DatasetId field to given value.

### HasDatasetId

`func (o *ScoreBatchResponse) HasDatasetId() bool`

HasDatasetId returns a boolean if a field has been set.

### GetResults

`func (o *ScoreBatchResponse) GetResults() map[string]ScoringResult`

GetResults returns the Results field if non-nil, zero value otherwise.

### GetResultsOk

`func (o *ScoreBatchResponse) GetResultsOk() (*map[string]ScoringResult, bool)`

GetResultsOk returns a tuple with the Results field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResults

`func (o *ScoreBatchResponse) SetResults(v map[string]ScoringResult)`

SetResults sets Results field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


