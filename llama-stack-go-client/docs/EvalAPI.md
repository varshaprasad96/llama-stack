# \EvalAPI

All URIs are relative to *http://any-hosted-llama-stack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1EvalBenchmarksBenchmarkIdEvaluationsPost**](EvalAPI.md#V1EvalBenchmarksBenchmarkIdEvaluationsPost) | **Post** /v1/eval/benchmarks/{benchmark_id}/evaluations | 
[**V1EvalBenchmarksBenchmarkIdJobsJobIdDelete**](EvalAPI.md#V1EvalBenchmarksBenchmarkIdJobsJobIdDelete) | **Delete** /v1/eval/benchmarks/{benchmark_id}/jobs/{job_id} | 
[**V1EvalBenchmarksBenchmarkIdJobsJobIdGet**](EvalAPI.md#V1EvalBenchmarksBenchmarkIdJobsJobIdGet) | **Get** /v1/eval/benchmarks/{benchmark_id}/jobs/{job_id} | 
[**V1EvalBenchmarksBenchmarkIdJobsJobIdResultGet**](EvalAPI.md#V1EvalBenchmarksBenchmarkIdJobsJobIdResultGet) | **Get** /v1/eval/benchmarks/{benchmark_id}/jobs/{job_id}/result | 
[**V1EvalBenchmarksBenchmarkIdJobsPost**](EvalAPI.md#V1EvalBenchmarksBenchmarkIdJobsPost) | **Post** /v1/eval/benchmarks/{benchmark_id}/jobs | 



## V1EvalBenchmarksBenchmarkIdEvaluationsPost

> EvaluateResponse V1EvalBenchmarksBenchmarkIdEvaluationsPost(ctx, benchmarkId).EvaluateRowsRequest(evaluateRowsRequest).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	benchmarkId := "benchmarkId_example" // string | The ID of the benchmark to run the evaluation on.
	evaluateRowsRequest := *openapiclient.NewEvaluateRowsRequest([]map[string]AppendRowsRequestRowsInnerValue{map[string]AppendRowsRequestRowsInnerValue{"key": openapiclient.AppendRowsRequest_rows_inner_value{ArrayOfAny: new([]interface{})}}}, []string{"ScoringFunctions_example"}, *openapiclient.NewBenchmarkConfig(openapiclient.EvalCandidate{AgentCandidate: openapiclient.NewAgentCandidate("Type_example", *openapiclient.NewAgentConfig("Model_example", "Instructions_example"))}, map[string]ScoringFnParams{"key": openapiclient.ScoringFnParams{BasicScoringFnParams: openapiclient.NewBasicScoringFnParams("Type_example")}})) // EvaluateRowsRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EvalAPI.V1EvalBenchmarksBenchmarkIdEvaluationsPost(context.Background(), benchmarkId).EvaluateRowsRequest(evaluateRowsRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EvalAPI.V1EvalBenchmarksBenchmarkIdEvaluationsPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1EvalBenchmarksBenchmarkIdEvaluationsPost`: EvaluateResponse
	fmt.Fprintf(os.Stdout, "Response from `EvalAPI.V1EvalBenchmarksBenchmarkIdEvaluationsPost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**benchmarkId** | **string** | The ID of the benchmark to run the evaluation on. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1EvalBenchmarksBenchmarkIdEvaluationsPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **evaluateRowsRequest** | [**EvaluateRowsRequest**](EvaluateRowsRequest.md) |  | 

### Return type

[**EvaluateResponse**](EvaluateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1EvalBenchmarksBenchmarkIdJobsJobIdDelete

> V1EvalBenchmarksBenchmarkIdJobsJobIdDelete(ctx, benchmarkId, jobId).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	benchmarkId := "benchmarkId_example" // string | The ID of the benchmark to run the evaluation on.
	jobId := "jobId_example" // string | The ID of the job to cancel.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.EvalAPI.V1EvalBenchmarksBenchmarkIdJobsJobIdDelete(context.Background(), benchmarkId, jobId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EvalAPI.V1EvalBenchmarksBenchmarkIdJobsJobIdDelete``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**benchmarkId** | **string** | The ID of the benchmark to run the evaluation on. | 
**jobId** | **string** | The ID of the job to cancel. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1EvalBenchmarksBenchmarkIdJobsJobIdDeleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1EvalBenchmarksBenchmarkIdJobsJobIdGet

> Job V1EvalBenchmarksBenchmarkIdJobsJobIdGet(ctx, benchmarkId, jobId).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	benchmarkId := "benchmarkId_example" // string | The ID of the benchmark to run the evaluation on.
	jobId := "jobId_example" // string | The ID of the job to get the status of.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EvalAPI.V1EvalBenchmarksBenchmarkIdJobsJobIdGet(context.Background(), benchmarkId, jobId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EvalAPI.V1EvalBenchmarksBenchmarkIdJobsJobIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1EvalBenchmarksBenchmarkIdJobsJobIdGet`: Job
	fmt.Fprintf(os.Stdout, "Response from `EvalAPI.V1EvalBenchmarksBenchmarkIdJobsJobIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**benchmarkId** | **string** | The ID of the benchmark to run the evaluation on. | 
**jobId** | **string** | The ID of the job to get the status of. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1EvalBenchmarksBenchmarkIdJobsJobIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1EvalBenchmarksBenchmarkIdJobsJobIdResultGet

> EvaluateResponse V1EvalBenchmarksBenchmarkIdJobsJobIdResultGet(ctx, benchmarkId, jobId).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	benchmarkId := "benchmarkId_example" // string | The ID of the benchmark to run the evaluation on.
	jobId := "jobId_example" // string | The ID of the job to get the result of.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EvalAPI.V1EvalBenchmarksBenchmarkIdJobsJobIdResultGet(context.Background(), benchmarkId, jobId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EvalAPI.V1EvalBenchmarksBenchmarkIdJobsJobIdResultGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1EvalBenchmarksBenchmarkIdJobsJobIdResultGet`: EvaluateResponse
	fmt.Fprintf(os.Stdout, "Response from `EvalAPI.V1EvalBenchmarksBenchmarkIdJobsJobIdResultGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**benchmarkId** | **string** | The ID of the benchmark to run the evaluation on. | 
**jobId** | **string** | The ID of the job to get the result of. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1EvalBenchmarksBenchmarkIdJobsJobIdResultGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**EvaluateResponse**](EvaluateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1EvalBenchmarksBenchmarkIdJobsPost

> Job V1EvalBenchmarksBenchmarkIdJobsPost(ctx, benchmarkId).RunEvalRequest(runEvalRequest).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	benchmarkId := "benchmarkId_example" // string | The ID of the benchmark to run the evaluation on.
	runEvalRequest := *openapiclient.NewRunEvalRequest(*openapiclient.NewBenchmarkConfig(openapiclient.EvalCandidate{AgentCandidate: openapiclient.NewAgentCandidate("Type_example", *openapiclient.NewAgentConfig("Model_example", "Instructions_example"))}, map[string]ScoringFnParams{"key": openapiclient.ScoringFnParams{BasicScoringFnParams: openapiclient.NewBasicScoringFnParams("Type_example")}})) // RunEvalRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EvalAPI.V1EvalBenchmarksBenchmarkIdJobsPost(context.Background(), benchmarkId).RunEvalRequest(runEvalRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EvalAPI.V1EvalBenchmarksBenchmarkIdJobsPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1EvalBenchmarksBenchmarkIdJobsPost`: Job
	fmt.Fprintf(os.Stdout, "Response from `EvalAPI.V1EvalBenchmarksBenchmarkIdJobsPost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**benchmarkId** | **string** | The ID of the benchmark to run the evaluation on. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1EvalBenchmarksBenchmarkIdJobsPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **runEvalRequest** | [**RunEvalRequest**](RunEvalRequest.md) |  | 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

