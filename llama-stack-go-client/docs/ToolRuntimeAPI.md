# \ToolRuntimeAPI

All URIs are relative to *http://any-hosted-llama-stack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1ToolRuntimeInvokePost**](ToolRuntimeAPI.md#V1ToolRuntimeInvokePost) | **Post** /v1/tool-runtime/invoke | 
[**V1ToolRuntimeListToolsGet**](ToolRuntimeAPI.md#V1ToolRuntimeListToolsGet) | **Get** /v1/tool-runtime/list-tools | 
[**V1ToolRuntimeRagToolInsertPost**](ToolRuntimeAPI.md#V1ToolRuntimeRagToolInsertPost) | **Post** /v1/tool-runtime/rag-tool/insert | 
[**V1ToolRuntimeRagToolQueryPost**](ToolRuntimeAPI.md#V1ToolRuntimeRagToolQueryPost) | **Post** /v1/tool-runtime/rag-tool/query | 



## V1ToolRuntimeInvokePost

> ToolInvocationResult V1ToolRuntimeInvokePost(ctx).InvokeToolRequest(invokeToolRequest).Execute()





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
	invokeToolRequest := *openapiclient.NewInvokeToolRequest("ToolName_example", map[string]AppendRowsRequestRowsInnerValue{"key": openapiclient.AppendRowsRequest_rows_inner_value{ArrayOfAny: new([]interface{})}}) // InvokeToolRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ToolRuntimeAPI.V1ToolRuntimeInvokePost(context.Background()).InvokeToolRequest(invokeToolRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ToolRuntimeAPI.V1ToolRuntimeInvokePost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1ToolRuntimeInvokePost`: ToolInvocationResult
	fmt.Fprintf(os.Stdout, "Response from `ToolRuntimeAPI.V1ToolRuntimeInvokePost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1ToolRuntimeInvokePostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invokeToolRequest** | [**InvokeToolRequest**](InvokeToolRequest.md) |  | 

### Return type

[**ToolInvocationResult**](ToolInvocationResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1ToolRuntimeListToolsGet

> ListToolDefsResponse V1ToolRuntimeListToolsGet(ctx).ToolGroupId(toolGroupId).McpEndpoint(mcpEndpoint).Execute()





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
	toolGroupId := "toolGroupId_example" // string |  (optional)
	mcpEndpoint := *openapiclient.NewURL("Uri_example") // URL |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ToolRuntimeAPI.V1ToolRuntimeListToolsGet(context.Background()).ToolGroupId(toolGroupId).McpEndpoint(mcpEndpoint).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ToolRuntimeAPI.V1ToolRuntimeListToolsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1ToolRuntimeListToolsGet`: ListToolDefsResponse
	fmt.Fprintf(os.Stdout, "Response from `ToolRuntimeAPI.V1ToolRuntimeListToolsGet`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1ToolRuntimeListToolsGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toolGroupId** | **string** |  | 
 **mcpEndpoint** | [**URL**](URL.md) |  | 

### Return type

[**ListToolDefsResponse**](ListToolDefsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1ToolRuntimeRagToolInsertPost

> V1ToolRuntimeRagToolInsertPost(ctx).InsertRequest(insertRequest).Execute()





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
	insertRequest := *openapiclient.NewInsertRequest([]openapiclient.RAGDocument{*openapiclient.NewRAGDocument("DocumentId_example", openapiclient.RAGDocument_content{InterleavedContentItem: openapiclient.InterleavedContentItem{ImageContentItem: openapiclient.NewImageContentItem("Type_example", *openapiclient.NewImageContentItemImage())}}, map[string]AppendRowsRequestRowsInnerValue{"key": openapiclient.AppendRowsRequest_rows_inner_value{ArrayOfAny: new([]interface{})}})}, "VectorDbId_example", int32(123)) // InsertRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ToolRuntimeAPI.V1ToolRuntimeRagToolInsertPost(context.Background()).InsertRequest(insertRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ToolRuntimeAPI.V1ToolRuntimeRagToolInsertPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1ToolRuntimeRagToolInsertPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insertRequest** | [**InsertRequest**](InsertRequest.md) |  | 

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


## V1ToolRuntimeRagToolQueryPost

> RAGQueryResult V1ToolRuntimeRagToolQueryPost(ctx).QueryRequest(queryRequest).Execute()





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
	queryRequest := *openapiclient.NewQueryRequest(openapiclient.InterleavedContent{InterleavedContentItem: openapiclient.InterleavedContentItem{ImageContentItem: openapiclient.NewImageContentItem("Type_example", *openapiclient.NewImageContentItemImage())}}, []string{"VectorDbIds_example"}) // QueryRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ToolRuntimeAPI.V1ToolRuntimeRagToolQueryPost(context.Background()).QueryRequest(queryRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ToolRuntimeAPI.V1ToolRuntimeRagToolQueryPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1ToolRuntimeRagToolQueryPost`: RAGQueryResult
	fmt.Fprintf(os.Stdout, "Response from `ToolRuntimeAPI.V1ToolRuntimeRagToolQueryPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1ToolRuntimeRagToolQueryPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queryRequest** | [**QueryRequest**](QueryRequest.md) |  | 

### Return type

[**RAGQueryResult**](RAGQueryResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

