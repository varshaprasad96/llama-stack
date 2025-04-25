# \DatasetIOAPI

All URIs are relative to *http://any-hosted-llama-stack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1DatasetioAppendRowsDatasetIdPost**](DatasetIOAPI.md#V1DatasetioAppendRowsDatasetIdPost) | **Post** /v1/datasetio/append-rows/{dataset_id} | 
[**V1DatasetioIterrowsDatasetIdGet**](DatasetIOAPI.md#V1DatasetioIterrowsDatasetIdGet) | **Get** /v1/datasetio/iterrows/{dataset_id} | 



## V1DatasetioAppendRowsDatasetIdPost

> V1DatasetioAppendRowsDatasetIdPost(ctx, datasetId).AppendRowsRequest(appendRowsRequest).Execute()





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
	datasetId := "datasetId_example" // string | 
	appendRowsRequest := *openapiclient.NewAppendRowsRequest([]map[string]AppendRowsRequestRowsInnerValue{map[string]AppendRowsRequestRowsInnerValue{"key": openapiclient.AppendRowsRequest_rows_inner_value{ArrayOfAny: new([]interface{})}}}) // AppendRowsRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DatasetIOAPI.V1DatasetioAppendRowsDatasetIdPost(context.Background(), datasetId).AppendRowsRequest(appendRowsRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DatasetIOAPI.V1DatasetioAppendRowsDatasetIdPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**datasetId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1DatasetioAppendRowsDatasetIdPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **appendRowsRequest** | [**AppendRowsRequest**](AppendRowsRequest.md) |  | 

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


## V1DatasetioIterrowsDatasetIdGet

> PaginatedResponse V1DatasetioIterrowsDatasetIdGet(ctx, datasetId).StartIndex(startIndex).Limit(limit).Execute()





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
	datasetId := "datasetId_example" // string | The ID of the dataset to get the rows from.
	startIndex := int32(56) // int32 | Index into dataset for the first row to get. Get all rows if None. (optional)
	limit := int32(56) // int32 | The number of rows to get. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DatasetIOAPI.V1DatasetioIterrowsDatasetIdGet(context.Background(), datasetId).StartIndex(startIndex).Limit(limit).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DatasetIOAPI.V1DatasetioIterrowsDatasetIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1DatasetioIterrowsDatasetIdGet`: PaginatedResponse
	fmt.Fprintf(os.Stdout, "Response from `DatasetIOAPI.V1DatasetioIterrowsDatasetIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**datasetId** | **string** | The ID of the dataset to get the rows from. | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1DatasetioIterrowsDatasetIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **startIndex** | **int32** | Index into dataset for the first row to get. Get all rows if None. | 
 **limit** | **int32** | The number of rows to get. | 

### Return type

[**PaginatedResponse**](PaginatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

