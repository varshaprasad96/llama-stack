# \BenchmarksAPI

All URIs are relative to *http://any-hosted-llama-stack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1EvalBenchmarksBenchmarkIdGet**](BenchmarksAPI.md#V1EvalBenchmarksBenchmarkIdGet) | **Get** /v1/eval/benchmarks/{benchmark_id} | 
[**V1EvalBenchmarksGet**](BenchmarksAPI.md#V1EvalBenchmarksGet) | **Get** /v1/eval/benchmarks | 
[**V1EvalBenchmarksPost**](BenchmarksAPI.md#V1EvalBenchmarksPost) | **Post** /v1/eval/benchmarks | 



## V1EvalBenchmarksBenchmarkIdGet

> Benchmark V1EvalBenchmarksBenchmarkIdGet(ctx, benchmarkId).Execute()





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
	benchmarkId := "benchmarkId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BenchmarksAPI.V1EvalBenchmarksBenchmarkIdGet(context.Background(), benchmarkId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BenchmarksAPI.V1EvalBenchmarksBenchmarkIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1EvalBenchmarksBenchmarkIdGet`: Benchmark
	fmt.Fprintf(os.Stdout, "Response from `BenchmarksAPI.V1EvalBenchmarksBenchmarkIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**benchmarkId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1EvalBenchmarksBenchmarkIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**Benchmark**](Benchmark.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1EvalBenchmarksGet

> ListBenchmarksResponse V1EvalBenchmarksGet(ctx).Execute()





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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BenchmarksAPI.V1EvalBenchmarksGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BenchmarksAPI.V1EvalBenchmarksGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1EvalBenchmarksGet`: ListBenchmarksResponse
	fmt.Fprintf(os.Stdout, "Response from `BenchmarksAPI.V1EvalBenchmarksGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiV1EvalBenchmarksGetRequest struct via the builder pattern


### Return type

[**ListBenchmarksResponse**](ListBenchmarksResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1EvalBenchmarksPost

> V1EvalBenchmarksPost(ctx).RegisterBenchmarkRequest(registerBenchmarkRequest).Execute()





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
	registerBenchmarkRequest := *openapiclient.NewRegisterBenchmarkRequest("BenchmarkId_example", "DatasetId_example", []string{"ScoringFunctions_example"}) // RegisterBenchmarkRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.BenchmarksAPI.V1EvalBenchmarksPost(context.Background()).RegisterBenchmarkRequest(registerBenchmarkRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BenchmarksAPI.V1EvalBenchmarksPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1EvalBenchmarksPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registerBenchmarkRequest** | [**RegisterBenchmarkRequest**](RegisterBenchmarkRequest.md) |  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

