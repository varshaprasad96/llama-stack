# EvaluateRowsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**InputRows** | [**[]map[string]AppendRowsRequestRowsInnerValue**](map[string]AppendRowsRequestRowsInnerValue.md) | The rows to evaluate. | 
**ScoringFunctions** | **[]string** | The scoring functions to use for the evaluation. | 
**BenchmarkConfig** | [**BenchmarkConfig**](BenchmarkConfig.md) | The configuration for the benchmark. | 

## Methods

### NewEvaluateRowsRequest

`func NewEvaluateRowsRequest(inputRows []map[string]AppendRowsRequestRowsInnerValue, scoringFunctions []string, benchmarkConfig BenchmarkConfig, ) *EvaluateRowsRequest`

NewEvaluateRowsRequest instantiates a new EvaluateRowsRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEvaluateRowsRequestWithDefaults

`func NewEvaluateRowsRequestWithDefaults() *EvaluateRowsRequest`

NewEvaluateRowsRequestWithDefaults instantiates a new EvaluateRowsRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetInputRows

`func (o *EvaluateRowsRequest) GetInputRows() []map[string]AppendRowsRequestRowsInnerValue`

GetInputRows returns the InputRows field if non-nil, zero value otherwise.

### GetInputRowsOk

`func (o *EvaluateRowsRequest) GetInputRowsOk() (*[]map[string]AppendRowsRequestRowsInnerValue, bool)`

GetInputRowsOk returns a tuple with the InputRows field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInputRows

`func (o *EvaluateRowsRequest) SetInputRows(v []map[string]AppendRowsRequestRowsInnerValue)`

SetInputRows sets InputRows field to given value.


### GetScoringFunctions

`func (o *EvaluateRowsRequest) GetScoringFunctions() []string`

GetScoringFunctions returns the ScoringFunctions field if non-nil, zero value otherwise.

### GetScoringFunctionsOk

`func (o *EvaluateRowsRequest) GetScoringFunctionsOk() (*[]string, bool)`

GetScoringFunctionsOk returns a tuple with the ScoringFunctions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScoringFunctions

`func (o *EvaluateRowsRequest) SetScoringFunctions(v []string)`

SetScoringFunctions sets ScoringFunctions field to given value.


### GetBenchmarkConfig

`func (o *EvaluateRowsRequest) GetBenchmarkConfig() BenchmarkConfig`

GetBenchmarkConfig returns the BenchmarkConfig field if non-nil, zero value otherwise.

### GetBenchmarkConfigOk

`func (o *EvaluateRowsRequest) GetBenchmarkConfigOk() (*BenchmarkConfig, bool)`

GetBenchmarkConfigOk returns a tuple with the BenchmarkConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBenchmarkConfig

`func (o *EvaluateRowsRequest) SetBenchmarkConfig(v BenchmarkConfig)`

SetBenchmarkConfig sets BenchmarkConfig field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


