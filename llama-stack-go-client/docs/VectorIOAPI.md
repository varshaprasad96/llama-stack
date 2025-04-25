# \VectorIOAPI

All URIs are relative to *http://any-hosted-llama-stack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1VectorIoInsertPost**](VectorIOAPI.md#V1VectorIoInsertPost) | **Post** /v1/vector-io/insert | 
[**V1VectorIoQueryPost**](VectorIOAPI.md#V1VectorIoQueryPost) | **Post** /v1/vector-io/query | 



## V1VectorIoInsertPost

> V1VectorIoInsertPost(ctx).InsertChunksRequest(insertChunksRequest).Execute()





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
	insertChunksRequest := *openapiclient.NewInsertChunksRequest("VectorDbId_example", []openapiclient.Chunk{*openapiclient.NewChunk(openapiclient.InterleavedContent{InterleavedContentItem: openapiclient.InterleavedContentItem{ImageContentItem: openapiclient.NewImageContentItem("Type_example", *openapiclient.NewImageContentItemImage())}}, map[string]AppendRowsRequestRowsInnerValue{"key": openapiclient.AppendRowsRequest_rows_inner_value{ArrayOfAny: new([]interface{})}})}) // InsertChunksRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.VectorIOAPI.V1VectorIoInsertPost(context.Background()).InsertChunksRequest(insertChunksRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VectorIOAPI.V1VectorIoInsertPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1VectorIoInsertPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insertChunksRequest** | [**InsertChunksRequest**](InsertChunksRequest.md) |  | 

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


## V1VectorIoQueryPost

> QueryChunksResponse V1VectorIoQueryPost(ctx).QueryChunksRequest(queryChunksRequest).Execute()





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
	queryChunksRequest := *openapiclient.NewQueryChunksRequest("VectorDbId_example", openapiclient.InterleavedContent{InterleavedContentItem: openapiclient.InterleavedContentItem{ImageContentItem: openapiclient.NewImageContentItem("Type_example", *openapiclient.NewImageContentItemImage())}}) // QueryChunksRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.VectorIOAPI.V1VectorIoQueryPost(context.Background()).QueryChunksRequest(queryChunksRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `VectorIOAPI.V1VectorIoQueryPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1VectorIoQueryPost`: QueryChunksResponse
	fmt.Fprintf(os.Stdout, "Response from `VectorIOAPI.V1VectorIoQueryPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1VectorIoQueryPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queryChunksRequest** | [**QueryChunksRequest**](QueryChunksRequest.md) |  | 

### Return type

[**QueryChunksResponse**](QueryChunksResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

