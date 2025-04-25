# BenchmarkConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EvalCandidate** | [**EvalCandidate**](EvalCandidate.md) | The candidate to evaluate. | 
**ScoringParams** | [**map[string]ScoringFnParams**](ScoringFnParams.md) | Map between scoring function id and parameters for each scoring function you want to run | 
**NumExamples** | Pointer to **int32** | (Optional) The number of examples to evaluate. If not provided, all examples in the dataset will be evaluated | [optional] 

## Methods

### NewBenchmarkConfig

`func NewBenchmarkConfig(evalCandidate EvalCandidate, scoringParams map[string]ScoringFnParams, ) *BenchmarkConfig`

NewBenchmarkConfig instantiates a new BenchmarkConfig object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBenchmarkConfigWithDefaults

`func NewBenchmarkConfigWithDefaults() *BenchmarkConfig`

NewBenchmarkConfigWithDefaults instantiates a new BenchmarkConfig object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEvalCandidate

`func (o *BenchmarkConfig) GetEvalCandidate() EvalCandidate`

GetEvalCandidate returns the EvalCandidate field if non-nil, zero value otherwise.

### GetEvalCandidateOk

`func (o *BenchmarkConfig) GetEvalCandidateOk() (*EvalCandidate, bool)`

GetEvalCandidateOk returns a tuple with the EvalCandidate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvalCandidate

`func (o *BenchmarkConfig) SetEvalCandidate(v EvalCandidate)`

SetEvalCandidate sets EvalCandidate field to given value.


### GetScoringParams

`func (o *BenchmarkConfig) GetScoringParams() map[string]ScoringFnParams`

GetScoringParams returns the ScoringParams field if non-nil, zero value otherwise.

### GetScoringParamsOk

`func (o *BenchmarkConfig) GetScoringParamsOk() (*map[string]ScoringFnParams, bool)`

GetScoringParamsOk returns a tuple with the ScoringParams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScoringParams

`func (o *BenchmarkConfig) SetScoringParams(v map[string]ScoringFnParams)`

SetScoringParams sets ScoringParams field to given value.


### GetNumExamples

`func (o *BenchmarkConfig) GetNumExamples() int32`

GetNumExamples returns the NumExamples field if non-nil, zero value otherwise.

### GetNumExamplesOk

`func (o *BenchmarkConfig) GetNumExamplesOk() (*int32, bool)`

GetNumExamplesOk returns a tuple with the NumExamples field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNumExamples

`func (o *BenchmarkConfig) SetNumExamples(v int32)`

SetNumExamples sets NumExamples field to given value.

### HasNumExamples

`func (o *BenchmarkConfig) HasNumExamples() bool`

HasNumExamples returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


