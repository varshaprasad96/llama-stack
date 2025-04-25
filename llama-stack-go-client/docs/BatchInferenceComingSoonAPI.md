# \BatchInferenceComingSoonAPI

All URIs are relative to *http://any-hosted-llama-stack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1InferenceChatCompletionPost**](BatchInferenceComingSoonAPI.md#V1InferenceChatCompletionPost) | **Post** /v1/inference/chat-completion | 
[**V1InferenceCompletionPost**](BatchInferenceComingSoonAPI.md#V1InferenceCompletionPost) | **Post** /v1/inference/completion | 



## V1InferenceChatCompletionPost

> ChatCompletionResponse V1InferenceChatCompletionPost(ctx).ChatCompletionRequest(chatCompletionRequest).Execute()





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
	chatCompletionRequest := *openapiclient.NewChatCompletionRequest("ModelId_example", []openapiclient.Message{openapiclient.Message{CompletionMessage: openapiclient.NewCompletionMessage("Role_example", openapiclient.InterleavedContent{InterleavedContentItem: openapiclient.InterleavedContentItem{ImageContentItem: openapiclient.NewImageContentItem("Type_example", *openapiclient.NewImageContentItemImage())}}, "StopReason_example")}}) // ChatCompletionRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BatchInferenceComingSoonAPI.V1InferenceChatCompletionPost(context.Background()).ChatCompletionRequest(chatCompletionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BatchInferenceComingSoonAPI.V1InferenceChatCompletionPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1InferenceChatCompletionPost`: ChatCompletionResponse
	fmt.Fprintf(os.Stdout, "Response from `BatchInferenceComingSoonAPI.V1InferenceChatCompletionPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1InferenceChatCompletionPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chatCompletionRequest** | [**ChatCompletionRequest**](ChatCompletionRequest.md) |  | 

### Return type

[**ChatCompletionResponse**](ChatCompletionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/event-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1InferenceCompletionPost

> CompletionResponse V1InferenceCompletionPost(ctx).CompletionRequest(completionRequest).Execute()





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
	completionRequest := *openapiclient.NewCompletionRequest("ModelId_example", openapiclient.InterleavedContent{InterleavedContentItem: openapiclient.InterleavedContentItem{ImageContentItem: openapiclient.NewImageContentItem("Type_example", *openapiclient.NewImageContentItemImage())}}) // CompletionRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.BatchInferenceComingSoonAPI.V1InferenceCompletionPost(context.Background()).CompletionRequest(completionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `BatchInferenceComingSoonAPI.V1InferenceCompletionPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1InferenceCompletionPost`: CompletionResponse
	fmt.Fprintf(os.Stdout, "Response from `BatchInferenceComingSoonAPI.V1InferenceCompletionPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1InferenceCompletionPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **completionRequest** | [**CompletionRequest**](CompletionRequest.md) |  | 

### Return type

[**CompletionResponse**](CompletionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/event-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

