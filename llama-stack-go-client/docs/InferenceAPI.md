# \InferenceAPI

All URIs are relative to *http://any-hosted-llama-stack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1InferenceBatchChatCompletionPost**](InferenceAPI.md#V1InferenceBatchChatCompletionPost) | **Post** /v1/inference/batch-chat-completion | 
[**V1InferenceBatchCompletionPost**](InferenceAPI.md#V1InferenceBatchCompletionPost) | **Post** /v1/inference/batch-completion | 
[**V1InferenceEmbeddingsPost**](InferenceAPI.md#V1InferenceEmbeddingsPost) | **Post** /v1/inference/embeddings | 
[**V1OpenaiV1ChatCompletionsPost**](InferenceAPI.md#V1OpenaiV1ChatCompletionsPost) | **Post** /v1/openai/v1/chat/completions | 
[**V1OpenaiV1CompletionsPost**](InferenceAPI.md#V1OpenaiV1CompletionsPost) | **Post** /v1/openai/v1/completions | 



## V1InferenceBatchChatCompletionPost

> BatchChatCompletionResponse V1InferenceBatchChatCompletionPost(ctx).BatchChatCompletionRequest(batchChatCompletionRequest).Execute()





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
	batchChatCompletionRequest := *openapiclient.NewBatchChatCompletionRequest("ModelId_example", [][]Message{[]openapiclient.Message{openapiclient.Message{CompletionMessage: openapiclient.NewCompletionMessage("Role_example", openapiclient.InterleavedContent{InterleavedContentItem: openapiclient.InterleavedContentItem{ImageContentItem: openapiclient.NewImageContentItem("Type_example", *openapiclient.NewImageContentItemImage())}}, "StopReason_example")}}}) // BatchChatCompletionRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InferenceAPI.V1InferenceBatchChatCompletionPost(context.Background()).BatchChatCompletionRequest(batchChatCompletionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InferenceAPI.V1InferenceBatchChatCompletionPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1InferenceBatchChatCompletionPost`: BatchChatCompletionResponse
	fmt.Fprintf(os.Stdout, "Response from `InferenceAPI.V1InferenceBatchChatCompletionPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1InferenceBatchChatCompletionPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batchChatCompletionRequest** | [**BatchChatCompletionRequest**](BatchChatCompletionRequest.md) |  | 

### Return type

[**BatchChatCompletionResponse**](BatchChatCompletionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1InferenceBatchCompletionPost

> BatchCompletionResponse V1InferenceBatchCompletionPost(ctx).BatchCompletionRequest(batchCompletionRequest).Execute()





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
	batchCompletionRequest := *openapiclient.NewBatchCompletionRequest("ModelId_example", []openapiclient.InterleavedContent{openapiclient.InterleavedContent{InterleavedContentItem: openapiclient.InterleavedContentItem{ImageContentItem: openapiclient.NewImageContentItem("Type_example", *openapiclient.NewImageContentItemImage())}}}) // BatchCompletionRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InferenceAPI.V1InferenceBatchCompletionPost(context.Background()).BatchCompletionRequest(batchCompletionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InferenceAPI.V1InferenceBatchCompletionPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1InferenceBatchCompletionPost`: BatchCompletionResponse
	fmt.Fprintf(os.Stdout, "Response from `InferenceAPI.V1InferenceBatchCompletionPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1InferenceBatchCompletionPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batchCompletionRequest** | [**BatchCompletionRequest**](BatchCompletionRequest.md) |  | 

### Return type

[**BatchCompletionResponse**](BatchCompletionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1InferenceEmbeddingsPost

> EmbeddingsResponse V1InferenceEmbeddingsPost(ctx).EmbeddingsRequest(embeddingsRequest).Execute()





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
	embeddingsRequest := *openapiclient.NewEmbeddingsRequest("ModelId_example", openapiclient.EmbeddingsRequest_contents{ArrayOfInterleavedContentItem: new([]InterleavedContentItem)}) // EmbeddingsRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InferenceAPI.V1InferenceEmbeddingsPost(context.Background()).EmbeddingsRequest(embeddingsRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InferenceAPI.V1InferenceEmbeddingsPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1InferenceEmbeddingsPost`: EmbeddingsResponse
	fmt.Fprintf(os.Stdout, "Response from `InferenceAPI.V1InferenceEmbeddingsPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1InferenceEmbeddingsPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **embeddingsRequest** | [**EmbeddingsRequest**](EmbeddingsRequest.md) |  | 

### Return type

[**EmbeddingsResponse**](EmbeddingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1OpenaiV1ChatCompletionsPost

> V1OpenaiV1ChatCompletionsPost200Response V1OpenaiV1ChatCompletionsPost(ctx).OpenaiChatCompletionRequest(openaiChatCompletionRequest).Execute()





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
	openaiChatCompletionRequest := *openapiclient.NewOpenaiChatCompletionRequest("Model_example", []openapiclient.OpenAIMessageParam{openapiclient.OpenAIMessageParam{OpenAIAssistantMessageParam: openapiclient.NewOpenAIAssistantMessageParam("Role_example")}}) // OpenaiChatCompletionRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InferenceAPI.V1OpenaiV1ChatCompletionsPost(context.Background()).OpenaiChatCompletionRequest(openaiChatCompletionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InferenceAPI.V1OpenaiV1ChatCompletionsPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1OpenaiV1ChatCompletionsPost`: V1OpenaiV1ChatCompletionsPost200Response
	fmt.Fprintf(os.Stdout, "Response from `InferenceAPI.V1OpenaiV1ChatCompletionsPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1OpenaiV1ChatCompletionsPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **openaiChatCompletionRequest** | [**OpenaiChatCompletionRequest**](OpenaiChatCompletionRequest.md) |  | 

### Return type

[**V1OpenaiV1ChatCompletionsPost200Response**](V1OpenaiV1ChatCompletionsPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1OpenaiV1CompletionsPost

> OpenAICompletion V1OpenaiV1CompletionsPost(ctx).OpenaiCompletionRequest(openaiCompletionRequest).Execute()





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
	openaiCompletionRequest := *openapiclient.NewOpenaiCompletionRequest("Model_example", openapiclient.OpenaiCompletionRequest_prompt{ArrayOfArrayOfInt32: new([][]int32)}) // OpenaiCompletionRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InferenceAPI.V1OpenaiV1CompletionsPost(context.Background()).OpenaiCompletionRequest(openaiCompletionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InferenceAPI.V1OpenaiV1CompletionsPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1OpenaiV1CompletionsPost`: OpenAICompletion
	fmt.Fprintf(os.Stdout, "Response from `InferenceAPI.V1OpenaiV1CompletionsPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1OpenaiV1CompletionsPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **openaiCompletionRequest** | [**OpenaiCompletionRequest**](OpenaiCompletionRequest.md) |  | 

### Return type

[**OpenAICompletion**](OpenAICompletion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

