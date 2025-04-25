# ScoreBatchRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DatasetId** | **string** |  | 
**ScoringFunctions** | [**map[string]ScoreRequestScoringFunctionsValue**](ScoreRequestScoringFunctionsValue.md) |  | 
**SaveResultsDataset** | **bool** |  | 

## Methods

### NewScoreBatchRequest

`func NewScoreBatchRequest(datasetId string, scoringFunctions map[string]ScoreRequestScoringFunctionsValue, saveResultsDataset bool, ) *ScoreBatchRequest`

NewScoreBatchRequest instantiates a new ScoreBatchRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewScoreBatchRequestWithDefaults

`func NewScoreBatchRequestWithDefaults() *ScoreBatchRequest`

NewScoreBatchRequestWithDefaults instantiates a new ScoreBatchRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDatasetId

`func (o *ScoreBatchRequest) GetDatasetId() string`

GetDatasetId returns the DatasetId field if non-nil, zero value otherwise.

### GetDatasetIdOk

`func (o *ScoreBatchRequest) GetDatasetIdOk() (*string, bool)`

GetDatasetIdOk returns a tuple with the DatasetId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDatasetId

`func (o *ScoreBatchRequest) SetDatasetId(v string)`

SetDatasetId sets DatasetId field to given value.


### GetScoringFunctions

`func (o *ScoreBatchRequest) GetScoringFunctions() map[string]ScoreRequestScoringFunctionsValue`

GetScoringFunctions returns the ScoringFunctions field if non-nil, zero value otherwise.

### GetScoringFunctionsOk

`func (o *ScoreBatchRequest) GetScoringFunctionsOk() (*map[string]ScoreRequestScoringFunctionsValue, bool)`

GetScoringFunctionsOk returns a tuple with the ScoringFunctions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScoringFunctions

`func (o *ScoreBatchRequest) SetScoringFunctions(v map[string]ScoreRequestScoringFunctionsValue)`

SetScoringFunctions sets ScoringFunctions field to given value.


### GetSaveResultsDataset

`func (o *ScoreBatchRequest) GetSaveResultsDataset() bool`

GetSaveResultsDataset returns the SaveResultsDataset field if non-nil, zero value otherwise.

### GetSaveResultsDatasetOk

`func (o *ScoreBatchRequest) GetSaveResultsDatasetOk() (*bool, bool)`

GetSaveResultsDatasetOk returns a tuple with the SaveResultsDataset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSaveResultsDataset

`func (o *ScoreBatchRequest) SetSaveResultsDataset(v bool)`

SetSaveResultsDataset sets SaveResultsDataset field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


