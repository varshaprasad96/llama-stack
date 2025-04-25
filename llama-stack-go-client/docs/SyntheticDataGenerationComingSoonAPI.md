# \SyntheticDataGenerationComingSoonAPI

All URIs are relative to *http://any-hosted-llama-stack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1SyntheticDataGenerationGeneratePost**](SyntheticDataGenerationComingSoonAPI.md#V1SyntheticDataGenerationGeneratePost) | **Post** /v1/synthetic-data-generation/generate | 



## V1SyntheticDataGenerationGeneratePost

> SyntheticDataGenerationResponse V1SyntheticDataGenerationGeneratePost(ctx).SyntheticDataGenerateRequest(syntheticDataGenerateRequest).Execute()





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
	syntheticDataGenerateRequest := *openapiclient.NewSyntheticDataGenerateRequest([]openapiclient.Message{openapiclient.Message{CompletionMessage: openapiclient.NewCompletionMessage("Role_example", openapiclient.InterleavedContent{InterleavedContentItem: openapiclient.InterleavedContentItem{ImageContentItem: openapiclient.NewImageContentItem("Type_example", *openapiclient.NewImageContentItemImage())}}, "StopReason_example")}}, "FilteringFunction_example") // SyntheticDataGenerateRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SyntheticDataGenerationComingSoonAPI.V1SyntheticDataGenerationGeneratePost(context.Background()).SyntheticDataGenerateRequest(syntheticDataGenerateRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SyntheticDataGenerationComingSoonAPI.V1SyntheticDataGenerationGeneratePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1SyntheticDataGenerationGeneratePost`: SyntheticDataGenerationResponse
	fmt.Fprintf(os.Stdout, "Response from `SyntheticDataGenerationComingSoonAPI.V1SyntheticDataGenerationGeneratePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1SyntheticDataGenerationGeneratePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **syntheticDataGenerateRequest** | [**SyntheticDataGenerateRequest**](SyntheticDataGenerateRequest.md) |  | 

### Return type

[**SyntheticDataGenerationResponse**](SyntheticDataGenerationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

