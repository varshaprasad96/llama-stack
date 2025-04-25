# \SafetyAPI

All URIs are relative to *http://any-hosted-llama-stack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1SafetyRunShieldPost**](SafetyAPI.md#V1SafetyRunShieldPost) | **Post** /v1/safety/run-shield | 



## V1SafetyRunShieldPost

> RunShieldResponse V1SafetyRunShieldPost(ctx).RunShieldRequest(runShieldRequest).Execute()





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
	runShieldRequest := *openapiclient.NewRunShieldRequest("ShieldId_example", []openapiclient.Message{openapiclient.Message{CompletionMessage: openapiclient.NewCompletionMessage("Role_example", openapiclient.InterleavedContent{InterleavedContentItem: openapiclient.InterleavedContentItem{ImageContentItem: openapiclient.NewImageContentItem("Type_example", *openapiclient.NewImageContentItemImage())}}, "StopReason_example")}}, map[string]AppendRowsRequestRowsInnerValue{"key": openapiclient.AppendRowsRequest_rows_inner_value{ArrayOfAny: new([]interface{})}}) // RunShieldRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SafetyAPI.V1SafetyRunShieldPost(context.Background()).RunShieldRequest(runShieldRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SafetyAPI.V1SafetyRunShieldPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1SafetyRunShieldPost`: RunShieldResponse
	fmt.Fprintf(os.Stdout, "Response from `SafetyAPI.V1SafetyRunShieldPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1SafetyRunShieldPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **runShieldRequest** | [**RunShieldRequest**](RunShieldRequest.md) |  | 

### Return type

[**RunShieldResponse**](RunShieldResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

