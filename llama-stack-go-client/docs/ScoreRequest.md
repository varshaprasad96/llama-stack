# ScoreRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**InputRows** | [**[]map[string]AppendRowsRequestRowsInnerValue**](map[string]AppendRowsRequestRowsInnerValue.md) | The rows to score. | 
**ScoringFunctions** | [**map[string]ScoreRequestScoringFunctionsValue**](ScoreRequestScoringFunctionsValue.md) | The scoring functions to use for the scoring. | 

## Methods

### NewScoreRequest

`func NewScoreRequest(inputRows []map[string]AppendRowsRequestRowsInnerValue, scoringFunctions map[string]ScoreRequestScoringFunctionsValue, ) *ScoreRequest`

NewScoreRequest instantiates a new ScoreRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewScoreRequestWithDefaults

`func NewScoreRequestWithDefaults() *ScoreRequest`

NewScoreRequestWithDefaults instantiates a new ScoreRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetInputRows

`func (o *ScoreRequest) GetInputRows() []map[string]AppendRowsRequestRowsInnerValue`

GetInputRows returns the InputRows field if non-nil, zero value otherwise.

### GetInputRowsOk

`func (o *ScoreRequest) GetInputRowsOk() (*[]map[string]AppendRowsRequestRowsInnerValue, bool)`

GetInputRowsOk returns a tuple with the InputRows field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInputRows

`func (o *ScoreRequest) SetInputRows(v []map[string]AppendRowsRequestRowsInnerValue)`

SetInputRows sets InputRows field to given value.


### GetScoringFunctions

`func (o *ScoreRequest) GetScoringFunctions() map[string]ScoreRequestScoringFunctionsValue`

GetScoringFunctions returns the ScoringFunctions field if non-nil, zero value otherwise.

### GetScoringFunctionsOk

`func (o *ScoreRequest) GetScoringFunctionsOk() (*map[string]ScoreRequestScoringFunctionsValue, bool)`

GetScoringFunctionsOk returns a tuple with the ScoringFunctions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScoringFunctions

`func (o *ScoreRequest) SetScoringFunctions(v map[string]ScoreRequestScoringFunctionsValue)`

SetScoringFunctions sets ScoringFunctions field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


