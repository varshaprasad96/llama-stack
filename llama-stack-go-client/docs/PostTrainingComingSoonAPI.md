# \PostTrainingComingSoonAPI

All URIs are relative to *http://any-hosted-llama-stack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1PostTrainingJobArtifactsGet**](PostTrainingComingSoonAPI.md#V1PostTrainingJobArtifactsGet) | **Get** /v1/post-training/job/artifacts | 
[**V1PostTrainingJobCancelPost**](PostTrainingComingSoonAPI.md#V1PostTrainingJobCancelPost) | **Post** /v1/post-training/job/cancel | 
[**V1PostTrainingJobStatusGet**](PostTrainingComingSoonAPI.md#V1PostTrainingJobStatusGet) | **Get** /v1/post-training/job/status | 
[**V1PostTrainingJobsGet**](PostTrainingComingSoonAPI.md#V1PostTrainingJobsGet) | **Get** /v1/post-training/jobs | 
[**V1PostTrainingPreferenceOptimizePost**](PostTrainingComingSoonAPI.md#V1PostTrainingPreferenceOptimizePost) | **Post** /v1/post-training/preference-optimize | 
[**V1PostTrainingSupervisedFineTunePost**](PostTrainingComingSoonAPI.md#V1PostTrainingSupervisedFineTunePost) | **Post** /v1/post-training/supervised-fine-tune | 



## V1PostTrainingJobArtifactsGet

> PostTrainingJobArtifactsResponse V1PostTrainingJobArtifactsGet(ctx).JobUuid(jobUuid).Execute()





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
	jobUuid := "jobUuid_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.PostTrainingComingSoonAPI.V1PostTrainingJobArtifactsGet(context.Background()).JobUuid(jobUuid).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PostTrainingComingSoonAPI.V1PostTrainingJobArtifactsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1PostTrainingJobArtifactsGet`: PostTrainingJobArtifactsResponse
	fmt.Fprintf(os.Stdout, "Response from `PostTrainingComingSoonAPI.V1PostTrainingJobArtifactsGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1PostTrainingJobArtifactsGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobUuid** | **string** |  | 

### Return type

[**PostTrainingJobArtifactsResponse**](PostTrainingJobArtifactsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1PostTrainingJobCancelPost

> V1PostTrainingJobCancelPost(ctx).CancelTrainingJobRequest(cancelTrainingJobRequest).Execute()





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
	cancelTrainingJobRequest := *openapiclient.NewCancelTrainingJobRequest("JobUuid_example") // CancelTrainingJobRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.PostTrainingComingSoonAPI.V1PostTrainingJobCancelPost(context.Background()).CancelTrainingJobRequest(cancelTrainingJobRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PostTrainingComingSoonAPI.V1PostTrainingJobCancelPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1PostTrainingJobCancelPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancelTrainingJobRequest** | [**CancelTrainingJobRequest**](CancelTrainingJobRequest.md) |  | 

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


## V1PostTrainingJobStatusGet

> PostTrainingJobStatusResponse V1PostTrainingJobStatusGet(ctx).JobUuid(jobUuid).Execute()





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
	jobUuid := "jobUuid_example" // string | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.PostTrainingComingSoonAPI.V1PostTrainingJobStatusGet(context.Background()).JobUuid(jobUuid).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PostTrainingComingSoonAPI.V1PostTrainingJobStatusGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1PostTrainingJobStatusGet`: PostTrainingJobStatusResponse
	fmt.Fprintf(os.Stdout, "Response from `PostTrainingComingSoonAPI.V1PostTrainingJobStatusGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1PostTrainingJobStatusGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobUuid** | **string** |  | 

### Return type

[**PostTrainingJobStatusResponse**](PostTrainingJobStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1PostTrainingJobsGet

> ListPostTrainingJobsResponse V1PostTrainingJobsGet(ctx).Execute()





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
	resp, r, err := apiClient.PostTrainingComingSoonAPI.V1PostTrainingJobsGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PostTrainingComingSoonAPI.V1PostTrainingJobsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1PostTrainingJobsGet`: ListPostTrainingJobsResponse
	fmt.Fprintf(os.Stdout, "Response from `PostTrainingComingSoonAPI.V1PostTrainingJobsGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiV1PostTrainingJobsGetRequest struct via the builder pattern


### Return type

[**ListPostTrainingJobsResponse**](ListPostTrainingJobsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1PostTrainingPreferenceOptimizePost

> PostTrainingJob V1PostTrainingPreferenceOptimizePost(ctx).PreferenceOptimizeRequest(preferenceOptimizeRequest).Execute()





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
	preferenceOptimizeRequest := *openapiclient.NewPreferenceOptimizeRequest("JobUuid_example", "FinetunedModel_example", *openapiclient.NewDPOAlignmentConfig(float32(123), float32(123), float32(123), float32(123)), *openapiclient.NewTrainingConfig(int32(123), int32(123), int32(123)), map[string]AppendRowsRequestRowsInnerValue{"key": openapiclient.AppendRowsRequest_rows_inner_value{ArrayOfAny: new([]interface{})}}, map[string]AppendRowsRequestRowsInnerValue{"key": openapiclient.AppendRowsRequest_rows_inner_value{ArrayOfAny: new([]interface{})}}) // PreferenceOptimizeRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.PostTrainingComingSoonAPI.V1PostTrainingPreferenceOptimizePost(context.Background()).PreferenceOptimizeRequest(preferenceOptimizeRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PostTrainingComingSoonAPI.V1PostTrainingPreferenceOptimizePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1PostTrainingPreferenceOptimizePost`: PostTrainingJob
	fmt.Fprintf(os.Stdout, "Response from `PostTrainingComingSoonAPI.V1PostTrainingPreferenceOptimizePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1PostTrainingPreferenceOptimizePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preferenceOptimizeRequest** | [**PreferenceOptimizeRequest**](PreferenceOptimizeRequest.md) |  | 

### Return type

[**PostTrainingJob**](PostTrainingJob.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1PostTrainingSupervisedFineTunePost

> PostTrainingJob V1PostTrainingSupervisedFineTunePost(ctx).SupervisedFineTuneRequest(supervisedFineTuneRequest).Execute()





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
	supervisedFineTuneRequest := *openapiclient.NewSupervisedFineTuneRequest("JobUuid_example", *openapiclient.NewTrainingConfig(int32(123), int32(123), int32(123)), map[string]AppendRowsRequestRowsInnerValue{"key": openapiclient.AppendRowsRequest_rows_inner_value{ArrayOfAny: new([]interface{})}}, map[string]AppendRowsRequestRowsInnerValue{"key": openapiclient.AppendRowsRequest_rows_inner_value{ArrayOfAny: new([]interface{})}}) // SupervisedFineTuneRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.PostTrainingComingSoonAPI.V1PostTrainingSupervisedFineTunePost(context.Background()).SupervisedFineTuneRequest(supervisedFineTuneRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `PostTrainingComingSoonAPI.V1PostTrainingSupervisedFineTunePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1PostTrainingSupervisedFineTunePost`: PostTrainingJob
	fmt.Fprintf(os.Stdout, "Response from `PostTrainingComingSoonAPI.V1PostTrainingSupervisedFineTunePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1PostTrainingSupervisedFineTunePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supervisedFineTuneRequest** | [**SupervisedFineTuneRequest**](SupervisedFineTuneRequest.md) |  | 

### Return type

[**PostTrainingJob**](PostTrainingJob.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

