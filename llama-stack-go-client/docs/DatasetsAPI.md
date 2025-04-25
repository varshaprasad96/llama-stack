# \DatasetsAPI

All URIs are relative to *http://any-hosted-llama-stack.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**V1DatasetsDatasetIdDelete**](DatasetsAPI.md#V1DatasetsDatasetIdDelete) | **Delete** /v1/datasets/{dataset_id} | 
[**V1DatasetsDatasetIdGet**](DatasetsAPI.md#V1DatasetsDatasetIdGet) | **Get** /v1/datasets/{dataset_id} | 
[**V1DatasetsGet**](DatasetsAPI.md#V1DatasetsGet) | **Get** /v1/datasets | 
[**V1DatasetsPost**](DatasetsAPI.md#V1DatasetsPost) | **Post** /v1/datasets | 



## V1DatasetsDatasetIdDelete

> V1DatasetsDatasetIdDelete(ctx, datasetId).Execute()





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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.DatasetsAPI.V1DatasetsDatasetIdDelete(context.Background(), datasetId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DatasetsAPI.V1DatasetsDatasetIdDelete``: %v\n", err)
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

Other parameters are passed through a pointer to a apiV1DatasetsDatasetIdDeleteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1DatasetsDatasetIdGet

> Dataset V1DatasetsDatasetIdGet(ctx, datasetId).Execute()





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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DatasetsAPI.V1DatasetsDatasetIdGet(context.Background(), datasetId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DatasetsAPI.V1DatasetsDatasetIdGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1DatasetsDatasetIdGet`: Dataset
	fmt.Fprintf(os.Stdout, "Response from `DatasetsAPI.V1DatasetsDatasetIdGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**datasetId** | **string** |  | 

### Other Parameters

Other parameters are passed through a pointer to a apiV1DatasetsDatasetIdGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1DatasetsGet

> ListDatasetsResponse V1DatasetsGet(ctx).Execute()





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
	resp, r, err := apiClient.DatasetsAPI.V1DatasetsGet(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DatasetsAPI.V1DatasetsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1DatasetsGet`: ListDatasetsResponse
	fmt.Fprintf(os.Stdout, "Response from `DatasetsAPI.V1DatasetsGet`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiV1DatasetsGetRequest struct via the builder pattern


### Return type

[**ListDatasetsResponse**](ListDatasetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## V1DatasetsPost

> Dataset V1DatasetsPost(ctx).RegisterDatasetRequest(registerDatasetRequest).Execute()





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
	registerDatasetRequest := *openapiclient.NewRegisterDatasetRequest("Purpose_example", openapiclient.DataSource{RowsDataSource: openapiclient.NewRowsDataSource("Type_example", []map[string]AppendRowsRequestRowsInnerValue{map[string]AppendRowsRequestRowsInnerValue{"key": openapiclient.AppendRowsRequest_rows_inner_value{ArrayOfAny: new([]interface{})}}})}) // RegisterDatasetRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DatasetsAPI.V1DatasetsPost(context.Background()).RegisterDatasetRequest(registerDatasetRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DatasetsAPI.V1DatasetsPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `V1DatasetsPost`: Dataset
	fmt.Fprintf(os.Stdout, "Response from `DatasetsAPI.V1DatasetsPost`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiV1DatasetsPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registerDatasetRequest** | [**RegisterDatasetRequest**](RegisterDatasetRequest.md) |  | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

