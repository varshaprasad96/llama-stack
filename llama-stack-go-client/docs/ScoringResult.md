# ScoringResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ScoreRows** | [**[]map[string]AppendRowsRequestRowsInnerValue**](map[string]AppendRowsRequestRowsInnerValue.md) | The scoring result for each row. Each row is a map of column name to value. | 
**AggregatedResults** | [**map[string]AppendRowsRequestRowsInnerValue**](AppendRowsRequestRowsInnerValue.md) | Map of metric name to aggregated value | 

## Methods

### NewScoringResult

`func NewScoringResult(scoreRows []map[string]AppendRowsRequestRowsInnerValue, aggregatedResults map[string]AppendRowsRequestRowsInnerValue, ) *ScoringResult`

NewScoringResult instantiates a new ScoringResult object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewScoringResultWithDefaults

`func NewScoringResultWithDefaults() *ScoringResult`

NewScoringResultWithDefaults instantiates a new ScoringResult object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetScoreRows

`func (o *ScoringResult) GetScoreRows() []map[string]AppendRowsRequestRowsInnerValue`

GetScoreRows returns the ScoreRows field if non-nil, zero value otherwise.

### GetScoreRowsOk

`func (o *ScoringResult) GetScoreRowsOk() (*[]map[string]AppendRowsRequestRowsInnerValue, bool)`

GetScoreRowsOk returns a tuple with the ScoreRows field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScoreRows

`func (o *ScoringResult) SetScoreRows(v []map[string]AppendRowsRequestRowsInnerValue)`

SetScoreRows sets ScoreRows field to given value.


### GetAggregatedResults

`func (o *ScoringResult) GetAggregatedResults() map[string]AppendRowsRequestRowsInnerValue`

GetAggregatedResults returns the AggregatedResults field if non-nil, zero value otherwise.

### GetAggregatedResultsOk

`func (o *ScoringResult) GetAggregatedResultsOk() (*map[string]AppendRowsRequestRowsInnerValue, bool)`

GetAggregatedResultsOk returns a tuple with the AggregatedResults field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAggregatedResults

`func (o *ScoringResult) SetAggregatedResults(v map[string]AppendRowsRequestRowsInnerValue)`

SetAggregatedResults sets AggregatedResults field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


