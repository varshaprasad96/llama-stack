# \TelemetryAPI

All URIs are relative to *http://any-hosted-llama-stack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1TelemetryEventsPost**](TelemetryAPI.md#V1TelemetryEventsPost) | **Post** /v1/telemetry/events | 
[**V1TelemetrySpansExportPost**](TelemetryAPI.md#V1TelemetrySpansExportPost) | **Post** /v1/telemetry/spans/export | 
[**V1TelemetrySpansPost**](TelemetryAPI.md#V1TelemetrySpansPost) | **Post** /v1/telemetry/spans | 
[**V1TelemetrySpansSpanIdTreePost**](TelemetryAPI.md#V1TelemetrySpansSpanIdTreePost) | **Post** /v1/telemetry/spans/{span_id}/tree | 
[**V1TelemetryTracesPost**](TelemetryAPI.md#V1TelemetryTracesPost) | **Post** /v1/telemetry/traces | 
[**V1TelemetryTracesTraceIdGet**](TelemetryAPI.md#V1TelemetryTracesTraceIdGet) | **Get** /v1/telemetry/traces/{trace_id} | 
[**V1TelemetryTracesTraceIdSpansSpanIdGet**](TelemetryAPI.md#V1TelemetryTracesTraceIdSpansSpanIdGet) | **Get** /v1/telemetry/traces/{trace_id}/spans/{span_id} | 



## V1TelemetryEventsPost

> V1TelemetryEventsPost(ctx).LogEventRequest(logEventRequest).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	logEventRequest := *openapiclient.NewLogEventRequest(openapiclient.Event{MetricEvent: openapiclient.NewMetricEvent("TraceId_example", "SpanId_example", time.Now(), "Type_example", "Metric_example", openapiclient.MetricInResponse_value{Float32: new(float32)}, "Unit_example")}, int32(123)) // LogEventRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TelemetryAPI.V1TelemetryEventsPost(context.Background()).LogEventRequest(logEventRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TelemetryAPI.V1TelemetryEventsPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1TelemetryEventsPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logEventRequest** | [**LogEventRequest**](LogEventRequest.md) |  | 

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


## V1TelemetrySpansExportPost

> V1TelemetrySpansExportPost(ctx).SaveSpansToDatasetRequest(saveSpansToDatasetRequest).Execute()





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
	saveSpansToDatasetRequest := *openapiclient.NewSaveSpansToDatasetRequest([]openapiclient.QueryCondition{*openapiclient.NewQueryCondition("Key_example", openapiclient.QueryConditionOp("eq"), "TODO")}, []string{"AttributesToSave_example"}, "DatasetId_example") // SaveSpansToDatasetRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.TelemetryAPI.V1TelemetrySpansExportPost(context.Background()).SaveSpansToDatasetRequest(saveSpansToDatasetRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TelemetryAPI.V1TelemetrySpansExportPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1TelemetrySpansExportPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saveSpansToDatasetRequest** | [**SaveSpansToDatasetRequest**](SaveSpansToDatasetRequest.md) |  | 

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


## V1TelemetrySpansPost

> QuerySpansResponse V1TelemetrySpansPost(ctx).QuerySpansRequest(querySpansRequest).Execute()





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
	querySpansRequest := *openapiclient.NewQuerySpansRequest([]openapiclient.QueryCondition{*openapiclient.NewQueryCondition("Key_example", openapiclient.QueryConditionOp("eq"), "TODO")}, []string{"AttributesToReturn_example"}) // QuerySpansRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TelemetryAPI.V1TelemetrySpansPost(context.Background()).QuerySpansRequest(querySpansRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TelemetryAPI.V1TelemetrySpansPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1TelemetrySpansPost`: QuerySpansResponse
	fmt.Fprintf(os.Stdout, "Response from `TelemetryAPI.V1TelemetrySpansPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1TelemetrySpansPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **querySpansRequest** | [**QuerySpansRequest**](QuerySpansRequest.md) |  | 

### Return type

[**QuerySpansResponse**](QuerySpansResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1TelemetrySpansSpanIdTreePost

> QuerySpanTreeResponse V1TelemetrySpansSpanIdTreePost(ctx, spanId).GetSpanTreeRequest(getSpanTreeRequest).Execute()





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
	spanId := "spanId_example" // string | 
	getSpanTreeRequest := *openapiclient.NewGetSpanTreeRequest() // GetSpanTreeRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TelemetryAPI.V1TelemetrySpansSpanIdTreePost(context.Background(), spanId).GetSpanTreeRequest(getSpanTreeRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TelemetryAPI.V1TelemetrySpansSpanIdTreePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1TelemetrySpansSpanIdTreePost`: QuerySpanTreeResponse
	fmt.Fprintf(os.Stdout, "Response from `TelemetryAPI.V1TelemetrySpansSpanIdTreePost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**spanId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1TelemetrySpansSpanIdTreePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **getSpanTreeRequest** | [**GetSpanTreeRequest**](GetSpanTreeRequest.md) |  | 

### Return type

[**QuerySpanTreeResponse**](QuerySpanTreeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1TelemetryTracesPost

> QueryTracesResponse V1TelemetryTracesPost(ctx).QueryTracesRequest(queryTracesRequest).Execute()





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
	queryTracesRequest := *openapiclient.NewQueryTracesRequest() // QueryTracesRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TelemetryAPI.V1TelemetryTracesPost(context.Background()).QueryTracesRequest(queryTracesRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TelemetryAPI.V1TelemetryTracesPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1TelemetryTracesPost`: QueryTracesResponse
	fmt.Fprintf(os.Stdout, "Response from `TelemetryAPI.V1TelemetryTracesPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1TelemetryTracesPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queryTracesRequest** | [**QueryTracesRequest**](QueryTracesRequest.md) |  | 

### Return type

[**QueryTracesResponse**](QueryTracesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1TelemetryTracesTraceIdGet

> Trace V1TelemetryTracesTraceIdGet(ctx, traceId).Execute()





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
	traceId := "traceId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TelemetryAPI.V1TelemetryTracesTraceIdGet(context.Background(), traceId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TelemetryAPI.V1TelemetryTracesTraceIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1TelemetryTracesTraceIdGet`: Trace
	fmt.Fprintf(os.Stdout, "Response from `TelemetryAPI.V1TelemetryTracesTraceIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**traceId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1TelemetryTracesTraceIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**Trace**](Trace.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1TelemetryTracesTraceIdSpansSpanIdGet

> Span V1TelemetryTracesTraceIdSpansSpanIdGet(ctx, traceId, spanId).Execute()





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
	traceId := "traceId_example" // string | 
	spanId := "spanId_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TelemetryAPI.V1TelemetryTracesTraceIdSpansSpanIdGet(context.Background(), traceId, spanId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TelemetryAPI.V1TelemetryTracesTraceIdSpansSpanIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1TelemetryTracesTraceIdSpansSpanIdGet`: Span
	fmt.Fprintf(os.Stdout, "Response from `TelemetryAPI.V1TelemetryTracesTraceIdSpansSpanIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**traceId** | **string** |  | 
**spanId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1TelemetryTracesTraceIdSpansSpanIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**Span**](Span.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

