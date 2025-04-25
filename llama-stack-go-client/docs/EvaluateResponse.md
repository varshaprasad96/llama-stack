# EvaluateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Generations** | [**[]map[string]AppendRowsRequestRowsInnerValue**](map[string]AppendRowsRequestRowsInnerValue.md) | The generations from the evaluation. | 
**Scores** | [**map[string]ScoringResult**](ScoringResult.md) | The scores from the evaluation. | 

## Methods

### NewEvaluateResponse

`func NewEvaluateResponse(generations []map[string]AppendRowsRequestRowsInnerValue, scores map[string]ScoringResult, ) *EvaluateResponse`

NewEvaluateResponse instantiates a new EvaluateResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEvaluateResponseWithDefaults

`func NewEvaluateResponseWithDefaults() *EvaluateResponse`

NewEvaluateResponseWithDefaults instantiates a new EvaluateResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetGenerations

`func (o *EvaluateResponse) GetGenerations() []map[string]AppendRowsRequestRowsInnerValue`

GetGenerations returns the Generations field if non-nil, zero value otherwise.

### GetGenerationsOk

`func (o *EvaluateResponse) GetGenerationsOk() (*[]map[string]AppendRowsRequestRowsInnerValue, bool)`

GetGenerationsOk returns a tuple with the Generations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGenerations

`func (o *EvaluateResponse) SetGenerations(v []map[string]AppendRowsRequestRowsInnerValue)`

SetGenerations sets Generations field to given value.


### GetScores

`func (o *EvaluateResponse) GetScores() map[string]ScoringResult`

GetScores returns the Scores field if non-nil, zero value otherwise.

### GetScoresOk

`func (o *EvaluateResponse) GetScoresOk() (*map[string]ScoringResult, bool)`

GetScoresOk returns a tuple with the Scores field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScores

`func (o *EvaluateResponse) SetScores(v map[string]ScoringResult)`

SetScores sets Scores field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


