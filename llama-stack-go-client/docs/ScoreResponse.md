# ScoreResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Results** | [**map[string]ScoringResult**](ScoringResult.md) | A map of scoring function name to ScoringResult. | 

## Methods

### NewScoreResponse

`func NewScoreResponse(results map[string]ScoringResult, ) *ScoreResponse`

NewScoreResponse instantiates a new ScoreResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewScoreResponseWithDefaults

`func NewScoreResponseWithDefaults() *ScoreResponse`

NewScoreResponseWithDefaults instantiates a new ScoreResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetResults

`func (o *ScoreResponse) GetResults() map[string]ScoringResult`

GetResults returns the Results field if non-nil, zero value otherwise.

### GetResultsOk

`func (o *ScoreResponse) GetResultsOk() (*map[string]ScoringResult, bool)`

GetResultsOk returns a tuple with the Results field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResults

`func (o *ScoreResponse) SetResults(v map[string]ScoringResult)`

SetResults sets Results field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


